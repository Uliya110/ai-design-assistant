"""Мини-демо, чтобы студент сразу увидел 'проект запускается'."""

from __future__ import annotations

from dataclasses import dataclass
from typing import List

from src.storage.local_store import LocalStore


@dataclass
class DemoResult:
    items: List[str]


def run_demo() -> None:
    store = LocalStore()
    store.save_text("demo_note.txt", "Hello! Это демо-файл дипломного проекта.")
    text = store.load_text("demo_note.txt")

    result = DemoResult(items=[text, "Следующий шаг: добавить свою бизнес-логику в src/core/"])
    print("✅ DEMO OK")
    for i, item in enumerate(result.items, 1):
        print(f"{i}. {item}")
