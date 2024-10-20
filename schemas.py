from pydantic import BaseModel
from typing_extensions import Optional

class CalculationBase(BaseModel):
    num1: float
    num2: Optional[float] = None
    operator: str
    result: Optional[float] = None

class CalculationCreate(CalculationBase):
    pass

class CalculationResponse(CalculationBase):
    id: int