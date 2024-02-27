#!/usr/bin/python3
"""This is the place class"""
from models.base_model import BaseModel, Base
from models.review import Review
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from os import getenv


place_amenity = Table("place_amenity", Base.metadata,
                      Column("place_id", String(60), ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column("amenity_id", String(60),
                             ForeignKey('amenities.id'), primary_key=True,
                             nullable=False))


class Place(BaseModel, Base):
    """This is the class for Place
    Attributes:
        city_id: city id
        user_id: user id
        name: name input
        description: string of description
        number_rooms: number of room in int
        number_bathrooms: number of bathrooms in int
        max_guest: maximum guest in int
        price_by_night:: pice for a staying in int
        latitude: latitude in flaot
        longitude: longitude in float
        amenity_ids: list of Amenity ids
    """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship('Review', backref='place',
                               cascade='all, delete-orphan')

        amenities = relationship("Amenity", secondary=place_amenity,
                                 viewonly=False)

    if getenv('HBNB_TYPE_STORAGE') == 'fs':
        @property
        def reviews(self):
            review_list = []
            for ob_id, review in models.storage.all(Review).items():
                if self.id == review.place_id:
                    review_list.append(review)
            return review_list

        @property
        def amenities(self):
            """Returns all amenities linked to the place
            """
            am_list = []
            for amenity in amenity_ids:
                if amenity.id == self.id:
                    am_list.append(amenity)
            return am_list

        @amenities.setter
        def amenitites(self, amen):
            """Adds an Amenity.id to amenity_ids"""
            if type(amen).__name__ == 'Amenity':
                self.amenity_ids.append(amen)
