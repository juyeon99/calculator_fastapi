from fastapi import FastAPI, Request, Depends, Form, status
from fastapi.templating import Jinja2Templates
import models, schemas, calculator_crud
from database import engine, session_local
from sqlalchemy.orm import Session
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles

templates = Jinja2Templates(directory="template")
app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.mount("/static", StaticFiles(directory="template/static"), name="static")

def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def home(request: Request, db: Session=Depends(get_db)):
    return templates.TemplateResponse("index.html", {"request":request})

@app.post("/calculations", response_model=schemas.CalculationResponse)
async def create_calculation(
    calculation: schemas.CalculationCreate,
    db: Session=Depends(get_db)
):
    response = calculator_crud.create_calculation(db, calculation)
    return response

@app.get("/calculations/{calculation_id}", response_model=schemas.CalculationResponse)
async def find_calculation_by_id(calculation_id: int, db: Session=Depends(get_db)):
    db_calculation = calculator_crud.get_calculation_by_id(db, calculation_id)
    return db_calculation

@app.get("/calculations", response_model=list[schemas.CalculationResponse])
async def find_all_calculations(db: Session=Depends(get_db)):
    all_calculations = calculator_crud.get_all_calculations(db)
    return all_calculations

@app.delete("/calculations/{calculation_id}", status_code=204)
async def delete_calculation(calculation_id: int, db: Session=Depends(get_db)):
    calculator_crud.delete_calculation(db, calculation_id)
    return None