from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA
import os

# 1. Load all PDF files
def load_documents(folder_path):
    documents = []
    for filename in os.listdir(folder_path):
        if filename.endswith('.pdf'):
            loader = PyPDFLoader(os.path.join(folder_path, filename))
            documents.extend(loader.load())
    return documents

# 2. Chunk the documents
def split_documents(documents, chunk_size=1000, chunk_overlap=200):
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    return splitter.split_documents(documents)

# 3. Embed and create FAISS index
def create_vectorstore(chunks):
    embeddings = OpenAIEmbeddings()
    return FAISS.from_documents(chunks, embeddings)

# 4. Create QA chain
def get_rag_chain(vectorstore):
    retriever = vectorstore.as_retriever(search_kwargs={"k": 4})
    llm = OpenAI(temperature=0)
    return RetrievalQA.from_chain_type(llm=llm, retriever=retriever, return_source_documents=True)

# === MAIN ===
def build_rag_bot(books_folder):
    print("[+] Loading documents...")
    docs = load_documents(books_folder)
    print(f"[+] Loaded {len(docs)} pages")

    print("[+] Splitting documents...")
    chunks = split_documents(docs)

    print("[+] Creating FAISS vector store...")
    vectorstore = create_vectorstore(chunks)

    print("[+] Building RAG chain...")
    rag_chain = get_rag_chain(vectorstore)

    return rag_chain

# You can now use:
# rag_bot = build_rag_bot("./books")
# result = rag_bot.run("Explain the phase estimation algorithm")
# print(result)