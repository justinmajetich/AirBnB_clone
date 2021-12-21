#!/usr/bin/python3
""" Place Module for HBNB project """
from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.expression import false, null
from sqlalchemy.sql.sqltypes import Float
from models.base_model import BaseModel
from models.user import User
from models.city import City
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Place(BaseModel, Base):
    """ A place to stay """

    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    amenity_ids = []
