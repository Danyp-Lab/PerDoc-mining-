"""
PDF to JSON metadata extraction tool.
Modernized to support modern pypdf, pathlib, and typing conventions.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any
import pypdf


def extract_pdf_metadata(pdf_path: Path | str) -> dict[str, Any]:
    """Read metadata from a PDF file using modern pypdf."""
    path = Path(pdf_path)
    if not path.is_file():
        raise FileNotFoundError(f"PDF file not found: {path}")

    reader = pypdf.PdfReader(path)
    metadata = reader.metadata or {}

    doc_info: dict[str, Any] = {}
    for key, value in metadata.items():
        clean_key = str(key).lstrip("/").lower()
        doc_info[clean_key] = str(value) if value is not None else ""

    return {
        "filename": path.name,
        "page_count": len(reader.pages),
        "metadata": doc_info,
    }


def save_metadata_to_json(data: dict[str, Any], output_path: Path | str) -> Path:
    """Save extracted metadata dictionary as formatted JSON."""
    out = Path(output_path)
    with out.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    return out


def main() -> None:
    filename_input = input("Enter path to PDF file (e.g. sample.pdf): ").strip()
    if not filename_input:
        print("No file specified.")
        return

    path = Path(filename_input)
    if not path.suffix:
        path = path.with_suffix(".pdf")

    try:
        extracted = extract_pdf_metadata(path)
        out_json = path.with_suffix(".json")
        save_metadata_to_json(extracted, out_json)
        print(f"✅ Metadata saved to: {out_json}")
    except Exception as exc:
        print(f"❌ Error extracting metadata: {exc}")


if __name__ == "__main__":
    main()