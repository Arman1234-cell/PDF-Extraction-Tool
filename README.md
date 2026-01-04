# 📂 PDF-Extraction-Tool

**DocuMind AI** is a professional-grade Retrieval-Augmented Generation (RAG) application that allows you to have natural conversations with your PDF documents. By combining semantic search with the power of Gemini AI, it provides accurate, grounded answers to your most complex document queries.

<div align="center">
  <a href="https://github.com/Arman1234-cell/Assets/raw/main/545607a0-970e-45a7-bd04-e61ada2061a8_removalai_previewcopy.png">
    <img src="https://github.com/Arman1234-cell/Assets/raw/main/545607a0-970e-45a7-bd04-e61ada2061a8_removalai_previewcopy.png" alt="DocuMind AI Header" width="100%">
  </a>
  <h3>🚀 [Live Demo: DocuMind AI](https://huggingface.co/spaces/ghost4488/pdfExtraction)</h3>
</div>

---

## 🌟 Quick Overview
- **Engine:** Google Gemini 2.0 Flash & ChromaDB.
- **Capability:** Instant indexing, automated topic tagging, and cited answers.
- **UI:** Responsive Dark/Light mode dashboard with mobile auto-indexing.
- **Trust:** Grounded responses based strictly on document context to prevent AI hallucinations.

---

## ✨ Key Features
- **🚀 Instant Indexing:** Upload any PDF and start chatting in seconds.
- **🎯 Context-Aware Answers:** Our AI understands the full context of your document to provide precise insights.
- **🏷️ Automated Topic Tagging:** Uses AI to categorize your documents with smart, descriptive tags.
- **🔒 Secure & Private:** Built with privacy in mind—your documents are processed securely.
- **🗑️ Reset Capability:** Built-in "Danger Zone" allows you to wipe all uploaded data and start fresh with one click.

---

## 🛠️ How It Works (RAG Architecture)
The application uses **Retrieval-Augmented Generation (RAG)** to ensure that every answer the AI provides is backed by the actual text in your documents, preventing hallucinations:

1. **Ingestion:** The PDF is parsed using OCR and split into semantic chunks.
2. **Vectorization:** Each chunk is converted into a vector representation and stored in **ChromaDB**.
3. **Retrieval:** When you ask a question, the system performs a semantic search to find the most relevant chunks.
4. **Augmentation:** These relevant chunks are provided to the Gemini model as ground-truth context.
5. **Generation:** The AI generates an answer based *only* on that context.

---

## 🚀 Tech Stack
- **Frontend:** HTML5, CSS3 (Inter & JetBrains Mono fonts), JavaScript.
- **Backend:** Python / Flask.
- **AI Model:** Google Gemini 2.5 Flash.
- **Vector Database:** ChromaDB.
- **OCR Engine:** Tesseract OCR (via PyMuPDF4LLM).
- **Deployment:** Docker on Hugging Face Spaces.

---

## 📥 Getting Started

### Prerequisites
- Python 3.11+
- Google Gemini API Key
- Tesseract OCR (for local development)

### Installation
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/ghost4488/pdfExtraction.git](https://github.com/ghost4488/pdfExtraction.git)
   cd pdfExtraction
