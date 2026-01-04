import os
import uuid
import time
import random
import pymupdf4llm
from google import genai
from chromadb import PersistentClient
from chromadb.utils import embedding_functions
from langchain_text_splitters import RecursiveCharacterTextSplitter

# 1. Initialize Gemini Client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# 2. Setup ChromaDB & Embedding Model
emb_fn = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")
db_client = PersistentClient(path="./chroma_db")
collection = db_client.get_or_create_collection(name="pdf_knowledge", embedding_function=emb_fn)

def safe_generate(prompt, model_name="gemini-2.5-flash"): # Changed from gemini-1.5-flash-002
    """
    Handles 429 Errors with Exponential Backoff and Jitter.
    Updated for Gemini 2.5 Flash stable support.
    """
    max_retries = 5
    base_delay = 2 
    
    for i in range(max_retries):
        try:
            # v1beta now prioritizes 2.5 and 3.0 series models
            response = client.models.generate_content(model=model_name, contents=prompt)
            return response.text
        except Exception as e:
            if "429" in str(e):
                delay = (base_delay * (2 ** i)) + random.uniform(0, 1)
                print(f"Hugging Face IP limited (429). Retrying in {delay:.2f}s...")
                time.sleep(delay)
            elif "404" in str(e):
                print(f"Model {model_name} not found. Ensure you are using gemini-2.5-flash.")
                raise e
            else:
                raise e
    return "Error: API quota exhausted. Please try again in 1 minute."

def process_pdf(filepath):
    """Extracts text, generates tags using safe_generate, and stores in Vector DB."""
    try:
        md_content = pymupdf4llm.to_markdown(filepath, force_ocr=True)
        
        # Step B: Generate dynamic Topic Tags using safe_generate
        tag_prompt = f"List 5 main topics from this text as a comma-separated list:\n\n{md_content[:4000]}"
        tag_text = safe_generate(tag_prompt)
        tags = [t.strip() for t in tag_text.split(",")]

        # Step C: Chunk and store in Vector DB
        splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
        chunks = splitter.split_text(md_content)
        filename = os.path.basename(filepath)
        
        collection.add(
            documents=chunks,
            ids=[f"{filename}-{uuid.uuid4()}" for _ in chunks],
            metadatas=[{"source": filename} for _ in chunks]
        )
        return tags
    except Exception as e:
        print(f"Processing error: {e}")
        return ["Error processing file"]

def get_answer(user_query):
    """Retrieves context and generates answer using retry logic."""
    results = collection.query(query_texts=[user_query], n_results=5)
    context_text = "\n\n".join(results['documents'][0])
    
    prompt = f"""
    Answer the question based ONLY on the following context. 
    If you don't know the answer from the context, say so.
    
    CONTEXT:
    {context_text}
    
    QUESTION:
    {user_query}
    """
    return safe_generate(prompt)