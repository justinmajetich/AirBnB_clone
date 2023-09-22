#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship
from os import getenv


storage_type = getenv("HBNB_TYPE_STORAGE")


place_amenity = Table(
        'place_amenity', Base.metadata,
        Column(
            'place_id', String(60),
            ForeignKey('places.id'),
            primary_key=True,
            nullable=False
            ),
        Column(
            'amenity_id', String(60),
            ForeignKey('amenities.id'),
            primary_key=True,
            nullable=False
            ),
        )


class Place(BaseModel, Base):
    """ A place to stay """

    __tablename__ = 'places'

    if storage_type == 'db':
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=False)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship('Review', cascade="all,delete", backref="place")
        amenities = relationship(
                "Amenity", secondary=place_amenity,
                back_populates="place_amenities",
                viewonly=False)
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
            '''
            returns the list of Review instances with place_id
            equals to the current Place.id
            '''
            from models import storage
            list_reviews = []
            all_reviews = storage.all(Review)
            for review in all_reviews.values():
                if review.place_id == self.id:
                    list_reviews.append(review)

            return list_reviews

        @property
        def amenities(self):
            '''
            returns the list of Amenity instances based on the attribute
            amenity_ids that contains all Amenity.id linked to the Place
            '''
            from models import storage
            all_amenities = storage.all(Anemity)
            list_amenities = []
            for amenity in all_amenities.values():
                if amenity.id == self.amenity_ids:
                    list_amenities.append(amenity)

            return list_amenities

        @amenities.setter
        def amenities(self, amenity):
            '''
            handles append method for adding an Amenity.id to the
            attribute amenity_ids
            '''
            if isinstance(amenity, Amenity):
                self.amenity_ids.append(amenity.id)
