#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Table, Column, Integer, String, ForeignKey, Float


class Place(BaseModel, Base):
    """ The Place class """
    __tablename__ = "places"
    city_id = (String(60), ForeignKey('cities.id'), nullable=False)
    user_id = (String(60), ForeignKey('users.id'), nullable=False)
    name = (String(128), nullable=False)
    description = (String(1024), nullable=False)
    number_rooms = (Integer, nullable=False, default=0)
    number_bathrooms = (Integer, nullable=False, default=0)
    max_guest = (Integer, nullable=False, default=0)
    price_by_night = (Integer, nullable=False, default=0)
    latitude = (Float, nullable=False)
    longitude = (Float, nullable=False)
    amenity_ids = []

    reviews = relationship("Review", backref="place", cascade="all, delete")

    @property
    def reviews(self):
        my_list = {}
        all_review = self.reviews
        for rev in all_review:
            if self.id == rev.id:
                my_list.append(rev)
        return my_list
