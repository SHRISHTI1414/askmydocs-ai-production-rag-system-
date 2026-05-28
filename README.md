# AskMyDocs AI

An end-to-end Retrieval-Augmented Generation (RAG) application that allows users to upload PDFs and interact with documents using AI-powered semantic search and retrieval.

---

# Features

* Upload and analyze PDFs
* Semantic search using vector embeddings
* Hybrid retrieval using:

  * Dense Retrieval (Embeddings)
  * Sparse Retrieval (BM25)
* Reranking pipeline
* AI-generated grounded answers
* Source-aware responses
* Interactive Streamlit interface

---

# Tech Stack

## Frontend

* Streamlit

## Backend

* Python

## AI / ML

* Sentence Transformers
* ChromaDB
* BM25
* OpenRouter API
* Embedding-based semantic retrieval

---

# Architecture
User
 ↓
Streamlit UI
 ↓
PDF Upload
 ↓
Text Extraction
 ↓
Chunking
 ↓
Embeddings
 ↓
ChromaDB
 ↓
 Retriever
 ├─> BM25
 └─> Semantic Search
 ↓
Reranker
 ↓
LLM
 ↓
Answer + Sources

---

# Project Structure

```bash
app/
│
├── ui.py
├── pdf_loader.py
├── embeddings.py
├── vector_store.py
├── retriever.py
├── bm25_retriever.py
├── reranker.py
├── generator.py
```

---

# How It Works

## 1. PDF Processing

The uploaded PDF is parsed using PyPDF.

## 2. Chunking

Large text is split into overlapping chunks for efficient retrieval.

## 3. Embedding Creation

SentenceTransformer converts chunks into dense vector embeddings.

## 4. Vector Storage

Embeddings are stored inside ChromaDB.

## 5. Hybrid Retrieval

The system combines:

* Semantic vector similarity
* Keyword-based BM25 retrieval

## 6. Reranking

Retrieved chunks are reranked for higher relevance.

## 7. Answer Generation

Relevant context is passed into the LLM to generate grounded responses.

---

# Installation

```bash
git clone <repo>

cd askmydocs-ai

pip install -r requirements.txt
```

Create `.env`

```env
OPENROUTER_API_KEY=your_key
```

Run:

```bash
streamlit run app/ui.py
```

---

# Future Improvements

* Multi-PDF memory
* Conversational memory
* Streaming responses
* OCR support
* Citation highlighting
* Persistent vector databases
* Better reranking models
* Cloud deployment

---

# Why I Built This

This is my first complete end-to-end AI engineering project focused on understanding how modern RAG systems work internally.

Instead of relying heavily on frameworks, I wanted to manually build:

* retrieval pipelines
* vector databases
* chunking systems
* reranking logic
* grounding workflows

to deeply understand production-style AI systems.
