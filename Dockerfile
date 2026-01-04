# 1. Use a Python base image
FROM python:3.11-slim

# 2. Set working directory
WORKDIR /app

# 3. Install Linux system dependencies (Tesseract OCR)
# This replaces your Windows "C:\Program Files" paths
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    libtesseract-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# 4. Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy your application code
COPY . .

# 6. Create upload folder with correct permissions
RUN mkdir -p /app/uploads && chmod 777 /app/uploads

# 7. Hugging Face Spaces uses port 7860
EXPOSE 7860

# 8. Run the app with Gunicorn (Production grade)
CMD ["gunicorn", "--bind", "0.0.0.0:7860", "--timeout", "120", "app:app"]