import logging
from pathlib import Path

log = logging.getLogger(__name__)


def load_docs_from_path(docs_path: str) -> list[str]:
    path = Path(docs_path)
    if not path.exists():
        raise FileNotFoundError(f"Path not found: {docs_path}")

    log.info("Scanning  %s  for .txt files...", docs_path)
    docs: list[str] = []

    for f in sorted(path.glob("**/*.txt")):
        content = f.read_text(encoding="utf-8")
        docs.append(f"=== FILE: {f.name} ===\n{content}\n")
        log.info("  %-52s  %6d chars", f.name, len(content))

    if not docs:
        raise ValueError(f"No .txt files found in {docs_path}")

    total_chars = sum(len(d) for d in docs)
    log.info("Loaded %d document(s)  —  %d total chars", len(docs), total_chars)
    return docs
