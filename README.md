# Simple RAG Pipeline

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![LangChain](https://img.shields.io/badge/LangChain-RAG-green)
![Embeddings](https://img.shields.io/badge/Embeddings-SentenceTransformers-orange)
![VectorDB](https://img.shields.io/badge/VectorDB-ChromaDB-purple)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

A professional, end-to-end implementation of a Retrieval-Augmented Generation (RAG) workflow using LangChain, Sentence Transformers, and ChromaDB.

This project demonstrates how to:
- Ingest PDF documents from a local data folder
- Split long text into retrieval-friendly chunks
- Generate semantic embeddings for each chunk
- Store embeddings in a persistent vector database
- Build the foundation for fast and relevant LLM retrieval

## RAG Pipeline Diagram

The following diagram summarizes the full indexing and retrieval-generation flow implemented in this project.

![Basic RAG Pipeline](assets/rag2.png)

### Simplified RAG Flow

![Basic RAG Pipeline - Simplified](assets/rag1.png)

Indexing flow:
- Documents are loaded from PDF files
- Content is split into chunks
- Chunk embeddings are generated
- Embeddings and metadata are stored in ChromaDB

Retrieval and generation flow:
- User query is converted to an embedding
- Top-k similar chunks are retrieved from vector DB
- Retrieved context is passed to the LLM
- LLM returns a grounded response

## What This Project Is Doing

The notebook builds a complete document indexing pipeline for RAG systems.

1. Load all PDF files from the `data/` directory
2. Extract document pages and metadata (source file, page info)
3. Split content into overlapping chunks for better retrieval quality
4. Generate dense vector embeddings from chunk text
5. Store chunk text, metadata, and embeddings in ChromaDB

The result is a searchable knowledge base that can be used by a chatbot or QA system.

## Architecture

- Document Loader: `PyPDFLoader` from LangChain Community
- Text Splitter: `RecursiveCharacterTextSplitter`
- Embedding Model: `sentence-transformers` (`all-MiniLM-L6-v2`)
- Vector Database: `ChromaDB` with persistent local storage

## Project Structure

```text
simple-rag-pipeline/
|-- data/                       # Input PDFs + vector store persistence
|   |-- *.pdf
|   |-- vector_store/           # Created automatically by ChromaDB
|-- notebook/
|   |-- doc.ipynb               # Data loading experiments
|   |-- rag_pipeline.ipynb      # Main RAG indexing pipeline
|-- requirements.txt
|-- README.md
```

## Setup

1. Create and activate a virtual environment.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Ensure your PDF files are inside the `data/` folder.

## Running the Pipeline

Open `notebook/rag_pipeline.ipynb` and run cells in order:

1. Import libraries
2. Load PDFs from `data/`
3. Split documents into chunks
4. Initialize embedding model
5. Initialize vector store
6. Generate embeddings and store in ChromaDB (batched inserts)

After successful execution, ChromaDB data is persisted at:

`data/vector_store`

## Why Batching Is Used

Large datasets can exceed vector database request limits if added in a single call.
This project uses batch inserts to:
- Prevent max batch-size errors
- Reduce memory pressure
- Make ingestion more reliable for large document sets

## Next Step

You can now connect a retriever + LLM on top of this indexed vector store to build:
- Document Q and A chatbot
- Internal knowledge assistant
- Semantic search application

## Author

**Himanshu Kumar**

- GitHub: [@himanshu231204](https://github.com/himanshu231204)
- LinkedIn: [himanshu231204](https://www.linkedin.com/in/himanshu231204)
- Twitter/X: [@himanshu231204](https://twitter.com/himanshu231204)
- Email: himanshu231204@gmail.com
