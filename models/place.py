#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from models.review import Review
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from os import getenv


place_amenity = Table(
    'place_amenity',
    Base.metadata,
    Column('place_id', String(60),
           ForeignKey('places.id'),
           nullable=False, primary_key=True),
    Column('amenity_id', String(60),
           ForeignKey('amenities.id'),
           nullable=False, primary_key=True)
)


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    reviews = relationship('Review', cascade='delete', backref='place')
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        amenities = relationship('Amenity', secondary='place_amenity',
                                 back_populates='place_amenities',
                                viewonly=False)
    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def reviews(self):
            import models
            reviews_list = []
            all_reviews_list = models.storage.all(Review)
            for review in all_reviews_list.values():
                if review.place_id == self.id:
                    reviews_list.append(review)
            return reviews_list

        @property
        def amenities(self):
            import models
            from models.amenity import Amenity
            amenities_list = []
            all_amenities_list = models.storage.all(Amenity)
            for amenity in all_amenities_list.values():
                amenities_list.append(amenity.id)
            return amenities_list

        @amenities.setter
        def amenities(self, obj):
            from models.amenity import Amenity
            if isinstance(obj, Amenity):
                if self.id == obj.place_id:
                    self.amenity_ids.append(obj.id)
