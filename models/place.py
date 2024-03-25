#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship
from models.review import Review
from models.amenity import Amenity


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    reviews = relationship("Review", cascade="all, delete", backref="place")

    @property
    def reviews(self):
        """Getter attribute that returns the list of Reviews"""
        from models import storage
        reviews_list = []
        for review in storage.all(Review).values():
            if review.place_id == self.id:
                reviews_list.append(review)
        return reviews_list

    @property
    def amenities(self):
        """getter for the linked amenities"""
        from models import storage
        all_ameny = storage.all(Amenity).values()
        linked = [amenity for amenity in all_ameny if amenity.id in self.amenity_ids]
        return linked

    @amenities.setter
    def amenities(self, value):
        if isinstance(value, Amenity):
            self.amenity_ids.append(value.id)