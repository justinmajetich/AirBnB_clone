#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Table
from os import getenv
from models.review import Review
from models.amenity import Amenity


place_amenity = Table(
                    "place_amenity",
                    Base.metadata,
                    Column(
                        "place_id",
                        String(60),
                        ForeignKey("places.id"),
                        primary_key=True,
                        nullable=False
                        ),
                    Column(
                        "amenity_id",
                        String(60),
                        ForeignKey("amenities.id"),
                        primary_key=True,
                        nullable=False
                        ),
                    )

class Place(BaseModel, Base):
    """A place to stay"""

    __tablename__ = "places"
    if getenv("HBNB_TYPE_STORAGE") == "db":
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024))
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float)
        longitude = Column(Float)
        reviews = relationship(
                    "Review",
                    backref="place",
                    cascade="all, delete-orphan")
        amenities = relationship(
                    "Amenity",
                    secondary=place_amenity,
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

        @property
        def reviews(self):
            from models import storage

            reviewList = []
            for review in storage.all(Review):
                if review.id == place_id:
                    reviewList.append(review)
            return reviewList

        @property
        def amenities(self):
            from models import storage

            ameniList = []
            for ameni in storage.all(Amenity):
                if self.id == ameni.id:
                    ameniList.append(ameni)
            return ameniList

        @amenities.setter
        def amenities(self, ameniObj):
            from models import storage

            if isinstance(ameniObj, storage.all(Amenity)):
                self.amenity_ids.append(ameniObj)
