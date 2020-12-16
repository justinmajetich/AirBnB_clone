#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Float, String, ForeignKey, MetaData
from sqlalchemy import Table, Column, Integer
from sqlalchemy.orm import relationship
from os import getenv

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id',
                             String(60),
                             ForeignKey('places.id'),
                             primary_key=True,
                             nullable=False),
                      Column('amenity_id',
                             String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True,
                             nullable=False))

class Place(BaseModel):
    """ A place to stay """

    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)

    if getenv("HBNB_MYSQL_DB") == "db":
        reviews = relationship("Review",
                               backref="place",
                               cascade="all, delete, delete-orphan")
        amenities = relationship("Amenity",
                                 secondary=place_amenity,
                                 viewonly=False)
    else:
                @property
        def reviews(self):
            """
            Returns the list of Review instances
            with place_id equals to the current Place.id
            """
            all_reviews = models.storage.all(Review)
            place_reviews = []
            for review_ins in all_reviews.values():
                if review_ins.place_id == self.id:
                    place_reviews.append(review_ins)

            return place_reviews

        @property
        def amenities(self):
            """
            Returns the list of Amenity instances based on the
            attribute amenity_ids that contains all Amenity.id
            linked to the Place
            """
            all_amenities = models.storage.all(Amenity)
            place_amenities = []
            for amenity_ins in all_amenities.values():
                if amenity_ins.place_id == self.id:
                    place_amenities.append(amenity_ins)

            return place_amenities

        @amenities.setter
        def amenities(self, amenity_obj):
            """
            Handles append method for adding an Amenity.id to the attribute
            amenity_ids
            """
            if isinstance(amenity_obj, models.Amenity):
                self.amenities.append(amenity_obj.id)