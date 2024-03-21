#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.review import Review
from os import getenv


class Place(BaseModel, Base):
    """ The Place class, contains infor about a BnB"""
    __tablename__ = 'places'


    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, default=0)
    longitude = Column(Float, default=0)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship("Review", backref='place',
                            cascade='all, delete, delete-orphan')
    else:
        @property
        def reviews(self):
            """Gets reviews from FileStorage"""
            from models import storage

            review_list = []
            for review in list(storage.all(Review).values()):
                if review.place_id == self.id:
                    review_list.append(review)
            return review_list
