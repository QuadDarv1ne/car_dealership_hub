# app/services/services/service_service.py

class ServiceService:
    def __init__(self, database):
        self.database = database  # Подключение к базе данных

    def get_all_services(self):
        """Получить список всех услуг."""
        return self.database.get_all("services")

    def get_service_by_id(self, service_id):
        """Получить услугу по ID."""
        return self.database.get_by_id("services", service_id)

    def create_service(self, service_data):
        """Создать новую услугу."""
        return self.database.create("services", service_data)

    def update_service(self, service_id, service_data):
        """Обновить информацию об услуге."""
        return self.database.update("services", service_id, service_data)

    def delete_service(self, service_id):
        """Удалить услугу по ID."""
        return self.database.delete("services", service_id)
