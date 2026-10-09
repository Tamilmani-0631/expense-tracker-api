from fastapi import FastAPI
from.database import Base, engine
from.routers import auth, expenses

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Expense Tracker API",
    description="FastAPI CRUD with JWT - Expense tracker with 6 fields",
    version="1.0.0"
)

app.include_router(auth.router)
app.include_router(expenses.router)

@app.get("/")
def root():
    return {"msg": "Expense Tracker API running", "docs": "/docs"}