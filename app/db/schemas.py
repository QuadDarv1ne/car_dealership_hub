# app/db/schemas.py
from pydantic import BaseModel
from typing import List, Optional

# Схема для автомобиля
class CarBase(BaseModel):
    make: str
    model: str
    year: int
    price: float

class CarCreate(CarBase):
    pass

class Car(CarBase):
    id: int

    class Config:
        from_attributes = True

# Схема для услуги
class ServiceBase(BaseModel):
    name: str
    description: str
    price: float

class ServiceCreate(ServiceBase):
    pass

class Service(ServiceBase):
    id: int

    class Config:
        from_attributes = True

# Схема для записи в мастерскую
class AppointmentBase(BaseModel):
    user_id: int
    car_id: int
    service_id: int
    appointment_date: str

class AppointmentCreate(AppointmentBase):
    pass

class Appointment(AppointmentBase):
    id: int

    class Config:
        from_attributes = True

# Схема для пользователя
class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

    class Config:
        from_attributes = True

# Схема для аутентификации
class UserLogin(BaseModel):
    username: str
    password: str
