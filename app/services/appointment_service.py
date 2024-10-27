# app/services/services/appointment_service.py

class AppointmentService:
    def __init__(self, database):
        self.database = database  # Подключение к базе данных

    def get_all_appointments(self):
        """Получить все записи на прием."""
        return self.database.get_all("appointments")

    def get_appointment_by_id(self, appointment_id):
        """Получить запись на прием по ID."""
        return self.database.get_by_id("appointments", appointment_id)

    def create_appointment(self, appointment_data):
        """Создать новую запись на прием."""
        return self.database.create("appointments", appointment_data)

    def update_appointment(self, appointment_id, appointment_data):
        """Обновить запись на прием."""
        return self.database.update("appointments", appointment_id, appointment_data)

    def delete_appointment(self, appointment_id):
        """Удалить запись на прием по ID."""
        return self.database.delete("appointments", appointment_id)
