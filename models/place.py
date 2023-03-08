#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from models.review import Review
from os import getenv
from sqlalchemy.orm import relationship


place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'),
                             primary_key=True,
                             nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True,
                             nullable=False))


class Place(BaseModel, Base):
    """ Place class """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    storageType = getenv("HBNB_TYPE_STORAGE")
    if storageType == "db":
        reviews = relationship('Review',
                               cascade="all, delete, delete-orphan",
                               backref="place")
        amenities = relationship("Amenity",
                                 secondary=place_amenity,
                                 back_populates='place_amenities',
                                 viewonly=False)

    else:
        @property
        def reviews(self):
            """ getter for reviews """
            from models import storage
            rev_list = []
            for x in storage.all(Review).values():
                if x.place_id == self.id:
                    rev_list.append(x)
            return rev_list

        @property
        def amenities(self):
            """getter for amenities"""
            from models import storage
            from models.amenity import Amenity
            ame_list = []
            i = storage.all(Amenity)

            for amenity_in in i.values():
                if amenity_in.id == self.amenity_id:
                    ame_list.append(amenity_in)
            return ame_list

        @amenities.setter
        def amenities(self, obj):
            from models.amenity import Amenity
            """setter for amenities"""
            for j in obj:
                if type(j) == Amenity:
                    self.amenity_ids.append(j)
