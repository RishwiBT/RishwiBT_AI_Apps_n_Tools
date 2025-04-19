# 📘 Quantum RAG Bot

Ask questions from your **quantum computing books** using a Retrieval-Augmented Generation (RAG) chatbot powered by **LangChain**, **OpenAI**, and **Google Drive**.

Live Demo 👉 [quantumragbot1.streamlit.app](https://quantumragbot1.streamlit.app/)

---

## 🧠 What it does

- Loads quantum computing book PDFs from **Google Drive**
- Converts them into chunks, embeds them using OpenAI
- Stores them in a **FAISS vector database**
- Lets you ask natural language questions
- Uses a **LangChain QA chain** to answer with citations

---

## 🚀 How to Use This App

### ✅ Option 1: Use It Instantly

Visit the live app here (hosted on Streamlit Cloud):  
🔗 [https://quantumragbot1.streamlit.app](https://quantumragbot1.streamlit.app)

No setup required. The app already includes a few quantum PDFs.

---

### 💻 Option 2: Run It Yourself Locally

#### 1. Clone the Repo

```bash
git clone https://github.com/your-username/Quantum_RAG_Bot.git
cd Quantum_RAG_Bot

Make sure your .env or shell has:
export OPENAI_API_KEY="your-api-key-here"
