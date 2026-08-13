from pathlib import Path

from src.analyzer import load_records
from src.report import build_report


def main() -> None:
    data_file = Path(__file__).parent / "data" / "patients.csv"
    records = load_records(data_file)
    print(build_report(records))


if __name__ == "__main__":
    main()
