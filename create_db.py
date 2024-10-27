from sqlalchemy import create_engine
from app.db.database import Base
from app.db.models import Car, Service  # Импортируем модели
import os

# Путь к базе данных
db_path = "./instance/car_dealership.db"

# Убедитесь, что директория существует
db_directory = os.path.dirname(db_path)
os.makedirs(db_directory, exist_ok=True)

# Создание движка
engine = create_engine(f"sqlite:///{db_path}", connect_args={"check_same_thread": False})

# Создание таблиц в базе данных
def create_tables():
    Base.metadata.create_all(bind=engine)
    print("Таблицы успешно созданы.")

if __name__ == "__main__":
    create_tables()
