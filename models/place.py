#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
import models
from os import getenv
import sqlalchemy
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, Float, String, ForeignKey, Table


if models.storage_t == "db":
    place_amenity = Table('place_amenity', Base.metadata,
                          Column('place_id', String(60),
                                 ForeignKey('places.id', onupdate='CASCADE',
                                            ondelete='CASCADE'),
                                 primary_key=True),
                          Column('amenity_id', String(60),
                                 ForeignKey('amenities.id', onupdate='CASCADE',
                                            ondelete='CASCADE'),
                                 primary_key=True))


class Place(BaseModel, Base):
    """ A place to stay """
    if models.storage_t == 'db':
        __tablename__ = 'places'
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024))
        number_rooms = Column(Integer, default=0, nullable=False)
        number_bathrooms = Column(Integer, default=0, nullable=False)
        max_guest = Column(Integer, default=0, nullable=False)
        price_by_night = Column(Integer, default=0, nullable=False)
        latitude = Column(Float)
        longitude = Column(Float)
        reviews = relationship('Review', backref='place')
        amenities = relationship('Amenity', secondary="place_amenity",
                                 backref="place_amenities",
                                 viewonly=False)
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        amenity_ids = []

    def __init__(self, *args, **kwargs):
        """Inicializa place"""
        super().__init__(*args, **kwargs)

    if models.storage_t != 'db':
        @property
        def reviews(self):
            """ Place reviews """
            from models.review import Review
            review_list = []
            all_reviews = models.storage.all(Review)
            for review in all_reviews.values():
                if review.place_id == self.id:
                    review_list.append(review)
            return review_list

        @property
        def amenities(self):
            """ Place amenities """
            from models.amenity import Amenity
            Amenity_list = []
            all_amenities = models.storage.all(Amenity)
            for amenity in all_Amenity.values():
                if amenity.place_id == self.id:
                    amenity_list.append(amenity)
            return amenity_list
