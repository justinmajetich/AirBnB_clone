#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel
from models import storage
from sqlalchemy import Table, Column
from sqlalchemy import Integer, Float, String
from sqlalchemy.orm import relationship

class Place(BaseModel):
    """ A place to stay """
    __tablename__='places'
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=False)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float)
        longitude = Column(Float)
        reviews = relationship("Review", backref="place", cascade="all, delete")
    else:
        city_id = ''
        user_id = ''
        name = ''
        description = ''
        number_rooms = ''
        number_bathrooms = ''
        max_guest = ''
        price_by_night = ''
        latitude = ''
        longitude = ''
        @property
        def reviews(self):
            """
            returns the list of Review instances with place_id equals
            to the current Place.id => It will be the FileStorage
            relationship between Place and Review
            """
            total_reviews = storage.all(Review)
            result = []
            for each in total_reviews.values():
                result.append(each)
            return result
