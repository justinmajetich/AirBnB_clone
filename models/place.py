#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Table
from sqlalchemy.orm import relationship, backref
import models
import sqlalchemy
from models.amenity import Amenity


if models.dbstorage == 'db':
    place_amenity = Table('place_amenity', Base.metadata,
                          Column("place_id", String(60),
                                 ForeignKey('places.id'),
                                 primary_key=True, nullable=False),
                          Column("amenity_id", String(60),
                                 ForeignKey('amenities.id'),
                                 primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    if models.dbstorage == "db":
        __tablename__ = "places"
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, default=0, nullable=False)
        number_bathrooms = Column(Integer, default=0, nullable=False)
        max_guest = Column(Integer, default=0, nullable=False)
        price_by_night = Column(Integer, default=0, nullable=False)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship('Review', cascade='all,delete', backref='place')
        amenities = relationship('Amenity', secondary="place_amenity",
                                 back_populates="place_amenities", viewonly=False)
    else:
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

        if models.dbstorage != 'db':
            @property
            def reviews(self):
                """ Returns the list of review instances with place_id equals to
                the current Place.id
                FileStorage relationship between Place and Review
                """
                from models.review import Review
                related_reviews = []
                reviews = models.storage.all(Review)
                for review in reviews.values():
                    if review.place_id == self.id:
                        related_reviews.append(review)
                return related_reviews


            @property
            def amenities(self):
                """
                Getter attribute amenities that returns the list of Amenity
                instances based on the attribute amenity_ids that contains
                all Amenity.id linked to the Place
                """
            
                from models.amenity import Amenity
                amenity_instances = []
                amenities = models.storage.all(Amenity)
                for amenity in amenities.values():
                    if amenity.place_id == self.id:
                        amenity_instances.append(amenity)
                return amenity_instances

            @amenities.setter
            def amenities(self, obj):
                """setter for amenities class"""
                if (isinstance(obj, Amenity)):
                    self.amenity_ids.append(obj.id)
