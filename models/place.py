#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


# class Place(BaseModel):
#     """ A place to stay """
#     city_id = ""
#     user_id = ""
#     name = ""
#     description = ""
#     number_rooms = 0
#     number_bathrooms = 0
#     max_guest = 0
#     price_by_night = 0
#     latitude = 0.0
#     longitude = 0.0
#     amenity_ids = []

class Place(BaseModel, Base):
    """
    Database File Storage Method for Place
    """
    __tablename__ = "places"
    city_id = Column(String(60), nullable=False, ForeignKey("cities.id"))
    user_id = Column(String(60), nullable=False, ForeignKey("users.id"))
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
