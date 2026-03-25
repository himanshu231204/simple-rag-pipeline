"""Backend: Index Management and Utilities"""

import os
from pathlib import Path


def index_exists(persist_dir: str) -> bool:
    """Check if FAISS index exists."""
    base = Path(persist_dir)
    return (base / "faiss.index").exists() and (base / "metadata.pkl").exists()


def get_source_documents_count(data_dir: str = "data") -> int:
    """Count source documents in data directory."""
    base = Path(data_dir)
    if not base.exists():
        return 0
    patterns = ["**/*.pdf", "**/*.txt", "**/*.csv", "**/*.xlsx", "**/*.docx", "**/*.json"]
    return sum(len(list(base.glob(pattern))) for pattern in patterns)


def build_index(persist_dir: str, embedding_model: str) -> None:
    """Build FAISS index from documents."""
    from src.rag.data_loader import load_all_documents
    from src.rag.vectorstore import FaissVectorStore

    docs = load_all_documents("data")
    store = FaissVectorStore(persist_dir=persist_dir, embedding_model=embedding_model)
    store.build_from_documents(docs)
