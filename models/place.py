#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__='place'
    city_id = Column(Sting(60), nullable=False, ForignKey("cities.id"))
    user_id = Column(Sting(60), nullable=False, ForignKey("users.id"))
    name = Column(Sting(128), nullable=False)
    description = Column(Sting(1024), nullable=False)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
