"""About Tab UI"""

import streamlit as st


def render_about_page():
    """Render the About RAGNOVA tab."""
    st.subheader("About RAGNOVA")
    st.markdown(
        """
        **RAGNOVA** is a production-oriented Retrieval-Augmented Generation (RAG) assistant for
        document-grounded question answering. It combines semantic retrieval, vector search,
        and large language model generation to deliver responses that are aligned with your indexed content.

        ### System Positioning
        RAGNOVA is designed for practical AI knowledge workflows where answer quality, traceability,
        and configurable model behavior are important. The app supports interactive chat with retrieval context,
        streaming output, and configurable response style.

        ### How Knowledge Is Used
        RAGNOVA does **not** train or fine-tune foundation models on your files during runtime.

        It operates with:
        - Pre-trained embedding models for semantic retrieval
        - Pre-trained LLMs for natural language generation
        - Your indexed document chunks as context at inference time

        This architecture keeps responses grounded in retrieved evidence rather than hidden model memory updates.

        ### Data Sources and Index Layer
        Primary project paths:
        - `data/`: source documents
        - `faiss_store/`: vector index and retrieval metadata

        Supported ingestion formats:
        - PDF, TXT, CSV, XLSX, DOCX, JSON

        ### Response Generation Pipeline
        For each query, RAGNOVA executes:
        1. Query embedding generation
        2. Top-K semantic retrieval from FAISS
        3. Context-grounded prompt construction
        4. LLM response generation (streamed in UI)
        5. Evidence visibility via retrieved chunks

        ### Output Control
        - **Short Summary**: concise response targeting approximately 400-500 words
        - **Detailed**: structured, broader explanation with deeper coverage

        ### Reliability Guidance
        RAGNOVA quality depends on document quality, chunking strategy, and retrieval relevance.
        For best results, maintain clean source files, rebuild index after updates, and validate responses
        against retrieved chunks for critical use cases.

        ### Security and Privacy Notes
        - API key can be provided securely through environment or UI input
        - Retrieval executes against your indexed project data
        - Final generation uses the configured remote model provider
        """
    )
