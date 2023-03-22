#!/usr/bin/python3
""" Place Module for HBNB project """
from os import getenv
import models
from models.review import Review
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey, Float, Table
from sqlalchemy.orm import relationship


place_amenity = Table('place_amenity', Base.metadata,
                          Column('place_id', String(60),
                                 ForeignKey('places.id'),
                                 primary_key=True,
                                 nullable=False),
                          Column('amenity_id', String(60),
                                 ForeignKey('amenities.id'),
                                 primary_key=True,
                                 nullable=False)
                          )


class Place(BaseModel, Base):
    """Place inherits from BaseModel and Base
    class attribute __tablename__:
        represents the table name, places
    """
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
    reviews = relationship("Review", backref="place", cascade="delete")
    amenities = relationship('Amenity', secondary=place_amenity, viewonly=False)
    amenity_ids = []
    

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def reviews(self):
            """getter attribute reviews that returns the list of Review instances
            with place_id equals to the current Place.id => It will be the FileStorage
            relationship between Place and Review
            """
            list = list(models.storage.all(Review).values())
            return [review for review in list if review.place_id == self.id]
        
        @property
        def amenities(self):
            """Getter attribute amenities that returns the list of Amenity instances
            based on the attribute amenity_ids that contains all Amenity.id linked to the Place
            """
            list = list(models.storage.all(Amenity).values())
            return [amenity for amenity in list if amenity.id in self.amenity_ids]
        
        @amenities.setter
        def amenities(self, val):
            """Setter attribute amenities that handles append method for
            adding an Amenity.id to the attribute amenity_ids.
            This method should accept only Amenity object, otherwise, do nothing
            """
            if type(val) == Amenity:
                self.amenity_ids.append(val.id)