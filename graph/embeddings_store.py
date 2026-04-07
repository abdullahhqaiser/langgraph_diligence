"""
Embedding pipeline for the DD engine.

Flow:
  raw .txt files  →  LangChain Documents
                  →  SemanticChunker (nomic-embed-text)
                  →  Chroma (persisted under embeddings/<fingerprint>/)

The fingerprint is a short MD5 of the resolved docs_path so the same deal
is never re-embedded twice.  Delete the folder to force a rebuild.
"""

import hashlib
import logging
import os
from pathlib import Path

from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv()

log = logging.getLogger(__name__)

EMBEDDING_MODEL    = "models/gemini-embedding-001"
EMBEDDINGS_BASE    = Path("embeddings")
RETRIEVAL_K        = 10   # chunks returned per stage query


def _fingerprint(docs_path: str) -> str:
    """Short MD5 of the resolved absolute path."""
    resolved = str(Path(docs_path).resolve())
    return hashlib.md5(resolved.encode()).hexdigest()[:12]


def _make_documents(raw_docs: list[str]) -> list[Document]:
    """Convert raw loaded strings (with === FILE: xxx === headers) to Documents."""
    documents: list[Document] = []
    for raw in raw_docs:
        lines = raw.split("\n", 2)
        # Header format: "=== FILE: filename.txt ==="
        header = lines[0]
        filename = header.replace("===", "").replace("FILE:", "").strip()
        body = lines[2] if len(lines) > 2 else (lines[1] if len(lines) > 1 else raw)
        documents.append(Document(page_content=body, metadata={"source": filename}))
    return documents


def build_or_load_vectorstore(docs_path: str, raw_docs: list[str]) -> tuple[Chroma, str]:
    """
    Build a persisted Chroma vector store from raw_docs using semantic chunking,
    or load the existing one if already built for this docs_path.

    Returns (vectorstore, persist_directory).
    """
    fingerprint = _fingerprint(docs_path)
    persist_dir = str(EMBEDDINGS_BASE / fingerprint)
    persist_path = Path(persist_dir)

    embeddings = GoogleGenerativeAIEmbeddings(
        model=EMBEDDING_MODEL,
        google_api_key=os.environ["GEMINI_API_KEY"],
    )

    # ── Load existing store ──────────────────────────────────────────────────
    chroma_db_file = persist_path / "chroma.sqlite3"
    if chroma_db_file.exists():
        log.info(
            "Vector store already exists at %s — loading (delete folder to rebuild)",
            persist_dir,
        )
        vectorstore = Chroma(
            persist_directory=persist_dir,
            embedding_function=embeddings,
        )
        count = vectorstore._collection.count()
        log.info("Loaded %d chunks from existing store", count)
        return vectorstore, persist_dir

    # ── Build new store ──────────────────────────────────────────────────────
    persist_path.mkdir(parents=True, exist_ok=True)
    log.info("Building vector store at %s", persist_dir)

    documents = _make_documents(raw_docs)
    log.info("Converted %d files to Documents", len(documents))

    # RecursiveCharacterTextSplitter — no API calls, fast, reliable.
    # SemanticChunker was dropped: it fires one embedding call per sentence pair
    # which burns through the 100 req/min free-tier quota instantly.
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1200,    # ~300 tokens — comfortably under gemini-embedding-001 limit
        chunk_overlap=150,
        separators=["\n\n", "\n", ". ", " ", ""],
    )
    chunks = splitter.split_documents(documents)
    log.info("Chunking complete — %d chunks from %d document(s)", len(chunks), len(documents))

    for i, chunk in enumerate(chunks):
        src = chunk.metadata.get("source", "unknown")
        log.debug("  chunk %03d  %-50s  %d chars", i, src, len(chunk.page_content))

    # Embed and persist
    log.info("Embedding %d chunks with %s ...", len(chunks), EMBEDDING_MODEL)
    vectorstore = Chroma.from_documents(
        chunks,
        embeddings,
        persist_directory=persist_dir,
    )
    log.info("Vector store persisted — %d chunks indexed", len(chunks))
    return vectorstore, persist_dir


def get_retriever(persist_dir: str, k: int = RETRIEVAL_K):
    """Load an existing Chroma store and return a retriever."""
    embeddings = GoogleGenerativeAIEmbeddings(
        model=EMBEDDING_MODEL,
        google_api_key=os.environ["GEMINI_API_KEY"],
    )
    vectorstore = Chroma(
        persist_directory=persist_dir,
        embedding_function=embeddings,
    )
    return vectorstore.as_retriever(search_kwargs={"k": k})


def retrieve_for_stage(persist_dir: str, stage: dict) -> str:
    """
    Build a query from the stage objective + checklist, retrieve the top-K
    most semantically relevant chunks, and return them as a single string.
    """
    query = stage["objective"] + "\n" + "\n".join(stage["checklist"])
    retriever = get_retriever(persist_dir)

    log.info("Retrieving top-%d chunks for: %s", RETRIEVAL_K, stage["objective"][:60])
    docs = retriever.invoke(query)

    # Group by source file for readability in the prompt
    grouped: dict[str, list[str]] = {}
    for doc in docs:
        src = doc.metadata.get("source", "unknown")
        grouped.setdefault(src, []).append(doc.page_content)

    parts: list[str] = []
    for src, passages in grouped.items():
        parts.append(f"=== SOURCE: {src} ===")
        parts.extend(passages)

    context = "\n\n".join(parts)
    log.info(
        "Retrieved %d chunks from %d source(s)  —  %d chars of context",
        len(docs), len(grouped), len(context),
    )
    return context
