from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from app.db.database import SessionLocal, Base, engine
from app.db.models import Car
from app.core.translations import load_translation
from app.main import templates

Base.metadata.create_all(bind=engine)
router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
async def get_cars(request: Request, db: Session = Depends(get_db)):
    cars = db.query(Car).all()
    language = request.cookies.get("lang", "en")
    translation = load_translation(language)
    return templates.TemplateResponse("cars.html", {"request": request, "cars": cars, "translation": translation})
