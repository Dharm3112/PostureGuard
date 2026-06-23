# Contributing to PostureGuard

Thank you for your interest in contributing to **PostureGuard**! To maintain code quality, formatting consistency, and project structure, please follow these guidelines.

## 🚀 Setting Up Local Development

1. **Fork and Clone** the repository.
2. **Create a virtual environment** and install dependencies:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Or activate script for Windows
   pip install -r requirements.txt
   pip install black isort mypy
   ```

## 🎨 Code Style and Standards

To ensure clean and maintainable code, we enforce the following:

- **Type Hints:** All new functions and classes must include type annotations (using standard types or types from `typing` module).
- **Docstrings:** Use PEP-257 docstrings to document class goals, parameters, return types, and exceptions.
- **Formatting:** Use **Black** for code formatting and **isort** for import sorting.
  * Run Black: `black .`
  * Run isort: `isort .`
- **Linting:** Use **flake8** for syntax checking and PEP-8 code style verification:
  * Run Flake8: `flake8 .`
- **Typing Checks:** Run **mypy** to verify type annotation correctness:
  * `mypy .`

## 🧪 Testing Guidelines

We use Python's built-in `unittest` framework. All new logic, config loaders, and helper metrics must be covered by tests.

- Place tests in the `tests/` directory with filenames starting with `test_`.
- Run the full test suite before committing:
  ```bash
  python -m unittest discover -s tests
  ```
- Make sure to review code coverage metrics regularly to ensure critical boundaries remain verified.

## 📐 Code Quality Metrics
- Keep functions length under 100 lines.
- Ensure all parameters have type hints.
- Every module must describe its design target in module header.

## 📝 Commit Message Guidelines

Keep commit messages concise, imperative, and structured:
- Start with a clear action verb (e.g., `Add`, `Fix`, `Refactor`, `Docs`).
- Keep the title line under 72 characters.
- If necessary, add a blank line followed by a detailed paragraph explanation.

## 📬 Pull Request Process

1. Create a descriptive feature branch: `git checkout -b feature/your-awesome-feature`.
2. Implement changes, adding appropriate unit tests.
3. Run tests and verify code formatting/types locally.
4. Submit your PR and ensure the GitHub Actions CI pipeline passes successfully.
