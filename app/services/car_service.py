# app/services/services/car_service.py

class CarService:
    def __init__(self, database):
        self.database = database  # Подключение к базе данных

    def get_all_cars(self):
        """Получить список всех автомобилей."""
        return self.database.get_all("cars")

    def get_car_by_id(self, car_id):
        """Получить автомобиль по ID."""
        return self.database.get_by_id("cars", car_id)

    def create_car(self, car_data):
        """Создать новый автомобиль."""
        return self.database.create("cars", car_data)

    def update_car(self, car_id, car_data):
        """Обновить информацию об автомобиле."""
        return self.database.update("cars", car_id, car_data)

    def delete_car(self, car_id):
        """Удалить автомобиль по ID."""
        return self.database.delete("cars", car_id)
