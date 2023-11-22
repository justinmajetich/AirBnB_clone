#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column
from sqlalchemy import FLoat
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024)) #nullable=True
    number_rooms = Column(Integer, default=0) #nullable=False
    number_bathrooms = Column(Integer, default=0) #nullable=False
    max_guest = Column(Integer, default=0) #nullable=False
    price_by_night = Column(Integer, default=0) #nullable=False
    latitude = Column(Float) #nullable=True
    longitude = Column(Float) #nullable=True
    reviews = relationship("Review", cascade="all, delete", backref="place")
    amenity_ids = []
