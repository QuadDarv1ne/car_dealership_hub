import json
import logging
from fastapi import Request
from pathlib import Path

# Настройка логирования
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

def load_translations(lang: str = "en"):
    translations_path = Path(f"app/translations/{lang}.json")
    
    # Попытка загрузить запрашиваемый язык
    try:
        with translations_path.open("r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        logger.error(f"Translation file for '{lang}' not found. Loading default (en).")
    except json.JSONDecodeError as e:
        logger.error(f"Error decoding JSON for '{lang}': {e}. Loading default (en).")
    
    # Если запрашиваемый язык не найден или произошла ошибка, загружаем язык по умолчанию
    with Path("app/translations/en.json").open("r", encoding="utf-8") as file:
        return json.load(file)

def get_language(request: Request):
    return request.cookies.get("lang", "en")
