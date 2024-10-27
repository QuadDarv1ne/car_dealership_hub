# app/db/models.py
from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.db.database import Base

# Модель автомобиля
class Car(Base):
    __tablename__ = 'cars'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    price = Column(Integer)
    image_url = Column(String)

    # Связь с записями
    appointments = relationship("Appointment", back_populates="car")

    def __init__(self, name, description, price, image_url):
        self.name = name
        self.description = description
        self.price = price
        self.image_url = image_url
        
# Модель услуги
class Service(Base):
    __tablename__ = 'services'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    price = Column(Float)

    # Связь с записями
    appointments = relationship("Appointment", back_populates="service")

# Модель пользователя
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)

    # Связь с записями
    appointments = relationship("Appointment", back_populates="user")

# Модель записи в мастерскую
class Appointment(Base):
    __tablename__ = 'appointments'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    car_id = Column(Integer, ForeignKey('cars.id'))
    service_id = Column(Integer, ForeignKey('services.id'))
    appointment_date = Column(DateTime)

    # Определение связей
    user = relationship("User", back_populates="appointments")
    car = relationship("Car", back_populates="appointments")
    service = relationship("Service", back_populates="appointments")
