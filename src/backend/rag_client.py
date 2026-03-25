"""Backend: RAG Client Management"""

import streamlit as st
from src.rag.search import RAGSearch


@st.cache_resource(show_spinner=False)
def get_rag_client(
    persist_dir: str,
    embedding_model: str,
    llm_model: str,
    groq_api_key: str,
) -> RAGSearch:
    """
    Get or create a cached RAG client instance.
    
    Raises:
        ValueError: If embedding model mismatch detected.
    """
    try:
        return RAGSearch(
            persist_dir=persist_dir,
            embedding_model=embedding_model,
            llm_model=llm_model,
            groq_api_key=groq_api_key,
        )
    except ValueError as e:
        raise e
