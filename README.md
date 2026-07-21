<div align="center">

# 📄 DocPulse AI
### *Enterprise-Grade RAG Intelligence Engine*

[![Live Demo](https://img.shields.io/badge/🚀_Live_Demo-DocsPulse_AI-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://docpulse-ai.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)](https://langchain.com)
[![FAISS](https://img.shields.io/badge/VectorDB-FAISS-00A8E8?style=for-the-badge)](https://github.com/facebookresearch/faiss)
[![Gemini](https://img.shields.io/badge/LLM-Gemini%203.1%20Flash%20Lite-8E44AD?style=for-the-badge&logo=google&logoColor=white)](https://ai.google.dev/)

[🌐 Live Demo](https://docpulse-ai.streamlit.app/) • [📖 System Architecture](#-system-architecture) • [🚀 Quickstart](#-quickstart-guide-local-setup)

---

</div>

## 📌 Overview

**DocPulse AI** is a production-grade Retrieval-Augmented Generation (RAG) platform designed for fast, accurate, and hallucination-resistant document intelligence.

By leveraging **Local HuggingFace Embeddings**, **FAISS Vector Indexing**, and **Google Gemini**, DocPulse AI extracts structured knowledge from unstructured PDFs, DOCX, and TXT files — while keeping document retrieval transparent with direct page/source citations.

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
    Gemini["🤖 LLM Synthesis Engine<br/>(Google Gemini 3.1 Flash Lite)"]:::llm

    UI -->|Upload Document| Ingest
    Ingest -->|Raw Document Text| Parser
    Parser -->|Text Chunks + Source Pages| HF
    HF -->|384-Dim Embeddings| FAISS
    UI -->|Ask Question| FAISS
    FAISS -->|Top-K Relevant Chunks| Gemini
    Gemini -->|Streamed Answer + Page Citations| UI
```

### Layer-by-Layer Breakdown

```
+-----------------------------------------------------------------------------------+
|                                  USER INTERFACE                                   |
|                        Streamlit Web App (st.session_state)                       |
+-----------------------------------------------------------------------------------+
                                         |
                                         v
+-----------------------------------------------------------------------------------+
|                             DOCUMENT INGESTION LAYER                              |
|           [PDF (PyMuPDF)]    |    [DOCX (python-docx)]    |    [TXT]              |
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
|              Google Gemini API (gemini-3.1-flash-lite / 3-flash-preview)           |
|               Structured Prompt + Retrieved Context + Page Citations              |
+-----------------------------------------------------------------------------------+
```

---

## 🛠️ Tech Stack & Dependencies

| Category | Technology | Purpose |
| :--- | :--- | :--- |
| **Deployed Web App** | [Streamlit Cloud](https://docpulse-ai.streamlit.app/) | Production app hosting & user interface |
| **Document Parsers** | PyMuPDF (`fitz`), `python-docx` | High-fidelity multi-format text & page extraction |
| **Embedding Engine** | HuggingFace (`sentence-transformers`) | Local 384-dimensional dense vector creation |
| **Vector Index** | FAISS (Facebook AI Similarity Search) | High-performance similarity search & disk storage |
| **LLM Provider** | Google Gemini (`gemini-3.1-flash-lite`, `gemini-3-flash-preview`, `gemini-3.1-pro-preview`) | Generative context synthesis & stream output |
| **Language** | Python 3.10+ | Core pipeline orchestration |

---

## 🚀 Quickstart Guide (Local Setup)

### 1. Clone Repository & Navigate

```bash
git clone https://github.com/Anas-Nakhuda/DocPulseAI.git
cd DocPulseAI
```

### 2. Create and Activate Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux / macOS
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root and add your Gemini API key:

```env
GOOGLE_API_KEY=your_actual_gemini_api_key_here
```

> **Tip:** Get your free API key at [Google AI Studio](https://aistudio.google.com/app/apikey).

### 5. Launch the Application

```bash
streamlit run app.py
```

The app will open automatically in your browser at `http://localhost:8501`.

---

## 🗂️ Project Structure

```
DocPulseAI/
├── app.py               # Main Streamlit application
├── eval.py              # Evaluation & benchmarking script
├── check_models.py      # Utility to verify available Gemini models
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables (not committed)
└── faiss_index/         # Persisted FAISS vector index (auto-generated)
```

---

## 📊 Evaluation & Benchmarking

The `eval.py` script provides automated benchmarking of the RAG pipeline:

- **Retrieval accuracy** — measures whether the correct document chunks are returned for a given query
- **Answer faithfulness** — checks that the LLM answer is grounded in the retrieved context
- **Latency profiling** — tracks end-to-end response time per query

To run the evaluation:

```bash
python eval.py
```

---

<div align="center">

### 🌟 Support the Project

If you found **DocPulse AI** useful or interesting, please consider giving this repository a star on GitHub!

[![GitHub stars](https://img.shields.io/github/stars/Anas-Nakhuda/DocPulseAI?style=social)](https://github.com/Anas-Nakhuda/DocPulseAI)

**[🚀 Launch DocPulse AI Live Demo](https://docpulse-ai.streamlit.app/)**

</div>

---

## 👤 Author

**Anas Nakhuda**

[![GitHub](https://img.shields.io/badge/GitHub-Anas--Nakhuda-181717?style=flat-square&logo=github)](https://github.com/Anas-Nakhuda)