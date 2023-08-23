#!/usr/bin/python3
"""
Place Module for HBNB project
"""
from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import (
        DateTime, Column, String, Integer, Float, ForeignKey, Table
)
from models.review import Review
from models.amenity import Amenity

place_amenity = Table("place_amenity", Base.metadata,
                      Column("place_id", String(60),
                             ForeignKey("places.id"),
                             primary_key=True,
                             nullable=False),
                      Column("amenity_is", String(60),
                             ForeignKey("amenities.id"),
                             primary_key=True,
                             nullable=False)
                      )


class Place(BaseModel, Base):
    """ A place to stay """

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

    city_id = Column(String(length=60), ForeignKey('cities.id'),
                     nullable=False)
    user_id = Column(String(length=60), ForeignKey('users.id'),
                     nullable=False)
    name = Column(String(length=128), nullable=False)
    description = Column(String(length=1024), nullable=False)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)

    reviews = relationship("Review", backref="place", cascade="delete")
    amenities = relationship("Amenity", secondary="place_amenity",
                             viewonly=False)

    @property
    def reviews(self):
        """
        Review list getter
        """
        from models import storage
        rev_lst = []
        for rev in storage.all(Review).values():
            if rev.place_id == self.id:
                rev_list.append(rev)
        return rev_lst

    @property
    def amenities(self):
        """
        Amenity list getter
        """
        amt_lst = []
        for amt in storage.all(Amenity).values():
            if amt.id in self.amenity_ids:
                amt_lst.append(amt)
        return amt_lst

    @amenities.setter
    def amenities(self, obj=None):
        """
        amenity setter
        """
        if isinstance(obj, Amenity):
            self.amenity_ids.append(obj.id)
