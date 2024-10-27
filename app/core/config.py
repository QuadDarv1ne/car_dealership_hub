from pydantic_settings import BaseSettings
import os

class Settings(BaseSettings):
    PROJECT_NAME: str = "Car Dealership Hub"
    DATABASE_URL: str = f"sqlite:///{os.path.join(os.getcwd(), 'instance', 'car_dealership.db')}"
    LANGUAGE: str = "en"  # Значение по умолчанию
    SECRET_KEY: str = "137"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

settings = Settings()
