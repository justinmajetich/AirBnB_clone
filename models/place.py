#!/usr/bin/python3
""" Place Module for HBNB project """

import os
from sqlalchemy import (
        Column,
        Float,
        ForeignKey,
        Integer,
        String,
        Table
        )
from models.base_model import Base, BaseModel
from sqlalchemy.orm import relationship
from models.review import Review
from models.amenity import Amenity

storage_type = os.getenv("HBNB_TYPE_STORAGE")

association_table = Table(
        "place_amenity",
        Base.metadata,
        Column("place_id", String(60), ForeignKey("places.id"),
               primary_key=True, nullable=False),
        Column("amenity_id", String(60), ForeignKey("amenities.id"),
               primary_key=True, nullable=False),
        )


class Place(BaseModel, Base):
    """
    A class representing the place to stay

    Attributes:
      city_id (str)
      user_id (str)
      name (str)
      description (str)
      number_rooms (int)
      number_bathrooms (int)
      max_guest (int)
      price_by_night (int)
      latitude (float)
      longitude (float)
      amenity_ids (list)
    """

    __tablename__ = "places"

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

    if storage_type == "db":
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
        reviews = relationship("Review", backref="place",
                               cascade="all, delete")
        amenities = relationship("Amenity", secondary=association_table,
                                 backref="place_amenity")

    def __init__(self, *args, **kwargs):
        """
        This is the instantiation of the place and
        """
        super().__init__(*args, **kwargs)
        self.amenity_ids = []

    if storage_type != "db":
        @property
        def reviews(self):
            """
            This is a getter attribute that returns a list of
            Review instances with place_id equals the the current
            Place.id.
            """
            from models import storage
            all_reviews = storage.all(Review)
            return [review for review in all_reviews.values()
                    if review.place_id == self.id]

        @property
        def amenities(self):
            """
            This is a getter attribute that returns a list of
            Amenity instances based on the amenity_ids that contains
            all Amenity.id linked to this place.
            """
            from models import storage
            all_amenities = storage.all(Amenity)
            return [v for k, v in all_amenities.items()
                    if any(x in k for x in self.amenity_ids)]

        @amenities.setter
        def amenities(self, obj=None):
            """
            This is a setter attribute which handles append method for
            adding an Amenity.id to the attribute amenity_id.
            """
            if isinstance(obj, Amenity):
                print(obj.id)
                self.amenity_ids.append(obj.id)
