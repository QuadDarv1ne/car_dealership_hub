from fastapi import APIRouter, Depends, HTTPException, Request, Response
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from app.db import models, schemas
from app.db.database import get_db
from app.core.translations import load_translations, get_language

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/")
async def get_cars(request: Request, db: Session = Depends(get_db)):
    cars = db.query(models.Car).all()
    lang = request.cookies.get("lang", "en")
    translations = load_translations()
    translation = translations.get(lang, translations["en"])
    return templates.TemplateResponse("cars.html", {"request": request, "cars": cars, "translation": translation})

@router.get("/set-lang")
def set_language(response: Response, lang: str = "en"):
    response.set_cookie(key="lang", value=lang)
    return {"message": f"Language set to {lang}"}

@router.post("/")
def create_car(car: schemas.CarCreate, db: Session = Depends(get_db)):
    db_car = models.Car(**car.dict())
    db.add(db_car)
    db.commit()
    db.refresh(db_car)
    return db_car

@router.get("/{car_id}")
def get_car(car_id: int, db: Session = Depends(get_db)):
    car = db.query(models.Car).filter(models.Car.id == car_id).first()
    if not car:
        raise HTTPException(status_code=404, detail="Car not found")
    return car

@router.delete("/{car_id}")
def delete_car(car_id: int, db: Session = Depends(get_db)):
    car = db.query(models.Car).filter(models.Car.id == car_id).first()
    if not car:
        raise HTTPException(status_code=404, detail="Car not found")
    db.delete(car)
    db.commit()
    return {"message": "Car deleted successfully"}
