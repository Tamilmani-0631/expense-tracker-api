from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import date, datetime

# Auth
class UserCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    email: EmailStr
    password: str = Field(..., min_length=6)

class UserOut(BaseModel):
    id: int
    name: str
    email: str
    created_at: datetime
    class Config:
        from_attributes = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

# Expense - 6 fields
class ExpenseCreate(BaseModel):
    title: str = Field(..., min_length=2, max_length=100)
    amount: float = Field(..., gt=0)
    category: str = Field(..., min_length=2)
    description: Optional[str] = None
    expense_date: date = Field(default_factory=date.today)
    payment_method: str = Field(default="Cash")

class ExpenseUpdate(BaseModel):
    title: Optional[str] = None
    amount: Optional[float] = Field(None, gt=0)
    category: Optional[str] = None
    description: Optional[str] = None
    expense_date: Optional[date] = None
    payment_method: Optional[str] = None

class ExpenseOut(BaseModel):
    id: int
    title: str
    amount: float
    category: str
    description: Optional[str]
    expense_date: date
    payment_method: str
    owner_id: int
    created_at: datetime
    class Config:
        from_attributes = True