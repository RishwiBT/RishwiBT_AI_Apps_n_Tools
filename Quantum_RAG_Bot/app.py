import streamlit as st
from rag_bot import build_rag_bot

st.set_page_config(page_title="Quantum RAG Bot", page_icon="📘")
st.title("📘 Quantum RAG Bot")
st.markdown("Ask questions to your quantum computing books stored in Google Drive.")

# Put your Google Drive file IDs here
BOOK_IDS = [
    "114qzgkbXhdugeTB2R1manwuZ2ubBza99",  # Replace with real file IDs
    "1IVy-dR6VDo_-Kz__UgGR-s-w6bUutgv7"
]

@st.cache_resource
def load_bot():
    return build_rag_bot(BOOK_IDS)

rag_bot = load_bot()

query = st.text_input("💬 Ask a question:")
if query and rag_bot:
    with st.spinner("Thinking..."):
        result = rag_bot.invoke({"query": query})

        if "result" in result:
            st.markdown("### ✅ Answer")
            st.write(result["result"])

        if "source_documents" in result:
            st.markdown("### 📚 Source Documents")
            for doc in result["source_documents"]:
                st.write(f"- {doc.metadata.get('source', 'Unknown')}")
