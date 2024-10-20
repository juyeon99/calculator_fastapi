from database import Base
from sqlalchemy import Column, Integer, String, Float

class Calculation(Base):
    __tablename__ = 'calculations'
    
    id = Column(Integer, primary_key=True)
    num1 = Column(Float)
    num2 = Column(Float)
    operator = Column(String(2))
    result = Column(Float)
