#!/usr/bin/python3
""" Place Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from models.review import Review
from models.amenity import Amenity
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship


if models.storage_type == "db":
    place_amenity = Table('place_amenity', Base.metadata,
                          Column('place_id', String(60),
                                 ForeignKey('places.id', onupdate='CASCADE',
                                            ondelete='CASCADE'),
                                 primary_key=True), 
                          Column('amenity_id', String(60),
                                ForeignKey('amenities.id', onupdate='CASCADE',
                                            ondelete='CASCADE'),
                                 primary_key=True))


class Place(BaseModel, Base):
    """ Represents a Place for our project, containing various attributes

    Inherits the BaseModel and Base(from sqlalchemy) and links to the mysql table users

    Attributes:
      __tablename__(str): name of the MySQL table
      email(sqlalchemy String): email for the User
      password(sqlalchemy String): password for the User
      first_name(sqlalchemy String): first_name for the User
      last_name(sqlalchemy String): last_name for the User 
    """
    if models.storage_type == "db":
        __tablename__ = "places"
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
        reviews = relationship("Review", backref="place")
        amenities = relationship("Amenity", secondary="place_amenity",
                                 backref="place_amenities", viewonly=False)
    else:
        def __init__(self, city_id = "", user_id = "", name = "", description = "", number_rooms = 0,
                     number_bathrooms = 0, max_guest = 0, price_by_night = 0, latitude = 0.0, longitude = 0.0, amenity_ids = []):
            """ if storage_type is not db (FileStorage) instantiate the values """
            self.city_id = city_id
            self.user_id = user_id
            self.name = name
            self.description = description
            self.number_rooms = number_rooms
            self.number_bathrooms = number_bathrooms
            self.max_guest = max_guest
            self.price_by_night = price_by_night
            self.latitude = latitude
            self.longitude = longitude
            self.amenity_ids = amenity_ids
            super().__init__()

        @property
        def reviews(self):
            """getter attribute reviews that returns the list of Review instances"""
            review_list = []
            all_reviews = models.storage.all(Review)
            for review in all_reviews.values():
                if review.place_id == self.id:
                    review_list.append(review)
            return review_list

        @property
        def amenities(self):
            """getter attribute reviews that returns the list of Amenity instances"""
            amenity_list = []
            all_amenities = models.storage.all(Amenity)
            for amenity in all_amenities.values():
                if amenity.place_id == self.id:
                    amenity_list.append(amenity)
            return amenity_list

        @amenities.setter
        def amenities(self, value):
            """setter for linked amenities"""
            if type(value) == Amenity:
                self.amenity_ids.append(value.id)
