# RAGNOVA Architecture

## Overview

RAGNOVA is a retrieval-augmented generation system for document-grounded answers.

At query time, the app retrieves relevant chunks from a local FAISS index and sends
that context to an LLM to generate the final response.

## Components

- `src/data_loader.py`: Loads supported document formats from `data/`.
- `src/embedding.py`: Splits text into chunks and generates embeddings.
- `src/vectorstore.py`: Builds, saves, and queries FAISS index.
- `src/search.py`: RAG orchestration and summary/streaming response generation.
- `streamlit_app.py`: UI for chat, settings, and developer/about sections.

## Data Flow

1. Ingestion
   - Read documents from `data/`.
   - Split into retrieval-friendly chunks.
   - Create embeddings.
   - Store vectors + metadata in `faiss_store/`.

2. Retrieval
   - Convert user query to embedding.
   - Fetch top-K nearest chunks from FAISS.

3. Generation
   - Build a prompt from retrieved context.
   - Generate response using configured LLM.
   - Return short or detailed answer mode.

## Runtime Notes

- `.env` provides API key configuration.
- Streamlit cache is used for client reuse.
- Rebuild index if source documents change.
