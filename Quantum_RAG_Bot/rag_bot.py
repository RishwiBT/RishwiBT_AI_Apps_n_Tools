import os
import gdown
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain_community.llms import OpenAI


# Download from Google Drive
def download_from_gdrive(file_id, save_path):
    url = f"https://drive.google.com/uc?id={file_id}"
    gdown.download(url, save_path, quiet=False)


# Load and parse PDFs
def load_documents_from_drive(file_ids):
    os.makedirs("temp_books", exist_ok=True)
    documents = []

    for i, file_id in enumerate(file_ids):
        save_path = f"temp_books/book_{i}.pdf"
        download_from_gdrive(file_id, save_path)

        loader = PyPDFLoader(save_path)
        documents.extend(loader.load())

    return documents


# Split into chunks
def split_documents(documents, chunk_size=1000, chunk_overlap=200):
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    return splitter.split_documents(documents)


# Embed and store
def create_vectorstore(chunks):
    embeddings = OpenAIEmbeddings()
    return FAISS.from_documents(chunks, embeddings)


# Create the RAG QA chain
def get_rag_chain(vectorstore):
    retriever = vectorstore.as_retriever(search_kwargs={"k": 4})
    llm = OpenAI(temperature=0)
    return RetrievalQA.from_chain_type(llm=llm, retriever=retriever, return_source_documents=True)


# Main entry point
def build_rag_bot(file_ids):
    print("[+] Downloading and loading documents...")
    docs = load_documents_from_drive(file_ids)
    print(f"[+] Loaded {len(docs)} pages")

    print("[+] Splitting into chunks...")
    chunks = split_documents(docs)

    print("[+] Creating FAISS vector store...")
    vectorstore = create_vectorstore(chunks)

    print("[+] Initializing QA chain...")
    return get_rag_chain(vectorstore)
