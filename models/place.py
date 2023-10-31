#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
import models
import os

place_amenity = Table(
    'place_amenity',
    Base.metadata,
    Column('place_id', String(60), ForeignKey('places.id'),
            primary_key=True, nullable=False),
    Column('amenity_id', String(60), ForeignKey('amenities.id'),
            primary_key=True, nullable=False)
)

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

    storage_type = os.getenv("HBNB_TYPE_STORAGE")

    if storage_type == 'db':
        reviews = relationship(
            "Review", backref="place", cascade="all, delete-orphan"
        )

        amenities = relationship(
            "Amenity", secondary="place_amenity",
            viewonly=False, back_populates="place_amenities"
        )
    else:
        @property
        def reviews(self):
            review_list = []
            all_reviews = models.storage.all("Review")
            for review in all_reviews.values():
                if review.place_id == self.id:
                    review_list.append(review)
            return review_list

        @property
        def amenities(self):
            from models.amenity import Amenity
            amenity_list = []
            all_amenities = models.storage.all("Amenity")
            for amenity in all_amenities.values():
                if amenity.id in self.amenity_ids:
                    amenity_list.append(amenity)
            return amenity_list

        # @amenities.setter
        # def amenities(self, amenity):
        #     from models.amenity import Amenity
        #     """Setter for amenities attribute"""
        #     if isinstance(amenity, Amenity):
        #         self.amenity_ids.append(amenity.id)
