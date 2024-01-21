#!/usr/bin/python3
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey

class City(BaseModel, Base):
    __tablename__ = 'cities'
     __tablename__ = "cities"
    places = relationship("Place", backref="city", cascade="all, delete")
