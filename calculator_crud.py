from sqlalchemy.orm import Session
import schemas, models
import math
from fastapi import HTTPException

def calculate(num1: float, num2: float, operator: str):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            raise ValueError("DBZ 에러")
        return num1 / num2
    elif operator == '%':
        return num1 % num2
    elif operator == '√':
        return math.sqrt(num1)
    else:
        raise ValueError("허용되지 않은 operator입니다.")

def create_calculation(db: Session, calculation: schemas.CalculationCreate):
    calc_result = calculate(calculation.num1, calculation.num2, calculation.operator)

    db_calculation = models.Calculation(
        num1 = calculation.num1,
        num2 = calculation.num2,
        operator = calculation.operator,
        result = calc_result
    )
    
    db.add(db_calculation)
    db.commit()
    
    return db_calculation

def get_calculation_by_id(db: Session, calculation_id: int):
    found_calculation = db.query(models.Calculation).filter(models.Calculation.id == calculation_id).first()
    return found_calculation

def get_all_calculations(db: Session):
    all_calculations = db.query(models.Calculation).all()
    return all_calculations

def delete_calculation(db: Session, calculation_id: int):
    found_calculation = db.query(models.Calculation).filter(models.Calculation.id == calculation_id).first()
    
    if found_calculation is None:
        raise HTTPException(status_code=404, detail="Calculation Not Found")
    
    db.delete(found_calculation)
    db.commit()