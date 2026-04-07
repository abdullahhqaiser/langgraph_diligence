"""
Logging configuration for the DD engine.

All output goes to stdout so it interleaves naturally with the
coloured print statements in main.py.
"""

import logging
import sys

# ─── ANSI codes (duplicated here so this module is self-contained) ────────────
_RESET  = "\033[0m"
_BOLD   = "\033[1m"
_DIM    = "\033[2m"

_COLOURS = {
    logging.DEBUG:    "\033[36m",   # cyan
    logging.INFO:     "\033[32m",   # green
    logging.WARNING:  "\033[33m",   # yellow
    logging.ERROR:    "\033[31m",   # red
    logging.CRITICAL: "\033[35m",   # magenta
}


class _ColourFormatter(logging.Formatter):
    """Compact, coloured log formatter: HH:MM:SS  LEVEL  logger.name  message"""

    def format(self, record: logging.LogRecord) -> str:
        colour  = _COLOURS.get(record.levelno, "")
        ts      = self.formatTime(record, "%H:%M:%S")
        level   = f"{colour}{_BOLD}{record.levelname:<8}{_RESET}"
        name    = f"{_DIM}{record.name:<20}{_RESET}"
        return f"{_DIM}{ts}{_RESET}  {level}  {name}  {record.getMessage()}"


def setup_logging(level: int = logging.INFO) -> None:
    """Call once at startup — configures root logger & silences noisy libs."""
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(_ColourFormatter())

    root = logging.getLogger()
    root.setLevel(level)
    root.handlers.clear()
    root.addHandler(handler)

    # Silence noisy third-party loggers
    for lib in ("httpx", "httpcore", "urllib3", "langchain", "langgraph",
                "openai", "anthropic", "langsmith"):
        logging.getLogger(lib).setLevel(logging.WARNING)
