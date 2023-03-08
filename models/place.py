#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from models.review import Review
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship
from os import getenv


place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'), primary_key=True,
                             nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
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

    storageType = getenv("HBNB_TYPE_STORAGE")
    if storageType == "db":
        reviews = relationship('Review', backref="place",
                               cascade="all, delete, delete-orphan")
        amenities = relationship("Amenity",
                                 secondary=place_amenity,
                                 back_populates='place_amenities',
                                 viewonly=False)
    else:

        @property
        def reviews(self):
            """reviews storage type"""
            from models import storage
            rl = []
            for v in storage.all(Review).values():
                if v.place_id == self.id:
                    rl.append(v)
            return rl

        @property
        def amenities(self):
            """amenities getter"""
            from models import storage
            from models.amenity import Amenity
            x = []
            y = storage.all(Amenity)

            for aminstance in y.values():
                if aminstance.id == self.aminstance_id:
                    x.append(aminstance)
            return x

        @amenities.setter
        def amenities(self, amenity_list):
            """setter"""
            from models.amenity import Amenity
            for t in amenity_list:
                if type(t) == Amenity:
                    self.amenity_ids.append(t)
