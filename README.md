<div align="center">

# 📄 DocPulse AI
### *Enterprise-Grade RAG Intelligence Engine*

[![Live Demo](https://img.shields.io/badge/🚀_Live_Demo-DocsPulse_AI-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://docpulse-ai.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)](https://langchain.com)
[![FAISS](https://img.shields.io/badge/VectorDB-FAISS-00A8E8?style=for-the-badge)](https://github.com/facebookresearch/faiss)
[![Gemini](https://img.shields.io/badge/LLM-Gemini%202.5%20Flash-8E44AD?style=for-the-badge&logo=google&logoColor=white)](https://ai.google.dev/)

[🌐 Live Demo](https://docpulse-ai.streamlit.app/) • [📖 System Flow](#-system-architecture) • [🧪 Benchmarking](#-evaluation--benchmarking)

---

</div>

## 📌 Overview

**DocPulse AI** is a production-grade Retrieval-Augmented Generation (RAG) platform designed for fast, accurate, and hallucination-resistant document intelligence. 

By leveraging **Local HuggingFace Embeddings**, **FAISS Vector Indexing**, and **Google Gemini**, DocsPulse AI extracts structured knowledge from unstructured PDFs, DOCX, and TXT files while keeping document retrieval transparent with direct page/source citations.

---

## ⚡ System Architecture

### Visual Pipeline Flow

```mermaid
graph TD
    classDef ui fill:#4B0082,stroke:#fff,stroke-width:2px,color:#fff
    classDef extract fill:#005F73,stroke:#fff,stroke-width:2px,color:#fff
    classDef embed fill:#0A9396,stroke:#fff,stroke-width:2px,color:#fff
    classDef store fill:#E9D8A6,stroke:#000,stroke-width:2px,color:#000
    classDef llm fill:#9B5DE5,stroke:#fff,stroke-width:2px,color:#fff

    UI["💻 User Interface<br/>(Streamlit Frontend)"]:::ui
    Ingest["📄 Document Ingestion<br/>(PDF / DOCX / TXT)"]:::extract
    Parser["🧩 Text Chunking & Metadata<br/>(RecursiveCharacterTextSplitter)"]:::extract
    HF["⚡ Local Vector Engine<br/>(HuggingFace all-MiniLM-L6-v2)"]:::embed
    FAISS[("🗄️ FAISS Vector Store<br/>(Disk Persistent index.faiss)")]:::store
    Gemini["🤖 LLM Synthesis Engine<br/>(Google Gemini 2.5 Flash)"]:::llm

    UI -->|Upload Document| Ingest
    Ingest -->|Raw Document Text| Parser
    Parser -->|Text Chunks + Source Pages| HF
    HF -->|384-Dim Embeddings| FAISS
    UI -->|Ask Question| FAISS
    FAISS -->|Top-K Relevant Chunks| Gemini
    Gemini -->|Streamed Answer + Page Citations| UI



    +-----------------------------------------------------------------------------------+
|                                  USER INTERFACE                                   |
|                        Streamlit Web App (st.session_state)                       |
+-----------------------------------------------------------------------------------+
                                         |
                                         v
+-----------------------------------------------------------------------------------+
|                             DOCUMENT INGESTION LAYER                              |
|           [PDF (PyMuPDF)]    |    [DOCX (python-docx)]    |    [TXT]                  |
+-----------------------------------------------------------------------------------+
                                         |
                                         v
+-----------------------------------------------------------------------------------+
|                            TEXT CHUNKING & PREPROCESSING                          |
|                       Recursive Character Text Splitter                           |
|                      (Preserves Page & Source Metadata)                           |
+-----------------------------------------------------------------------------------+
                                         |
                                         v
+-----------------------------------------------------------------------------------+
|                             LOCAL EMBEDDING PIPELINE                              |
|                   HuggingFace: sentence-transformers/all-MiniLM-L6-v2             |
|                        (Zero API Cost / CPU-Optimized)                            |
+-----------------------------------------------------------------------------------+
                                         |
                                         v
+-----------------------------------------------------------------------------------+
|                              VECTOR INDEX & SEARCH                                |
|                        FAISS (Similarity Indexing)                                |
|                    Local Disk Persistence (`faiss_index/`)                        |
+-----------------------------------------------------------------------------------+
                                         |
                                         v
+-----------------------------------------------------------------------------------+
|                             LLM SYNTHESIS & CITATION                              |
|                     Google Gemini API (gemini-2.5-flash)                          |
|               Structured Prompt + Retrieved Context + Page Citations              |
+-----------------------------------------------------------------------------------+


## 🛠️ Tech Stack & Dependencies

| Category | Technology | Purpose |
| :--- | :--- | :--- |
| **Deployed Web App** | [Streamlit Cloud](https://docpulse-ai.streamlit.app/) | Production app hosting & user interface |
| **Document Parsers** | PyMuPDF (`fitz`), `python-docx` | High-fidelity multi-format text & page extraction |
| **Embedding Engine** | HuggingFace (`sentence-transformers`) | Local 384-dimensional dense vector creation |
| **Vector Index** | FAISS (Facebook AI Similarity Search) | High-performance similarity search & disk storage |
| **LLM Provider** | Google Gemini (`gemini-2.5-flash`) | Generative context synthesis & stream output |
| **Language** | Python 3.10+ | Core pipeline orchestration |


## 🚀 Quickstart Guide (Local Setup)

### 1. Clone Repository & Navigate

```bash
git clone [https://github.com/YOUR_USERNAME/DocPulseAI.git](https://github.com/YOUR_USERNAME/DocPulseAI.git)
cd DocPulseAI

### 2. Create and Activate Virtual Environment

# Windows
python -m venv venv
.venv\Scripts\activate

# Linux / macOS
python3 -m venv venv
source venv/bin/activate

### 3. Install Dependencies

pip install -r requirements.txt

### 4. Configure Environment Variables

GOOGLE_API_KEY=your_actual_gemini_api_key_here

### 5. Launch Your Application

streamlit run app.py

---

<div align="center">

### 🌟 Support the Project

If you found **DocPulse AI** useful or interesting, please consider giving this repository a star on GitHub!

[![GitHub stars](https://img.shields.io/github/stars/YOUR_USERNAME/DocPulseAI?style=social)](https://github.com/YOUR_USERNAME/DocPulseAI)

**[🚀 Launch DocPulse AI Live Demo](https://docpulse-ai.streamlit.app/)**

</div>

## 👤 Author

**Anas Nakhuda**