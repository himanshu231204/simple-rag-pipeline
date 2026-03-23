# Simple RAG Pipeline

<p align="center">
  <img src="assets/rag2.png" alt="RAG Pipeline Diagram" width="800"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python" alt="Python"/>
  <img src="https://img.shields.io/badge/LangChain-RAG-green?style=for-the-badge" alt="LangChain"/>
  <img src="https://img.shields.io/badge/Embeddings-SentenceTransformers-orange?style=for-the-badge" alt="Embeddings"/>
  <img src="https://img.shields.io/badge/VectorDB-ChromaDB-purple?style=for-the-badge" alt="ChromaDB"/>
  <img src="https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge" alt="Status"/>
  <img src="https://img.shields.io/badge/License-MIT-lightgrey?style=for-the-badge" alt="License"/>
</p>

> A professional, end-to-end implementation of a **Retrieval-Augmented Generation (RAG)** pipeline using LangChain, Sentence Transformers, and ChromaDB — designed to ingest PDF documents, generate semantic embeddings, and build a searchable knowledge base ready for LLM-powered Q&A.

---

## 📚 Table of Contents

- [Overview](#-overview)
- [RAG Pipeline Flow](#-rag-pipeline-flow)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the Pipeline](#running-the-pipeline)
- [How It Works](#-how-it-works)
- [Why Batching?](#-why-batching)
- [Next Steps](#-next-steps)
- [Author](#-author)
- [License](#-license)

---

## 🔍 Overview

This project builds a complete **document indexing pipeline** for RAG systems. It takes raw PDF files as input and produces a persistent, semantically-searchable vector store — the foundational layer for any intelligent document assistant.

**What this project demonstrates:**

- 📄 Ingesting PDF documents from a local directory
- ✂️ Splitting long text into retrieval-friendly, overlapping chunks
- 🧠 Generating dense semantic embeddings with Sentence Transformers
- 🗄️ Storing embeddings and metadata in a persistent ChromaDB instance
- 🚀 Building the foundation for fast and context-aware LLM retrieval

---

## 🔄 RAG Pipeline Flow

### Full Indexing & Retrieval Flow

![Full RAG Pipeline](assets/rag2.png)

### Simplified RAG Flow

![Simplified RAG Flow](assets/rag1.png)

**Indexing (Offline):**

```
PDF Documents → Load Pages → Split into Chunks → Generate Embeddings → Store in ChromaDB
```

**Retrieval & Generation (Online):**

```
User Query → Query Embedding → Similarity Search → Top-K Chunks → LLM → Grounded Response
```

---

## ✨ Features

- ✅ Automated PDF loading from a directory using `PyPDFLoader`
- ✅ Intelligent text chunking with configurable size and overlap
- ✅ High-quality semantic embeddings via `all-MiniLM-L6-v2`
- ✅ Persistent local vector store powered by ChromaDB
- ✅ Batched ingestion to handle large document sets reliably
- ✅ Extensible architecture — plug in any LLM for Q&A on top

---

## 🛠️ Tech Stack

| Component         | Technology                        |
|-------------------|-----------------------------------|
| Language          | Python 3.10+                      |
| Framework         | LangChain, LangChain-Community    |
| PDF Parsing       | PyPDF, PyMuPDF                    |
| Embedding Model   | Sentence Transformers (`all-MiniLM-L6-v2`) |
| Vector Database   | ChromaDB (persistent local)       |
| Notebooks         | Jupyter Notebook                  |

---

## 📁 Project Structure

```text
simple-rag-pipeline/
├── assets/
│   ├── rag1.png                    # Simplified RAG flow diagram
│   └── rag2.png                    # Full RAG pipeline diagram
├── data/
│   ├── *.pdf                       # Input PDF documents
│   └── vector_store/               # ChromaDB persistence (auto-created)
├── notebook/
│   ├── doc.ipynb                   # Document loading experiments
│   └── rag_pipeline.ipynb          # Main RAG indexing pipeline
├── requirements.txt
├── LICENSE
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

- Python **3.10** or higher
- `pip` package manager
- One or more PDF files to index

### Installation

**1. Clone the repository:**

```bash
git clone https://github.com/himanshu231204/simple-rag-pipeline.git
cd simple-rag-pipeline
```

**2. Create and activate a virtual environment:**

```bash
# On macOS/Linux
python -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate
```

**3. Install dependencies:**

```bash
pip install -r requirements.txt
```

**4. Add your PDF files:**

Place all PDF documents you want to index inside the `data/` folder:

```bash
cp /path/to/your/document.pdf data/
```

### Running the Pipeline

Open the main notebook and run all cells in order:

```bash
jupyter notebook notebook/rag_pipeline.ipynb
```

**Pipeline steps (executed inside the notebook):**

| Step | Description |
|------|-------------|
| 1 | Import libraries and configure paths |
| 2 | Load all PDFs from `data/` using `PyPDFLoader` |
| 3 | Split documents into overlapping text chunks |
| 4 | Initialize the `all-MiniLM-L6-v2` embedding model |
| 5 | Initialize the ChromaDB vector store |
| 6 | Generate embeddings and insert into ChromaDB (batched) |

After successful execution, the ChromaDB index is persisted at:

```
data/vector_store/
```

---

## ⚙️ How It Works

```
┌─────────────┐    ┌───────────────┐    ┌──────────────────┐    ┌───────────────┐
│  PDF Files  │───▶│ PyPDFLoader   │───▶│ Text Splitter    │───▶│  Embedding    │
│  (data/)    │    │ (pages +      │    │ (chunk_size=500, │    │  Model        │
│             │    │  metadata)    │    │  overlap=50)     │    │  (MiniLM-L6)  │
└─────────────┘    └───────────────┘    └──────────────────┘    └───────┬───────┘
                                                                         │
                                                                         ▼
                                                               ┌─────────────────┐
                                                               │   ChromaDB      │
                                                               │ (vector_store/) │
                                                               └─────────────────┘
```

---

## 📦 Why Batching?

Large document sets can exceed ChromaDB's per-request limits if added in a single call. This project uses **batched inserts** to:

- 🛡️ Prevent `max batch size` errors from the vector database
- 💾 Reduce peak memory usage during ingestion
- 🔄 Make the pipeline reliable and scalable for large corpora

---

## 🔮 Next Steps

The indexed vector store is ready to be connected to a retriever + LLM. You can build:

- 💬 **Document Q&A Chatbot** — answer questions grounded in your PDFs
- 🏢 **Internal Knowledge Assistant** — query company docs, manuals, or reports
- 🔎 **Semantic Search Engine** — surface the most relevant passages instantly

> **Suggested extensions:** Add a Gradio/Streamlit UI, integrate OpenAI / Ollama as the LLM, or expose the pipeline as a REST API.

---

## 👨‍💻 Author

<p>
  <strong>Himanshu Kumar</strong>
</p>

[![GitHub](https://img.shields.io/badge/GitHub-himanshu231204-181717?style=flat-square&logo=github)](https://github.com/himanshu231204)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-himanshu231204-0077B5?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/himanshu231204)
[![Twitter](https://img.shields.io/badge/Twitter-himanshu231204-1DA1F2?style=flat-square&logo=twitter)](https://twitter.com/himanshu231204)
[![Email](https://img.shields.io/badge/Email-himanshu231204%40gmail.com-D14836?style=flat-square&logo=gmail)](mailto:himanshu231204@gmail.com)

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
