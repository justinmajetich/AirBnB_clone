#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from models.review import Review
from models.amenity import Amenity
from sqlalchemy import Column, Integer, String, ForeignKey, Float, null
from sqlalchemy.orm import relationship
from sqlalchemy import Table, MetaData
import os


metadata = MetaData()


class Place(BaseModel, Base):
    """ A place to stay """
    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = 'places'
        place_amenity = Table('place_amenity',
                              metadata,
                              Column('place_id',
                                     String(60),
                                     ForeignKey('places.id'),
                                     primary_key=True,
                                     nullable=False),
                              Column('amenity_id',
                                     String(60),
                                     ForeignKey('amenities.id'),
                                     primary_key=True,
                                     nullable=False)
                              )

        city_id = Column(String(60), ForeignKey('cities.id'))
        user_id = Column(String(60), ForeignKey('users.id'))
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        user = relationship("User", back_populates="places")
        cities = relationship("City", back_populates="places")
        reviews = relationship("Review", back_populates="place",
                               cascade="all, delete")
        amenities = relationship("Amenity", secondary="place_amenity",
                                 viewonly=False, overlaps="place_amenities")

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
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            """getter method to return the list of Review instances"""
            from models import storage
            review_list = storage.all(Review)
            return [review for review in review_list.values()
                    if review.place_id == self.id]

        @property
        def amenities(self):
            """getter method to return the list of Amenity"""
            from models import storage
            amenity_list = storage.all(Amenity)
            return [amenity for amenity in amenity_list.values()
                    if amenity.amenity_ids == self.id]

        @amenities.setter
        def amenities(self, obj):
            """
            Setter attribute amenities that handles append method for adding
            an Amenity. id to the attribute amenity_ids. This method should
            accept only Amenity object, otherwise, do nothing.
            """
            from models import storage
            if isinstance(obj, Amenity):
                self.amenity_ids.append(obj.id)
