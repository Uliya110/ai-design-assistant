"""CLI точка входа для дипломного проекта.

Запуск:
    python -m src.cli.app demo
"""

import argparse
from src.core.demo import run_demo


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="ai-diploma", description="CLI дипломного проекта")
    sub = p.add_subparsers(dest="cmd", required=True)

    sub.add_parser("demo", help="Запустить демо-пайплайн (проверка структуры проекта)")
    return p


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if args.cmd == "demo":
        run_demo()


if __name__ == "__main__":
    main()
