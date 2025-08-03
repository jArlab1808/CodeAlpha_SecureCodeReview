# 🛡 Python Secure Code Review Report

## 🔍 Findings Summary

| ID | Issue | Line | Severity | Fix |
|----|-------|------|----------|-----|
| 1 | Hardcoded Flask secret key | 5 | LOW | Move to `.env` and load securely |
| 2 | Hardcoded credentials | 11 | LOW | Use hashed credentials & Flask-Login |
| 3 | Flask debug mode enabled | 22 | HIGH | Set `debug=False` for production |

---

## ✅ Remediation Steps

- Install `python-dotenv` and use it for environment configs.
- Never hardcode credentials; use encrypted or hashed passwords with secure authentication.
- Avoid running Flask in debug mode in production.

---

## 🧪 Tools Used

- Bandit
