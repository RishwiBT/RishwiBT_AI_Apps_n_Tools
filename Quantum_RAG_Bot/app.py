import streamlit as st
from rag_bot import build_rag_bot

st.title("📘 Quantum RAG Bot")
st.markdown("Ask anything from your quantum computing books.")

@st.cache_resource
def load_bot():
    return build_rag_bot("./books")

rag_bot = load_bot()

query = st.text_input("Ask a question:")
if query:
    with st.spinner("Thinking..."):
        result = rag_bot(query)
        st.markdown("### Answer")
        st.write(result["result"])

        st.markdown("### Sources")
        for doc in result["source_documents"]:
            st.write(f"- {doc.metadata['source']}")