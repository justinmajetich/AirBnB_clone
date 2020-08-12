#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from models.review import Review
import os


class Place(BaseModel, Base):
    """ A place to stay """

    __tablename__ = "places"
    if (os.getenv("HBNB_TYPE_STORAGE") == "db"):

        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, default=0, nullable=False)
        number_bathrooms = Column(Integer, default=0, nullable=False)
        max_guest = Column(Integer, default=0, nullable=False)
        price_by_night = Column(Integer, default=0, nullable=False)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship('Review',
                               backref='place', cascade='all, delete-orphan')

    else:

        @property
        def reviews(self):
            """ getter to filestorage """
            lista = []
            # Returns the list of City instances with
            # state_id == to the current State.id
            for value in storage.all(Review).values():
                dict_obj = value.to_dict()
                if dict_obj["place_id"] == self.id:
                    lista.append(value)
            return (lista)
