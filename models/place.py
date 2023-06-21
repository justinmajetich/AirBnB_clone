#!/usr/bin/python3
""" Place Module for HBNB project """
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models.review import Review
from models.engine.file_storage import FileStorage
from os import getenv
from sqlalchemy import Table
from sqlalchemy import String, Integer, Float
from sqlalchemy import ForeignKey, Column
from sqlalchemy.orm import relationship


association_table = Table('place_amenity', Base.metadata,
                          Column('place_id', String(60),
                                 ForeignKey('places.id'),
                                 primary_key=True, nullable=False),
                          Column('amenity_id', String(60),
                                 ForeignKey('amenities.id'),
                                 primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """
    The Place Class Object, inherits from BaseModel and Base

    Attributes:

        city_id (string): foreign key from cities id
        user_id (string): foreign key from states id
        name (string): the name of the place
        description (string): the description of the place
        number_rooms (int): the number of rooms in the place
        number_bathrooms (int): the number of bathroom in place
        max_guest (int): the maximum number of guest in place
        price_by_night (int): the price of place for night
        latitude (float): the latitude of the place
        longitude (float): the longitude of the place.
        amenity_ids (list): A list of all linked amenity ids.
    """

    __tablename__ = "places"
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
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship('Review', backref='place',
                               cascade="all, delete-orphan")
        amenities = relationship('Amenity', secondary='place_amenity',
                                 backref='places', viewonly=False)
    else:
        @property
        def reviews(self):
            return [obj for obj
                    in FileStorage.all(Review).values()
                    if obj.place_id == self.id]

        @property
        def amenities(self):
            return [amenity for amenity
                    in FileStorage.all(Amenity).values()
                    if amenity.place_id in self.amenity_ids]

        @amenities.setter
        def amenities(self, obj):
            if type(self) == Amenity:
                self.amenity_ids.append(obj.id)
