#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy import Column, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from models.amenity import Amenity

# from models.review import Review
from os import getenv


metadata = Base.metadata
place_amenity = Table(
    "place_amenity",
    metadata,
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
    """The Place class, contains infor about a BnBs"""

    __tablename__ = "places"

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
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship(
            "Review",
            backref="place",
            cascade="all, delete, delete-orphan",
        )
        amenities = relationship(
            "Amenity",
            secondary=place_amenity,
            viewonly=False,
            overlaps="amenities",
        )
    else:

        @property
        def reviews(self):
            """Gets reviews from FileStorage"""
            from models import storage
            from models.review import Review

            review_list = []
            for review in list(storage.all(Review).values()):
                if review.place_id == self.id:
                    review_list.append(review)
            return review_list

        @property
        def amenities(self):
            """Getter attribute amenities that
            returns the list of Amenity instances"""
            from models import storage

            amenity_list = []
            for amenity in list(storage.all(Amenity).values()):
                if amenity.id in self.amenity_ids:
                    amenity_list.append(amenity)
            return amenity_list

        @amenities.setter
        def amenities(self, value):
            """Setter attribute amenities that handles
            append method for adding an Amenity.id"""

            if isinstance(value, Amenity):
                self.amenity_ids.append(value.id)
