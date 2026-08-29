# Healthcare Data Analyzer

A small Python portfolio project for validating and analyzing **synthetic healthcare-related CSV data**.

The included dataset is demonstration data only. It does not contain real patient records.

## Purpose

The project demonstrates practical Python data-processing skills: structured input validation, explicit data-quality assessment, type-safe transformation, aggregation, filtering, reporting and unit testing.

## Data-quality pipeline

Before analysis, the input dataset passes through a separate quality gate:

```text
CSV input
   ↓
Schema check
   ↓
Completeness / uniqueness / value validation
   ↓
PASS | PASS WITH WARNINGS | FAIL
   ↓
Analysis
   ↓
Report
```

A dataset that fails the quality gate is not analyzed. This prevents invalid input from silently producing a report.

## Features

- Reads CSV files
- Validates required fields
- Assesses schema conformity and completeness
- Detects duplicate patient identifiers
- Validates numeric, boolean and risk-domain values
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
├── src/                   # Quality, analysis, models and reporting
├── tests/                 # Unit tests
├── main.py                # Quality-gated application entry point
├── requirements.txt
├── PORTFOLIO-WORKLOG.md
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

The tests cover both the existing analysis behaviour and the data-quality gate, including duplicate identifiers and invalid values.

## Data safety

The repository uses synthetic demonstration records. No real patient information should be committed to this public repository. The application is an educational/data-engineering demonstration and is not a clinical decision-support system.

## Portfolio value

This project demonstrates Python, CSV processing, data-quality engineering, validation, data modelling, aggregation, filtering, reporting and automated testing in a healthcare-related but non-sensitive demonstration context.

## Status

**Portfolio / demonstration project.** The repository is the source of truth for the implementation and current project status.

## Change-control audit

See [docs/REPOSITORY-CHANGE-AUDIT-2026-08-28.md](docs/REPOSITORY-CHANGE-AUDIT-2026-08-28.md) for the repository change-control and traceability record.


## Quality and verification

Documentation is intended to describe the implementation that is actually present. Automated tests, dependency/security controls and repository checks should be used where appropriate. Prototype, demonstration and production status are kept distinct; claims are not made beyond what the code and available evidence support.
