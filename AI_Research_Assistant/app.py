import streamlit as st
from fetch_paper import fetch_arxiv_pdf
from summarize import summarize_sections
import tempfile
import os

st.set_page_config(page_title="AI Research Assistant", page_icon="📄")

st.title("🤖 AI Research Assistant")
st.markdown("Fetch and summarize academic papers by section using OpenAI GPT-4.")

query = st.text_input("1904.06560")

if query:
    with st.spinner("Fetching paper..."):
        pdf_path = fetch_arxiv_pdf(query)

    if pdf_path:
        st.success("PDF fetched successfully!")
        with st.spinner("Summarizing paper by section..."):
            summaries = summarize_sections(pdf_path)

        for section, summary in summaries.items():
            st.markdown(f"### 🧩 {section}")
            st.write(summary)

        os.remove(pdf_path)  # cleanup
    else:
        st.error("❌ Failed to fetch paper. Try another ID or keyword.")
