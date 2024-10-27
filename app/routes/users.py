from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from app.db import models, schemas
from app.db.database import get_db
from app.core.translations import load_translations, get_language
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter()

@router.get("/", response_model=list[schemas.User])
def get_users(request: Request, db: Session = Depends(get_db)) -> dict:
    lang = get_language(request)  # Получаем язык из запроса
    translation = load_translations(lang)  # Получаем переводы
    users = db.query(models.User).all()
    logger.info("Fetched users for language: %s", lang)
    return {"users": users, "translation": translation}

@router.post("/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)) -> schemas.User:
    try:
        db_user = models.User(**user.dict())
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        logger.info("Created user: %s", db_user)
        return db_user
    except Exception as e:
        logger.error("Failed to create user: %s", e)
        raise HTTPException(status_code=500, detail="Failed to create user")

@router.get("/{user_id}", response_model=schemas.User)
def get_user(user_id: int, db: Session = Depends(get_db)) -> schemas.User:
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        logger.warning("User not found: %d", user_id)
        raise HTTPException(status_code=404, detail="User not found")
    logger.info("Fetched user: %s", user)
    return user

@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)) -> dict:
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        logger.warning("User not found for deletion: %d", user_id)
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()
    logger.info("Deleted user: %d", user_id)
    return {"message": "User deleted successfully"}
