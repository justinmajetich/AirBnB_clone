#!/usr/bin/python3
""" Place Module for HBNB project """
import os

from models.base_model import Base, BaseModel
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship
from models.amenity import Amenity

place_amenity = Table(
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


class Place(BaseModel, Base):
    """Class for Place Module"""

    __tablename__ = "places"
    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024))
        number_rooms = Column(Integer, default=0, nullable=False)
        number_bathrooms = Column(Integer, default=0, nullable=False)
        max_guest = Column(Integer, default=0, nullable=False)
        price_by_night = Column(Integer, default=0, nullable=False)
        latitude = Column(Float)
        longitude = Column(Float)
        reviews = relationship(
            "Review", backref="place", cascade="all, delete, delete-orphan"
        )

        amenities = relationship(
            "Amenity",
            secondary=place_amenity,
            backref="place_amenities",
            viewonly=False,
            # overlaps="place_amenities,amenity",
        )
    else:
        amenity_ids = []

        @property
        def reviews(self):
            """Returns list of Reviews"""
            from models.review import Review
            from models import storage

            reviews = storage.all(Review).values()
            return list(filter(lambda review: review.place_id == self.id,
                               reviews))

        # @property
        # def amenities(self):
        #     """Getter function for the amenity class"""
        #     return self.amenity_ids
        #
        # @amenities.setter
        # def amenities(self, obj: Amenity):
        #     """Setter function for the amenities class"""
        #     if isinstance(obj, Amenity):
        #         self.amenity_ids.append(obj.id)
