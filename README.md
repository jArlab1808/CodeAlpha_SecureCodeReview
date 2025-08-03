# 🔐 Python Secure Coding Review

This project demonstrates a simple Flask web application that intentionally includes insecure coding practices. It is used to perform a secure code review using automated tools and manual inspection.

---

## 📁 Project Structure

```
secure-code-review/
├── app.py               # Flask app with vulnerabilities fixed
├── .env                 # Environment variables (not for upload)
├── requirements.txt     # Required Python packages
├── review-report.md     # Documented security findings and fixes
```

---

## 🚀 How to Run the Project

1. **Clone or extract the project folder.**
2. **Create a virtual environment:**

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

4. **Run the Flask application:**

```bash
python app.py
```

---

## 🔍 Perform Secure Code Analysis

### 1. Run Bandit

```bash
bandit -r app.py -f html -o bandit_report.html
start bandit_report.html
```

### 2. Manual Review Focus Areas
- Hardcoded secrets
- Unvalidated user inputs
- File handling
- Debug mode
- Credential management

---

## 🧪 Tools Used

- [Bandit](https://bandit.readthedocs.io/)
- Manual inspection

---

## 📝 Author

This secure coding review task is part of a cybersecurity learning module, demonstrating secure Python programming and vulnerability identification.
