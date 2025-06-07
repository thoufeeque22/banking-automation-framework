# Banking Automation Framework

A robust, data-driven automation framework using **Selenium**, **Pytest**, and **GitHub Actions CI**, designed for functional testing of a banking web application (e.g., ParaBank).

---

## 🚀 Features

* **Pytest-based** test execution
* **Page Object Model (POM)** for maintainability
* **Data-driven testing** using CSV
* **Screenshot capture on failure** with timestamps
* **Structured logging** per test run
* **GitHub Actions CI** integration
* **HTML/Allure reports** ready
* **Custom directory structure** for real-world test automation

---

## 🧱 Project Structure

```
banking-automation-framework/
└── .github/workflows/       # GitHub Actions CI configs
├── config/                  # Test configurations
├── data/                    # CSV test data
├── lib/                     # Reusable libraries (optional)
├── pages/                   # Page classes (POM)
├── reports/                 # Logs, screenshots, and reports
│   └── screenshots/         # Screenshots by test name
├── scripts/                 # Shell scripts (optional)
├── tests/                   # Test cases (Pytest)
├── utils/                   # Utility functions and logging
├── conftest.py              # Fixtures and hooks
├── requirements.txt         # Python dependencies
├── pytest.ini               # Pytest configuration
```

> **Note:** Folders like `reports/`, `logs/`, `allure-results/`, and `reports/screenshots/` are created dynamically when tests run and are excluded from version control (via `.gitignore`).

---

## 🧪 Running Tests

### Locally

```bash
pip install -r requirements.txt
pytest --maxfail=1 --disable-warnings -v
```

### With Allure (Optional)

```bash
pytest --alluredir=reports/allure-results
allure serve reports/allure-results
```

---

## 🔄 GitHub Actions CI

Tests automatically run on:

* Push to `master`
* Pull requests to `master`

Workflow file: `.github/workflows/python-tests.yml`

---

## 📸 Screenshot on Failure

* Automatically saved in `reports/screenshots/<test_name>/`
* Filename: `<test_name>_<timestamp>.png`

---

## 📦 Dependencies

See `requirements.txt`. Install using:

```bash
pip install -r requirements.txt
```

---

## ✅ Future Improvements

* Add parallel test support (pytest-xdist)
* Integrate test coverage (pytest-cov)
* Add cross-browser support
* Publish Allure reports to GitHub Pages or as CI artifact

---

## 👨🏻‍💻 Author

**Thoufeeque Abdul Rahman Rafique**
📧 [thoufeeque.rafique@gmail.com](mailto:thoufeeque.rafique@gmail.com)
📱 +48 570 266 513
🌍 Kraków, Poland
