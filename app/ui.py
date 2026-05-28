import streamlit as st
import tempfile
import os

from pdf_loader import extractor, chunk_text
from embeddings import create_embeddings
from vector_store import store_embeddings
from retriever import retrieve_chunks
from bm25_retriever import setup_bm25, bm25_search
from reranker import rerank_results
from generator import generate_answer

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="AskMyDocs AI",
    page_icon="📄",
    layout="wide"
)

# ---------------- HEADER ---------------- #

st.title("📄 AskMyDocs AI")

st.markdown("""
Chat with your PDFs using AI-powered semantic search and retrieval.

### What this app does
- Extracts text from PDFs
- Creates vector embeddings
- Stores data in ChromaDB
- Performs semantic + BM25 retrieval
- Reranks relevant chunks
- Generates grounded AI answers

### Built Using
- Sentence Transformers
- ChromaDB
- BM25
- Streamlit
- OpenRouter API
""")

# ---------------- HOW TO USE ---------------- #

with st.expander("How to use"):

    st.markdown("""
    1. Upload a PDF document  
    2. Ask questions naturally  
    3. AI retrieves relevant context  
    4. Get grounded answers with sources

    ### Example Questions
    - Summarize this document
    - What are the key topics?
    - Explain chapter 2
    - What skills are mentioned?
    - What is this PDF about?
    """)

# ---------------- SIDEBAR ---------------- #

st.sidebar.title("⚙ System Status")

st.sidebar.success("Embedding Model Loaded")
st.sidebar.success("Vector DB Connected")
st.sidebar.success("LLM Connected")

# ---------------- FILE UPLOAD ---------------- #

uploaded_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

# ---------------- CHAT INPUT ---------------- #

query = st.chat_input("Ask a question")

# ---------------- MAIN PIPELINE ---------------- #

if uploaded_file is not None and query:

    with st.spinner("Processing PDF and generating answer..."):

        # ---------- SAVE TEMP PDF ---------- #

        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:

            tmp_file.write(uploaded_file.read())

            pdf_path = tmp_file.name

        # ---------- EXTRACT TEXT ---------- #

        pages = extractor(pdf_path)

        # ---------- CHUNKING ---------- #

        chunks = chunk_text(pages)

        # ---------- BM25 SETUP ---------- #

        setup_bm25(chunks)

        # ---------- EMBEDDINGS ---------- #

        embeddings = create_embeddings(chunks)

        # ---------- STORE IN VECTOR DB ---------- #

        store_embeddings(chunks, embeddings)

        # ---------- VECTOR RETRIEVAL ---------- #

        vector_results = retrieve_chunks(query)

        # ---------- BM25 RETRIEVAL ---------- #

        bm25_results = bm25_search(query)

        # ---------- HYBRID RETRIEVAL ---------- #

        combined_results = vector_results + bm25_results

        unique_results = list(dict.fromkeys(combined_results))

        # ---------- RERANKING ---------- #

        reranked_results = rerank_results(
            query,
            unique_results,
            top_k=3
        )

        # ---------- CONTEXT BUILDING ---------- #

        context = "\n".join(reranked_results)

        # ---------- GENERATE ANSWER ---------- #

        answer = generate_answer(query, context)

    # ---------------- ANSWER UI ---------------- #

    st.markdown("## Answer")

    st.write(answer)

    # ---------------- SOURCES ---------------- #

    st.markdown("## Sources")

    for i, source in enumerate(reranked_results, 1):

        with st.expander(f"Source {i}"):

            st.write(source)

    # ---------- CLEANUP ---------- #

    os.remove(pdf_path)

# ---------------- FOOTER ---------------- #

st.markdown("---")

st.caption(
    "Built by Shrishti Yadav • End-to-End RAG Application"
)