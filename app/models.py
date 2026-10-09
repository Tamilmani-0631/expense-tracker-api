from sqlalchemy import Column, Integer, String, Float, Date, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from.database import Base
from datetime import datetime, date

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    expenses = relationship("Expense", back_populates="owner", cascade="all, delete")

class Expense(Base):
    __tablename__ = "expenses"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False) # e.g. "Office Lunch"
    amount = Column(Float, nullable=False) # e.g. 250.50
    category = Column(String, nullable=False) # e.g. "Food", "Travel"
    description = Column(Text, nullable=True)
    expense_date = Column(Date, default=date.today, nullable=False)
    payment_method = Column(String, default="Cash") # 5+ fields done
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    owner = relationship("User", back_populates="expenses")