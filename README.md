# Разработка сайта автомобильного магазина (концерна) + управление мастерской

![car_delership](car_delership.png)

🚗 **Car Dealership Hub** — это современная веб-платформа для автомобильных магазинов и мастерских.

Проект сочетает в себе удобство управления каталогом автомобилей, функций онлайн-продаж и сервисного обслуживания клиентов.

## Структура проекта
```
car_dealership_hub/
├── app/
│   ├── __init__.py           # Инициализация FastAPI приложения
│   ├── main.py               # Запуск приложения
│   ├── core/
│   │   ├── translations.py   # Конфигурация перевода текста [en/ru]
│   │   ├── config.py         # Конфигурации приложения
│   │   └── security.py       # Функции безопасности (например, для аутентификации)
│   │
│   ├── db/
│   │   ├── database.py       # Подключение к базе данных
│   │   ├── models.py         # Модели данных для автомобилей, услуг и пользователей
│   │   └── schemas.py        # Схемы Pydantic для валидации входящих данных
│   │
│   ├── routes/               # API маршруты
│   │   ├── __init__.py       # Инициализация маршрутов
│   │   ├── cars.py           # Маршруты для автомобилей
│   │   ├── services.py       # Маршруты для услуг
│   │   ├── appointments.py   # Маршруты для записей в мастерскую
│   │   ├── users.py          # Маршруты для пользователей
│   │   └── auth.py           # Маршруты для аутентификации
│   │
│   ├── services/                   # Логика бизнес-процессов
│   │   ├── car_service.py          # Сервис для работы с автомобилями
│   │   ├── appointment_service.py  # Сервис для работы с записями
│   │   ├── service_service.py      # Сервис для работы с услугами
│   │   └── user_service.py         # Сервис для работы с пользователями
│   │
│   ├── templates/             # HTML шаблоны
│   │   ├── base.html          # Основной шаблон
│   │   ├── index.html         # Главная страница
│   │   ├── cars.html          # Страница с автомобилями
│   │   ├── services.html      # Страница с услугами
│   │   ├── appointments.html  # Страница с записями
│   │   ├── contact.html       # Страница контактов
│   │   └── car_detail.html    # Страница с подробной информацией об автомобиле
│   │
│   ├── static/             # Статические файлы (CSS, JS, изображения)
│   │   ├── css/            # Файлы стилей
│   │   ├── js/             # Файлы скриптов
│   │   └── images/         # Изображения автомобилей и услуг
│   │
│   ├── translations/       # Папка с переводами текста [en/ru]
│   │   ├── en.json         # Перевод текста на английский язык
│   │   └── ru.json         # Перевод текста на русский язык
│   │
│   └── analytics/          # Аналитика посещаемости и действий
│
├── tests/                  # Тесты для приложения
│   ├── test_routes.py      # Тесты для маршрутов
│   └── test_services.py    # Тесты для сервисов
│
├── add_data.py             # Скрипт для добавления тестовых данных в БД
├── create_db.py            # Скрипт для создания базы данных
│
├── .env                    # Переменные окружения
├── .gitignore              # Файлы и папки, которые нужно игнорировать в Git
├── alembic/                # Миграции базы данных (если используем Alembic)
│   └── env.py              # Конфигурация миграций
│
├── docker-compose.yml      # Docker для контейнеризации (опционально)
├── README.md               # Описание репозитория проекта 
├── requirements.txt        # Зависимости проекта
└── run.py                  # Точка входа для запуска проекта
```

### Основные функции сайта

✔️ `Главная страница`: Предоставляет общую информацию о магазине и мастерской.

✔️ `Страница автомобилей`: Список доступных автомобилей с возможностью фильтрации и сортировки.

✔️ `Страница услуг`: Перечень услуг, предлагаемых в мастерской.

✔️ `Записи в мастерскую`: Пользователи могут записываться на услуги, предоставляемые мастерской.

✔️ `Контакты`: Информация о том, как связаться с магазином и мастерской.

✔️ `Аналитика`: Сбор данных о действиях пользователей для улучшения сервиса.

### 🌟 Особенности
🎯 `Магазин автомобилей`

- Каталог с фильтрами по марке, модели, цене и другим характеристикам.
- Детализированные карточки автомобилей с фото, спецификациями и ценами.
- Возможность бронирования, покупки и расчета кредита/лизинга.

🔧 `Управление мастерской`
- Запись на обслуживание с выбором даты, времени и типа услуги.
- Отслеживание статуса ремонта через личный кабинет.
- Уведомления через SMS/email.

📈 `Дополнительный функционал`

- Удобная панель администратора для управления контентом.
- Интеграция с платёжными системами для безопасных онлайн-платежей.
- Адаптивный дизайн для любого устройства.

```
uvicorn app.main:app --reload
```

**Автор:** Дуплей Максим Игоревич

**Дата:** 30.10.2024

**Версия:** 1.0
