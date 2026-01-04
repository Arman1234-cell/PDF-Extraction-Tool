import os
from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
from rag_master import process_pdf, get_answer 

app = Flask(__name__)
UPLOAD_FOLDER = '/tmp/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["GET"])
def chat_page():
    return render_template("chat.html")

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files['file']
    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)
    
    tags = process_pdf(filepath)
    return jsonify({"message": "Ready!", "tags": tags})

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    answer = get_answer(data.get("message"))
    return jsonify({"response": answer})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860)