[README.md](https://github.com/user-attachments/files/21949561/README.md)
# 🧠 Question-Answering Web App  

A Hugging Face Space powered by **Gradio** for answering user-provided questions from input text.  

🔗 Live Demo: [Hugging Face Space](https://huggingface.co/spaces/Yomex139/question-answering-ap)  

---

## ✨ Features  
- Paste a **context paragraph** and ask either:  
  - **Single Question Mode** → Ask one question at a time.  
  - **Batch Mode** → Ask multiple questions (one per line).  
- Displays the **answer** and a **confidence score**.  
- Clean and interactive Gradio-based UI.  

---

## 🚀 How to Use  
1. **Enter Context**  
   Paste your text into the **Context** box.  

2. **Single Question Mode**  
   - Enter your question in the "Question" field.  
   - Click **Get Answer** to receive the model’s prediction.  

3. **Batch Question Mode**  
   - Enter multiple questions (one per line).  
   - Click **Get Batch Answers** to receive answers for all questions at once.  

---

## ⚙️ Tech Stack  
- **Frontend:** [Gradio](https://gradio.app)  
- **Backend:** [Hugging Face Transformers](https://huggingface.co/transformers/) `pipeline("question-answering")`  
- **Deployment:** [Hugging Face Spaces](https://huggingface.co/spaces)  

---

## 📂 Project Structure  

```
.
├── app.py              # Gradio app and logic
├── requirements.txt    # Dependencies
└── runtime.txt         # (Optional) Python runtime version
```

---

## 🖥️ Run Locally  

Clone the repo and install dependencies:  

```bash
git clone https://github.com/Yomex139/question-answering-app.git
cd question-answering-app
pip install -r requirements.txt
python app.py
```

Then open `http://127.0.0.1:7860/` in your browser.  

---

## 📌 Links  
- 🔗 **Live App on Hugging Face:** [Question-Answering Web App](https://huggingface.co/spaces/Yomex139/question-answering-ap)  
- 🔗 **GitHub Repository:** [Yomex139/question-answering-app](https://github.com/Yomex139/question-answering-app)  
