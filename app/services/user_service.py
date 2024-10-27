# app/services/services/user_service.py

class UserService:
    def __init__(self, database):
        self.database = database  # Подключение к базе данных

    def get_all_users(self):
        """Получить список всех пользователей."""
        return self.database.get_all("users")

    def get_user_by_id(self, user_id):
        """Получить пользователя по ID."""
        return self.database.get_by_id("users", user_id)

    def create_user(self, user_data):
        """Создать нового пользователя."""
        return self.database.create("users", user_data)

    def update_user(self, user_id, user_data):
        """Обновить информацию о пользователе."""
        return self.database.update("users", user_id, user_data)

    def delete_user(self, user_id):
        """Удалить пользователя по ID."""
        return self.database.delete("users", user_id)

    def get_user_by_email(self, email):
        """Получить пользователя по email."""
        return self.database.get_by_field("users", "email", email)
