from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from.. import models, schemas, auth
from..database import get_db

router = APIRouter(prefix="/expenses", tags=["Expenses"])

@router.post("", response_model=schemas.ExpenseOut, status_code=201)
def create_expense(
    expense: schemas.ExpenseCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(auth.get_current_user)
):
    new_exp = models.Expense(**expense.model_dump(), owner_id=current_user.id)
    db.add(new_exp)
    db.commit()
    db.refresh(new_exp)
    return new_exp

@router.get("", response_model=List[schemas.ExpenseOut])
def list_expenses(
    skip: int = 0, limit: int = 10,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(auth.get_current_user)
):
    return db.query(models.Expense).filter(models.Expense.owner_id == current_user.id).offset(skip).limit(limit).all()

@router.get("/{expense_id}", response_model=schemas.ExpenseOut)
def get_expense(
    expense_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(auth.get_current_user)
):
    exp = db.query(models.Expense).filter(models.Expense.id == expense_id, models.Expense.owner_id == current_user.id).first()
    if not exp:
        raise HTTPException(status_code=404, detail="Expense not found")
    return exp

@router.put("/{expense_id}", response_model=schemas.ExpenseOut)
def update_expense(
    expense_id: int,
    update: schemas.ExpenseUpdate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(auth.get_current_user)
):
    exp = db.query(models.Expense).filter(models.Expense.id == expense_id, models.Expense.owner_id == current_user.id).first()
    if not exp:
        raise HTTPException(status_code=404, detail="Expense not found")
    for key, value in update.model_dump(exclude_unset=True).items():
        setattr(exp, key, value)
    db.commit()
    db.refresh(exp)
    return exp

@router.delete("/{expense_id}", status_code=204)
def delete_expense(
    expense_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(auth.get_current_user)
):
    exp = db.query(models.Expense).filter(models.Expense.id == expense_id, models.Expense.owner_id == current_user.id).first()
    if not exp:
        raise HTTPException(status_code=404, detail="Expense not found")
    db.delete(exp)
    db.commit()
    return None