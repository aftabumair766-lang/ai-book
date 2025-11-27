# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

# CLAUDE.md - Codebase Overview

This repository appears to be a new or empty Python project. It contains a `venv` directory, indicating a Python virtual environment.

## High-Level Architecture and Structure

As no specific project files or structure were found, this `CLAUDE.md` assumes a standard Python application. Future development would likely involve:
*   Python source files (e.g., `main.py`, `app.py`)
*   A `requirements.txt` or `pyproject.toml` for dependency management
*   Potential subdirectories for modules or features

## Common Build, Lint, and Test Commands

These commands are suggested for a typical Python development workflow. Actual commands may vary based on specific project setup.

*   **Dependency Installation**:
    *   `pip install -r requirements.txt` (if `requirements.txt` is present)
    *   `uv install` (if `uv` is used for dependency management)
*   **Run Application**:
    *   `python main.py` or `uv run main.py` (assuming `main.py` is the entry point)
*   **Linting/Formatting**:
    *   `black .` (if `black` is used for code formatting)
    *   `ruff .` or `flake8 .` (for linting)
*   **Testing**:
    *   `pytest` (if `pytest` is used for testing)
