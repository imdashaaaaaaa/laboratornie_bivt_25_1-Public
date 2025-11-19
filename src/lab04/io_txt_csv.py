from pathlib import Path


def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError

    return p.read_text(encoding=encoding)


import csv
from pathlib import Path
from typing import Iterable, Sequence


def write_csv(
    rows: Iterable[Sequence], path: str | Path, header: tuple[str, ...] | None = None
) -> None:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    rows = list(rows)

    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)

        if header is not None:
            w.writerow(header)
        if rows:
            for r in rows:
                if len(r) != len(rows[0]):
                    raise ValueError

        for r in rows:
            w.writerow(r)
