import os
import json
import logging
from fastapi import FastAPI, Request, HTTPException, Depends
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.core.config import settings
from app.core.translations import get_language, load_translations
from app.routes import appointments, auth, cars, services, users

# Настройка логгирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title=settings.PROJECT_NAME)
templates = Jinja2Templates(directory="app/templates")

# Укажите путь к папке со статическими файлами
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Подключение маршрутов
app.include_router(cars.router, prefix="/cars", tags=["cars"])
app.include_router(services.router, prefix="/services", tags=["services"])
app.include_router(appointments.router, prefix="/appointments", tags=["appointments"])
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(auth.router, tags=["auth"])

# Загрузка переводов
translations = load_translations()

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request, lang: str = Depends(get_language)):
    translation = translations.get(lang, translations.get("en"))
    return templates.TemplateResponse("index.html", {"request": request, "translation": translation})


@app.get("/set-lang")
async def set_language(request: Request, lang: str):
    response = templates.TemplateResponse("index.html", {
        "request": request,
        "translation": translations.get(lang, translations.get("en", {}))
    })
    response.set_cookie(key="lang", value=lang)
    return response


# Обработка ошибок
@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    logger.error(f"Error occurred: {exc.detail}")
    return templates.TemplateResponse("404.html", {"request": request}, status_code=exc.status_code)
