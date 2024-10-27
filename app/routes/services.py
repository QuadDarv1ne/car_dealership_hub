from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from app.db import models, schemas
from app.db.database import SessionLocal, get_db
from app.core.translations import load_translations, get_language
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/services")
def list_services(request: Request, db: Session = Depends(get_db)) -> templates.TemplateResponse:
    lang = get_language(request)
    translation = load_translations(lang)
    services = db.query(models.Service).all()
    logger.info("Fetched services for language: %s", lang)
    return templates.TemplateResponse("services.html", {"request": request, "services": services, "translation": translation})

@router.get("/")
def get_services(db: Session = Depends(get_db)) -> list[schemas.Service]:
    services = db.query(models.Service).all()
    logger.info("Fetched all services")
    return services

@router.post("/")
def create_service(service: schemas.ServiceCreate, db: Session = Depends(get_db)) -> schemas.Service:
    try:
        db_service = models.Service(**service.dict())
        db.add(db_service)
        db.commit()
        db.refresh(db_service)
        logger.info("Created service: %s", db_service)
        return db_service
    except Exception as e:
        logger.error("Failed to create service: %s", e)
        raise HTTPException(status_code=500, detail="Failed to create service")

@router.get("/{service_id}")
def get_service(service_id: int, db: Session = Depends(get_db)) -> schemas.Service:
    service = db.query(models.Service).filter(models.Service.id == service_id).first()
    if not service:
        logger.warning("Service not found: %d", service_id)
        raise HTTPException(status_code=404, detail="Service not found")
    logger.info("Fetched service: %s", service)
    return service

@router.delete("/{service_id}")
def delete_service(service_id: int, db: Session = Depends(get_db)) -> dict:
    service = db.query(models.Service).filter(models.Service.id == service_id).first()
    if not service:
        logger.warning("Service not found for deletion: %d", service_id)
        raise HTTPException(status_code=404, detail="Service not found")
    db.delete(service)
    db.commit()
    logger.info("Deleted service: %d", service_id)
    return {"message": "Service deleted successfully"}
