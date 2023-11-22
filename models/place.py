#!/usr/bin/python3
""" Place Module for HBNB project """
from os import getenv
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column
from sqlalchemy import FLoat
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Table
from sqlalchemy.orm import relationship

lk_table = Table("place_amenity", Base.metadata,
                 Column("place_id", String(60), ForeignKey("place.id"),
                        primary_ke=True, nullable=False),
                 Column("amenity_id", String(60), ForeignKey("amenity.id"),
                        primary_key=True, nallable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))  # nullable=True
    number_rooms = Column(Integer, default=0)  # nullable=False
    number_bathrooms = Column(Integer, default=0)  # nullable=False
    max_guest = Column(Integer, default=0)  # nullable=False
    price_by_night = Column(Integer, default=0)  # nullable=False
    latitude = Column(Float)  # nullable=True
    longitude = Column(Float)  # nullable=True
    reviews = relationship("Review", cascade="all, delete", backref="place")
    amenities = relationship("Amenity", secondary="place_amenity",
                             viewonly=False)
    amenity_ids = []

     if getenv("HBNB_TYPE_STORAGE", None) != "db":
         @property
         def reviews(self):
             """ Get a list of all linked reviews. """
             reviewList = []
             for review in list(models.storage.all(Review).values()):
                 if review.place.id == self.id:
                     reviewList.append(review)
             return reviewList
