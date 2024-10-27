from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.db.models import Car, Service

def add_test_data():
    db = SessionLocal()

    # Добавляем 10 записей в таблицу Car
    cars = [
        Car(name="Toyota Camry", description="Надежный и комфортный седан", price=30000, image_url="toyota_camry.jpg"),
        Car(name="Honda Civic", description="Экономичный и стильный", price=20000, image_url="honda_civic.jpg"),
        Car(name="BMW X5", description="Роскошный внедорожник с мощным двигателем", price=60000, image_url="bmw_x5.jpg"),
        Car(name="Mercedes-Benz C-Class", description="Комфортный седан премиум-класса", price=50000, image_url="mercedes_c_class.jpg"),
        Car(name="Audi A6", description="Спортивный и стильный", price=45000, image_url="audi_a6.jpg"),
        Car(name="Ford Mustang", description="Классический спортивный автомобиль", price=35000, image_url="ford_mustang.jpg"),
        Car(name="Chevrolet Tahoe", description="Просторный внедорожник для всей семьи", price=55000, image_url="chevrolet_tahoe.jpg"),
        Car(name="Nissan Altima", description="Надежный и экономичный седан", price=25000, image_url="nissan_altima.jpg"),
        Car(name="Volkswagen Passat", description="Комфортный автомобиль для городских поездок", price=27000, image_url="volkswagen_passat.jpg"),
        Car(name="Subaru Outback", description="Полный привод для любых условий", price=33000, image_url="subaru_outback.jpg"),
    ]
    db.add_all(cars)

    # Добавляем 10 записей в таблицу Service
    services = [
        Service(name="Замена масла", description="Полная замена масла и фильтров", price=100),
        Service(name="Техническое обслуживание", description="Полный осмотр автомобиля", price=200),
        Service(name="Диагностика двигателя", description="Компьютерная диагностика двигателя", price=150),
        Service(name="Балансировка колес", description="Балансировка всех четырех колес", price=80),
        Service(name="Замена тормозных колодок", description="Замена передних и задних тормозных колодок", price=120),
        Service(name="Регулировка развала-схождения", description="Точная настройка колес", price=90),
        Service(name="Чистка кондиционера", description="Профессиональная чистка системы кондиционирования", price=70),
        Service(name="Покраска кузова", description="Полная покраска кузова автомобиля", price=500),
        Service(name="Полировка кузова", description="Полная полировка кузова для блеска", price=200),
        Service(name="Шумоизоляция салона", description="Дополнительная шумоизоляция для комфорта", price=600),
    ]
    db.add_all(services)

    db.commit()
    db.close()
    print("Тестовые данные успешно добавлены.")

if __name__ == "__main__":
    add_test_data()
