"""Хранилище для простых файлов (MVP).

В реальном дипломе можно заменить/добавить SQLite/PostgreSQL, кеш и т.п.
"""

from __future__ import annotations

from pathlib import Path


class LocalStore:
    def __init__(self, root: str = "data") -> None:
        self.root = Path(root)
        self.root.mkdir(parents=True, exist_ok=True)

    def save_text(self, name: str, text: str) -> Path:
        path = self.root / name
        path.write_text(text, encoding="utf-8")
        return path

    def load_text(self, name: str) -> str:
        path = self.root / name
        return path.read_text(encoding="utf-8")
