#!/usr/bin/python3
""" Place Module for HBNB project """
import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship
from os import getenv

# an instance of SQLAlchemy Table called place_amenity for creating
# the relationship Many-To-Many between Place and Amenity
place_amenities = Table(
    "place_amenity",
    Base.metadata,
    Column(
        "place_id",
        String(60),
        ForeignKey("places.id"),
        primary_key=True,
        nullable=False,
    ),
    Column(
        "amenity_id",
        String(60),
        ForeignKey("amenities.id"),
        primary_key=True,
        nullable=False,
    ),
)

if getenv('HBNB_TYPE_STORAGE') == 'db':
    class Place(BaseModel, Base):
        """ A place to stay """

        __tablename__ = 'places'
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer(), nullable=False, default=0)
        number_bathrooms = Column(Integer(), nullable=False, default=0)
        max_guest = Column(Integer(), nullable=False, default=0)
        price_by_night = Column(Integer(), nullable=False, default=0)
        latitude = Column(Float(), nullable=True)
        longitude = Column(Float(), nullable=True)
        amenity_ids = []

        reviews = relationship(
            "Review",
            backref='place',
            cascade='all, delete, delete-orphan')
        amenities = relationship(
            "Amenity",
            secondary="place_amenity",
            viewonly=False)

        def __init__(self, *args, **kwargs):
            """initializes Place"""
            super().__init__(*args, **kwargs)
else:
    class Place(BaseModel):
        """ A place to stay """
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
            """ Getter method for reviews """
            reviews = models.storage.all(Review).values()
            reviews_list = [
                review for review in reviews if self.id == review.place_id]
            return reviews_list

        @property
        def amenities(self):
            """ Getter method for amenities """
            amenities = models.storage.all(Amenity).values()
            amenities_list = [
                amenity for amenity in amenities
                if amenity.id in self.amenity_ids]
            return amenities_list

        @amenities.setter
        def amenities(self, obj):
            """ handles append method for adding an
            Amenity.id to the attribute amenity_ids """

            # if object isnt of type Amenity, do nothing
            if isinstance(obj, Amenity):
                self.amenity_ids.append(obj.id)
