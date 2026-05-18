from pathlib import Path


PROJECT_SECTIONS = [
    "0-DataIngestionParsing",
    "1-VectorEmbeddingsAndDatabases",
    "2-VectorStores",
]


def main() -> None:
    root = Path(__file__).resolve().parent
    missing = [section for section in PROJECT_SECTIONS if not (root / section).exists()]

    if missing:
        missing_list = ", ".join(missing)
        raise SystemExit(f"Missing project sections: {missing_list}")

    notebook_count = sum(
        1 for section in PROJECT_SECTIONS for _ in (root / section).rglob("*.ipynb")
    )
    data_count = sum(
        1
        for path in (root / "0-DataIngestionParsing" / "data").rglob("*")
        if path.is_file()
    )

    print("RAG learning workspace")
    print(f"Sections: {len(PROJECT_SECTIONS)}")
    print(f"Notebooks: {notebook_count}")
    print(f"Sample data files: {data_count}")


if __name__ == "__main__":
    main()
