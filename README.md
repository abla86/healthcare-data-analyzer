# Healthcare Data Analyzer

A small Python portfolio project for validating and analyzing healthcare-related CSV data.

## Features

- Reads CSV files
- Validates required fields
- Converts numeric and boolean values safely
- Calculates summary metrics
- Filters records by municipality and risk level
- Generates a text report
- Uses type hints and dataclasses
- Includes pytest unit tests
- Includes sample data

## Project structure

```text
healthcare-data-analyzer/
├── data/
│   └── patients.csv
├── src/
│   ├── __init__.py
│   ├── analyzer.py
│   ├── models.py
│   └── report.py
├── tests/
│   └── test_analyzer.py
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Run

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it in PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install test dependency:

```bash
pip install -r requirements.txt
```

Run the analyzer:

```bash
python main.py
```

Run tests:

```bash
pytest
```

## Example output

The program prints:

- total records
- average age
- high-risk patients
- medication support count
- municipality distribution
- high-risk patient names
