"""Small shared helpers used across diagnostics and session-state modules."""

from __future__ import annotations

from datetime import UTC, datetime
import os
from pathlib import Path
import re


def slugify_fragment(value: str) -> str:
    """Return a lowercase URL/file-safe fragment."""
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def utcnow_iso() -> str:
    """Return the current UTC timestamp in a compact ISO-8601 form."""
    return datetime.now(UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def secure_write_text(path: Path, content: str, mode: int = 0o600) -> None:
    """Atomically write *content* to *path* with restrictive permissions.

    Uses a temporary file in the same directory so ``os.replace`` is atomic
    on the same filesystem.  The file is created with *mode* (default
    owner-only read/write).
    """
    path.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
    fd = os.open(
        str(path.parent / f".{path.name}.tmp"),
        os.O_WRONLY | os.O_CREAT | os.O_TRUNC,
        mode,
    )
    try:
        with os.fdopen(fd, "w") as fh:
            fh.write(content)
        os.replace(str(path.parent / f".{path.name}.tmp"), str(path))
    except BaseException:
        try:
            os.unlink(str(path.parent / f".{path.name}.tmp"))
        except OSError:
            pass
        raise


def secure_mkdir(path: Path, mode: int = 0o700) -> Path:
    """Create a directory with restrictive permissions."""
    path.mkdir(parents=True, exist_ok=True, mode=mode)
    return path
