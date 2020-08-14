#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy import Table
from sqlalchemy.orm import relationship
import os

place_amenity = Table(
    "place_amenity", Base.metadata,
    Column("place_id", String(60), ForeignKey("places.id"),
           primary_key=True, nullable=False),
    Column("amenity_id", String(60), ForeignKey("amenities.id"),
           primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """This Class stores information of places"""
    __tablename__ = "places"
    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, default=0, nullable=False)
        number_bathrooms = Column(Integer, default=0, nullable=False)
        max_guest = Column(Integer, default=0, nullable=False)
        price_by_night = Column(Integer, default=0, nullable=False)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        amenity_ids = []
        reviews = relationship(
            "Review",
            backref="place",
            cascade="all")
        amenities = relationship(
            "Amenity",
            secondary="place_amenity",
            viewonly=False,
            back_populates="place_amenities"
            )
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

    if os.getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def reviews(self):
            """Getter for reviews"""
            from models.review import Review

            list_reviews = []
            for c in FileStorage.all(Review).values():
                if c.place_id == self.id:
                    list_reviews.append(c)
            return list_reviews

        @property
        def amenities(self):
            """Getter for amenities"""
            from models.amenity import Amenity
            from models import storage

            list_amenities = []
            for c in storage.all(Amenity).values():
                if c.id in self.amenity_ids:
                    list_amenities.append(c)
            return list_amenities

        @amenities.setter
        def amenities(self, value):
            """Setter for amenities"""
            from models.amenity import Amenity

            if isinstance(value, Amenity):
                self.amenity_ids.append(value.id)
