# 🤝 Contributing to DocuMind AI

Thank you for your interest in contributing to **DocuMind AI**! We welcome contributions of all kinds, from fixing bugs to improving our RAG architecture.

---

## 🚀 Ways to Contribute

* **🐛 Bug Reports:** Found a parsing error or a UI glitch? Let us know!
* **💡 Feature Requests:** Have an idea for a new AI capability? We'd love to hear it!
* **📚 Documentation:** Help us improve our setup guides and README.
* **💻 Code:** Submit bug fixes, performance optimizations, or new features.
* **🎨 Design:** Improve the Dark/Light mode dashboard or mobile responsiveness.

---

## 🛠️ Contribution Setup

1.  **🍴 Fork the repository**
2.  **Clone your fork:**
    ```bash
    git clone [https://github.com/ghost4488/pdfExtraction.git](https://github.com/ghost4488/pdfExtraction.git)
    cd pdfExtraction
    ```
3.  **🌱 Create a branch:**
    ```bash
    git checkout -b feature/your-feature-name
    ```
4.  **✏️ Make your changes:**
    * Update `rag_master.py` for backend logic.
    * Edit `templates/` or `static/` for UI changes.
5.  **🧪 Test your changes:**
    * Verify RAG accuracy with different PDF types.
    * Test theme toggling and mobile responsiveness.

---

## 📋 Contribution Guidelines

### 💻 Code Standards
* **✨ Clean Code:** Write readable, well-commented code.
* **🎯 Factual Integrity:** Ensure changes to the RAG pipeline maintain maximum factual precision.
* **🌐 Browser Support:** Maintain compatibility with all modern mobile and desktop browsers.

### 🔤 Adding New RAG Capabilities
To add new data types or processing logic:
1.  **📝 Update `rag_master.py`:** Implement the new parsing or generation function.
2.  **🔧 Update HTML/JS:** Ensure the UI correctly displays the new output.
3.  **🎨 Update CSS:** Adjust styles for any new UI elements.

---

## ✨ Adding New Features
Ideas for the roadmap:
* **💾 Export Options:** Save chat transcripts or extracted tables to file.
* **🔢 Bulk Generation:** Process multiple PDFs in a single batch.
* **📊 Advanced Visualization:** Better rendering for complex charts and tables.

---

## 🛡️ Security & Privacy
When contributing, always consider:
* **🔒 API Keys:** Never commit your `GEMINI_API_KEY` to the repository.
* **🚫 No Data Storage:** Do not store user-uploaded PDFs or chat logs on the server.
* **🏠 Client-Side UI:** Keep user interaction logic on the frontend where possible.

---

## 🐛 Bug Reports
Please include:
* **🌐 Browser & OS**
* **📝 Steps to reproduce**
* **✅ Expected vs. ❌ Actual behavior**
* **📸 Screenshots**

---

## 🔄 Pull Request Process
1.  **📖 Update documentation** if needed.
2.  **🧪 Test thoroughly** across devices.
3.  **💬 Write clear commit messages**.
4.  **🔗 Reference related issues**.

---

## 💬 Commit Message Format
`type(scope): brief description`
* **Types:** `feat`, `fix`, `docs`, `style`, `refactor`, `test`

---

## 🎯 Good First Issues
* 📱 Mobile responsiveness tweaks.
* 🎨 Dark/Light mode CSS refinements.
* 📚 Improving factual integrity in AI prompts.

---

## 🌟 Community & Recognition
* 🤝 Be respectful and inclusive.
* 📜 Follow our **Code of Conduct**.
* 🏆 Contributors will be listed in the **README.md**.

---

## ❓ Questions?
* **💬 Discussions:** GitHub Discussions.
* **📧 Contact:** Open an issue or reach out via Hugging Face.
* **💡 Ideas:** Open an issue with the `enhancement` label.

**Thank you for contributing! 🙏**
