#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Table
from sqlalchemy.orm import relationship
from models.review import Review
from models.amenity import Amenity
import models
import os

place_amenity = Table("place_amenity", Base.metadata,
                      Column("place_id", String(60),
                             ForeignKey("places.id"),
                             primary_key=True, nullable=False),
                      Column("amenity_id", String(60),
                             ForeignKey("amenities.id"),
                             primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """

    __tablename__ = "places"
    if (os.getenv("HBNB_TYPE_STORAGE") == "db"):

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
        reviews = relationship('Review',
                               backref='place', cascade='all, delete-orphan')
        amenities = relationship(
            'Amenity', secondary="place_amenity", viewonly=False)
        amenity_ids = []

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

        @property
        def reviews(self):
            """ getter to reviews return a list of reviews for
            the actual isntance Placce """
            list_reviews_inst = []
            for reviews_inst in models.storage.all(Review).values():
                if reviews_inst.place_id == self.id:
                    list_reviews_inst.append(reviews_inst)
            return (list_reviews_inst)

        @property
        def amenities(self):
            """ getter amenities is attribute of class Place
            Returns a list of instances of type class Amenities"""
            list_amenities_inst = []
            for amenity_inst in models.storage.all(Amenity).values():
                if amenity_inst.id in self.amenity_ids:
                    list_amenities_inst.append(amenity_inst)
            return (list_amenities_inst)

        @amenities.setter
        def amenities(self, inst_amenity):
            """ setter amenities is an attribute of class Place that adds
            an Instance of type amenity into the list amenities_ids"""
            if isinstance(inst_amenity, Amenity):
                self.amenity_ids.append(inst_amenity)
