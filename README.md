# JSONPlaceholder_api_automation_framework

## 1. Project Title

`JSONPlaceholder_api_automation_framework` is a Python-based API automation framework built with `pytest` and `requests` for testing the public demo API at:

```text
https://jsonplaceholder.typicode.com
```

## 2. Project Overview

This framework demonstrates a clean and reusable approach to API testing. It separates test data, API clients, assertions, schemas, logging, and environment configuration so the project is easier to maintain as it grows.

The framework is designed for:

- Beginner-friendly learning
- Real-world API test automation practices
- Test execution from local machines and CI/CD pipelines
- HTML and Allure reporting

Generated reports and logs are ignored from Git so the repository stays clean. The only tracked file inside `reports/` should be `reports/.gitkeep`.

`.env` files should not be committed to Git because they may contain local or environment-specific settings.

## 3. Tech Stack

- Python 3.x
- `pytest`
- `requests`
- `jsonschema`
- `python-dotenv`
- `pytest-html`
- Allure Report
- GitHub Actions
- Python logging

## 4. Why This Framework Exists

This framework exists to show how API tests can be organized in a professional way instead of keeping everything in a single test file.

It helps you learn how to:

- Reuse API client methods
- Keep payloads and schemas separate from tests
- Validate API responses with assertions and JSON Schema
- Control environments using `.env`
- Produce readable test reports
- Run tests automatically in CI/CD

## 5. Folder Structure With Explanation

```text
company_api_automation_framework/
|-- .github/
|   `-- workflows/
|       `-- api-tests.yml
|
|-- clients/
|   |-- __init__.py
|   |-- base_client.py
|   `-- posts_client.py
|
|-- config/
|   |-- __init__.py
|   `-- config.py
|
|-- data/
|   |-- __init__.py
|   `-- posts_payloads.py
|
|-- schemas/
|   |-- __init__.py
|   `-- post_schema.py
|
|-- tests/
|   |-- __init__.py
|   `-- test_posts_api.py
|
|-- utils/
|   |-- __init__.py
|   |-- assertions.py
|   `-- logger.py
|
|-- reports/
|   `-- .gitkeep
|
|-- .gitignore
|-- conftest.py
|-- pytest.ini
|-- requirements.txt
`-- README.md
```

Short explanation of each folder:

- `clients/` contains reusable API client classes. Tests call these classes instead of calling `requests` directly.
- `config/` stores environment-based settings such as the base URL and timeout.
- `data/` stores reusable request payloads for test cases.
- `schemas/` stores JSON Schema definitions used for response validation.
- `tests/` contains the actual pytest test cases.
- `utils/` contains helper functions such as assertions and logging.
- `reports/` stores generated logs and reports locally. Only `.gitkeep` is tracked in Git.
- `.github/workflows/` contains the GitHub Actions workflow for CI/CD.

## 6. Prerequisites

Before running the project, make sure you have:

- Python 3.10 or newer
- Git installed
- Internet access to reach the demo API
- PowerShell on Windows
- Optional: Allure Commandline installed and available in `PATH` if you want to generate Allure reports locally

Also make sure your local `.env` file is not committed to the repository.

## 7. How to Clone the Repository

```bash
git clone <your-repository-url>
cd JSONPlaceholder_api_automation_framework
```

`git clone` downloads the repository. `cd` moves you into the project folder.

## 8. How to Create and Activate Virtual Environment on Windows

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

The first command creates an isolated Python environment. The second command activates it in PowerShell.

If PowerShell blocks activation, run this once in an elevated or current-user PowerShell session:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

## 9. How to Install Dependencies

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

The first command updates `pip`. The second command installs all project dependencies listed in `requirements.txt`.

## 10. How to Run All Tests

```powershell
pytest
```

This runs the full pytest suite using the defaults defined in `pytest.ini`.

If your local pytest discovery does not pick up the `tests/` folder automatically, use:

```powershell
pytest tests
```

## 11. How to Run Smoke Tests

```powershell
pytest -m smoke
```

This runs the quick, critical checks that verify the most important API behavior first.

## 12. How to Run Regression Tests

```powershell
pytest -m regression
```

This runs the broader test set that checks the main API flows more thoroughly.

## 13. How to Run API Tests

```powershell
pytest -m api
```

This runs only the tests marked as API tests.

## 14. How to Run a Single Test

```powershell
pytest tests/test_posts_api.py::test_get_single_post_successfully
```

This command runs one specific test case. It is useful when you want to debug a single failure quickly.

## 15. How to Generate pytest-html Report

```powershell
pytest --html=reports/pytest-report.html --self-contained-html
```

This creates a standalone HTML report inside `reports/`. The `--self-contained-html` option keeps the report portable because the CSS and assets are embedded in the file.

## 16. How to Generate Allure Report

First run the tests and write Allure results to a folder:

```powershell
pytest --alluredir=reports/allure-results
```

Then generate or open the report:

```powershell
allure serve reports/allure-results
```

`allure serve` starts a temporary local server and opens the report in your browser. If you want a static report folder instead, use:

```powershell
allure generate reports/allure-results -o reports/allure-report --clean
```

## 17. Where Logs Are Stored

Application and test logs are written to:

```text
reports/api_test.log
```

The logger is designed to keep runtime logs inside `reports/` so they stay separate from source code. Because `reports/` is ignored by Git, these files remain local unless you copy them elsewhere.

## 18. How Environment Config Works

Environment settings are loaded from `config/config.py` using `python-dotenv`.

The framework uses:

- `ENV` to choose the environment name
- `TIMEOUT` to control request timeout values
- `BASE_URLS` to map environment names to API base URLs

Example `.env` file:

```env
ENV=qa
TIMEOUT=10
```

If `ENV` is `qa`, the framework uses the QA base URL from the `BASE_URLS` mapping. You can change `ENV` to switch environments without editing your test code.

## 19. How Pytest Markers Work

Markers help you group and run tests by purpose.

The project defines these markers in `pytest.ini`:

- `smoke` for quick critical checks
- `regression` for broader regression coverage
- `api` for API automation tests
- `negative` for negative test scenarios

Example usage:

```powershell
pytest -m smoke
pytest -m regression
pytest -m negative
```

`pytest.ini` also enables:

- `-v` for verbose output
- `--tb=short` for shorter traceback output

## 20. How GitHub Actions CI/CD Works

The CI/CD workflow should live in:

```text
.github/workflows/api-tests.yml
```

In a typical setup, GitHub Actions will:

1. Trigger on push and pull request events
2. Set up the Python runtime
3. Install project dependencies
4. Run the pytest suite or selected markers
5. Upload logs and reports as workflow artifacts

This gives you automated feedback without running tests manually on every change.

## 21. How to View or Download CI/CD Artifacts

In GitHub, open the repository and go to:

```text
Actions -> select a workflow run -> Artifacts
```

From there you can view or download items such as:

- HTML reports
- Allure result files
- Logs

Artifact names depend on what your workflow uploads.

## 22. Beginner Debugging Guide

If a test fails, follow this order:

1. Check whether the virtual environment is active.
2. Confirm dependencies are installed with `pip list`.
3. Verify `.env` exists and has the correct values.
4. Run one test with extra output:

```powershell
pytest tests/test_posts_api.py::test_get_single_post_successfully -vv -s
```

5. Review the log file in `reports/api_test.log`.
6. Open the HTML or Allure report if you generated one.

The `-s` flag shows printed output immediately, and `-vv` makes pytest output more detailed.

## 23. Best Practices Followed in This Framework

- Reusable API clients keep HTTP logic out of test cases.
- Test data is stored separately from the tests.
- Schema validation adds structure checks beyond simple status code assertions.
- Fixtures reduce duplication and make tests easier to read.
- Logging improves debugging and traceability.
- Pytest markers make test selection simple.
- Environment-based configuration avoids hardcoding URLs and timeouts.
- CI/CD makes the framework usable in a team workflow.

## 24. Common Issues and Fixes on Windows

- If `.venv\Scripts\Activate.ps1` fails, run `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`.
- If `allure` is not recognized, install Allure Commandline and add it to `PATH`.
- If pytest does not find tests, run `pytest tests` and confirm the `tests/` folder exists.
- If `.env` values are not being read, confirm the file is named exactly `.env` and not `.env.txt`.
- If requests time out, check your internet connection and the demo API URL.
- If reports do not appear, confirm the `reports/` folder exists and the test run had permission to write there.

## 25. Future Improvements / Practice Tasks

This framework can be extended with:

- More API endpoints such as comments, users, and albums
- Negative and boundary test coverage
- Data-driven tests with multiple payload sets
- Schema validation for more response types
- Request and response logging improvements
- Docker support for repeatable local execution
- Parallel execution with `pytest-xdist`
- Better CI/CD artifact retention and reporting
- Integration with code quality tools such as `ruff` and `black`

## Notes

- Keep `reports/` out of Git except for `reports/.gitkeep`.
- Keep `.env` out of Git.
- If you change the base URL or timeout, update your local environment variables instead of hardcoding values in tests.
