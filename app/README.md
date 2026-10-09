# Expense Tracker API - FastAPI + JWT

Concept: Users track personal expenses. Each expense has 6 fields: title, amount, category, description, expense_date, payment_method. Only owner can CRUD.

## Setup
```bash
cd hrms_fastapi
python -m venv.venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload