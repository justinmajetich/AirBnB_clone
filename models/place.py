#!/usr/bin/python3
""" Place Module for HBNB project """
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from models.base_model import BaseModel
from sqlalchemy.orm import relationship
from models.review import Review
import os


class Place(BaseModel):
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

    """For DBStorage: Define a relationship with the class Review, and specify the behavior
    when a Place object is deleted (cascading deletion)."""
    reviews = relationship("Review", backref="place", cascade="all, delete-orphan")
    
    """For FileStorage: Implement a getter attribute for reviews."""
    if os.getenv('HBNB_TYPE_STORAGE') == 'file':
        @property
        def reviews(self):
            """Getter attribute for reviews in FileStorage."""
            from models import storage
            review_list = []
            for review in storage.all(Review).values():
                if review.place_id == self.id:
                    review_list.append(review)
            return review_list
