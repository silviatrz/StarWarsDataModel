import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)

class Character(Base):
    __tablename__ = 'character'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    birth_year = Column(Integer, nullable=True)
    gender = Column(String(25), nullable=True)
    height = Column(Float, nullable=False)
    skin_color = Column(String(25), nullable=False)
    hair_color = Column(String(25), nullable=False)
    description = Column(String(300), nullable=False)
    photo_url = Column(String(300), nullable=False)
   # person_id = Column(Integer, ForeignKey('person.id'))
   # person = relationship(Person)

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    climate = Column(String(25), nullable=False)
    population = Column(Integer, nullable=True)
    orbital_period = Column(Float, nullable=False)
    rotation_period = Column(Float, nullable=False)
    diameter = Column(Float, nullable=False)
    description = Column(String(300), nullable=False)
    photo_url = Column(String(300), nullable=False)

class Vehicle(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    model = Column(String(50), nullable=False)
    starship_class = Column(String(25), nullable=False)
    manufacturer = Column(String(25), nullable=False)
    length = Column(Float, nullable=False)
    passengers = Column(Integer, nullable=True)
    description = Column(String(300), nullable=False)
    photo_url = Column(String(300), nullable=False)

class Character_Fav(Base):
    __tablename__ = 'character_fav'
    id = Column(Integer, primary_key=True)
    id_user = Column(Integer, ForeignKey('user.id'), nullable=False)
    id_character = Column(Integer, ForeignKey('character.id'), nullable=False)
    user = relationship(User)
    character = relationship(Character)

class Planet_Fav(Base):
    __tablename__ = 'planet_fav'
    id = Column(Integer, primary_key=True)
    id_user = Column(Integer, ForeignKey('user.id'), nullable=False)
    id_planet = Column(Integer, ForeignKey('planet.id'), nullable=False)
    user = relationship(User)
    planet = relationship(Planet)

class Vehicle_Fav(Base):
    __tablename__ = 'vehicle_fav'
    id = Column(Integer, primary_key=True)
    id_user = Column(Integer, ForeignKey('user.id'), nullable=False)
    id_vehicle = Column(Integer, ForeignKey('vehicle.id'), nullable=False)
    vehicle = relationship(Vehicle)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')