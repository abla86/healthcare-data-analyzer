# Healthcare Data Analyzer

A small Python portfolio project for validating and analyzing **synthetic healthcare-related CSV data**.

The included dataset is demonstration data only. It does not contain real patient records.

## Purpose

The project demonstrates practical Python data-processing skills: structured input validation, type-safe transformation, aggregation, filtering, reporting and unit testing.

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
├── data/                  # Synthetic demonstration data
├── src/                   # Analysis, models and reporting
├── tests/                 # Unit tests
├── main.py                # Application entry point
├── requirements.txt
├── README.md
└── .gitignore
```

## Run locally

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python main.py
```

## Testing

Run the automated test suite with:

```powershell
pytest
```

The current portfolio verification run completed with **9 passed tests**.

## Data safety

The repository uses synthetic demonstration records. No real patient information should be committed to this public repository. The application is an educational/data-engineering demonstration and is not a clinical decision-support system.

## Portfolio value

This project demonstrates Python, CSV processing, validation, data modelling, aggregation, filtering, reporting and automated testing in a healthcare-related but non-sensitive demonstration context.

## Status

**Portfolio / demonstration project.** The repository is the source of truth for the implementation and current project status.
