# 🤖 AI Research Assistant

Fetch, parse, and summarize academic research papers by section (Abstract, Introduction, Methods, Results, Conclusion) using OpenAI GPT-4.

🔗 **Live Demo**: [https://airesearchassistant.streamlit.app](https://airesearchassistant.streamlit.app)

---

## ✨ Features

- 🔍 Fetch papers from **arXiv** by title or ID
- 📄 Extract PDF content using **PyMuPDF**
- 🧠 Summarize section-wise using **OpenAI GPT-4**
- 🔁 Handles long sections with chunked summarization
- 🚀 Streamlit UI with minimal input for quick research browsing

---

## 📦 Tech Stack

| Component       | Tool                             |
|----------------|----------------------------------|
| UI             | Streamlit                        |
| Paper Search   | arXiv API                        |
| PDF Parsing    | PyMuPDF                          |
| LLM            | OpenAI GPT-4                     |
| Summarization  | LangChain-style chunking + GPT   |

---

## 📂 Project Structure

AI_Research_Assistant/
├── app.py              # Streamlit frontend
├── fetch_paper.py      # arXiv fetch logic
├── summarize.py        # Section-based summarization
├── requirements.txt
└── README.md

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/AI_Research_Assistant.git
cd AI_Research_Assistant

2. Install dependencies

pip install -r requirements.txt

3. Set your OpenAI API Key

Set it in your terminal or create a .env file:

export OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

Or, on Streamlit Cloud, add it under App → Settings → Secrets:

OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxx

4. Run the app

streamlit run app.py



⸻

🧠 How It Works
	1.	You enter a title or arXiv ID (e.g., 1904.06560)
	2.	The app fetches the corresponding paper PDF via the arXiv API
	3.	The PDF is parsed and text is extracted section-wise
	4.	Each section is summarized in chunks using OpenAI’s chat.completions API (GPT-4)
	5.	The summaries are displayed interactively

⸻

🛠 Future Roadmap
	•	🔄 Support Semantic Scholar API
	•	🧪 Summarization styles: technical / simplified / critical
	•	💾 Save summaries to Markdown or PDF
	•	📁 Upload your own paper PDFs
	•	🧠 Add vector memory (FAISS/ChromaDB) for Q&A
	•	📊 Extract and summarize figures/tables using GPT-4 Vision

⸻

👨‍🔬 Example Paper

Try this arXiv ID to test the bot:

1904.06560  # BERT Rediscovers the Classical NLP Pipeline



⸻

🙌 Author

Built with ❤️ by Rishwi Thimmaraju
🎓 Quantum & AI Enthusiast | Founder of [QuAIT — Quantum & AI Technologies]

⸻

📜 License

MIT License. Free to use, fork, and enhance. Knowledge wants to be free ✨
