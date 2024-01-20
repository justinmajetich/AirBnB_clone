#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
import models
from models.review import Review


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
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
    cities = relationship('City', back_populates='places')
    user = relationship("User", back_populates="places",
                        cascade="all, delete, save-update")
    reviews = relationship('Review', backref='place',
                           cascade="all, delete, save-update")

    @property
    def reviews(self):
        """
        for FileStorage: getter attribute reviews
        that returns the list of Review instances
        """
        allReviews = models.storage.all(Review)
        return [review for review in allReviews if review.place_id == self.id]
