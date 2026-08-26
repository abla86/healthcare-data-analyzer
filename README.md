# Healthcare Data Analyzer

A small Python portfolio project for validating and analyzing **synthetic healthcare-related CSV data**.

The included dataset is demonstration data only. It does not contain real patient records.

## Features

- Reads CSV files
- Validates required fields
- Converts numeric and boolean values safely
- Calculates summary metrics
- Filters records by municipality and risk level
- Generates a text report
- Uses type hints and dataclasses
- Includes pytest unit tests
- Includes synthetic sample data

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

## Data safety

The repository uses synthetic identifiers (`Patient 001`, `Patient 002`, etc.) and generic municipality labels. No real patient information should be committed to this repository.

## Run

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it in PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

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

The program reports:

- total records
- average age
- high-risk records
- medication-support count
- municipality distribution
- high-risk record names/identifiers

## Portfolio

This repository is part of the ABLA86 engineering portfolio. The repository is the source of truth for its implementation, tests and current project status.
