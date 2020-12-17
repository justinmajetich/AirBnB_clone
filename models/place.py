#!/usr/bin/python3
""" Place Module for HBNB project """
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship


class Place(BaseModel):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), nullable=False, ForeignKey('cities.id'))
    user_id = Column(String(60), nullable=False, ForeignKey('users.id'))
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    amenity_ids = []
    reviews = relationship("Review", cascade="all, delete", backref="place")
    reviews = relationship("Review", cascade="all, delete", backref="place")

    @property
    def reviews(self):
        from models import storage
        review_list = []
        review_dict = storage.all(Review)
        for key, obj in review_dict.items():
            if self.id == obj['place_id']:
                review_list += obj
        return (review_list)
