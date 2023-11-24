#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship
from os import getenv

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'), primary_key=True,
                             nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'), primary_key=True,
                             nullable=False))


class Place(BaseModel):
    """ A place to stay """

    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)
    number_rooms = Column(Integer, default=0)
    number_bathrooms = Column(Integer, default=0)
    max_guest = Column(Integer, default=0)
    price_by_night = Column(Integer, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship("Review", backref="place",
                               cascade="all, delete")
        amenities = relationship(
            "Amenity", secondary=place_amenity, viewonly=False,
            back_populates="place_amenities")
    else:
        @property
        def reviews(self):
            """ Getter for reviews """
            from models import storage
            from models.review import Review

            reviews = storage.all(Review)
            reviews_list = []

            for review in reviews.values():
                if review.place_id == self.id:
                    reviews_list.append(review)

            return reviews_list

        @property
        def amenities(self):
            """ Getter for amenities """
            from models import storage
            from models.amenity import Amenity

            amenities = storage.all(Amenity)
            amenities_list = []

            for amenity in amenities.values():
                if amenity.id in self.amenity_ids:
                    amenities_list.append(amenity)

            return amenities_list

        @amenities.setter
        def amenities(self, obj):
            """ Setter for amenities """
            from models.amenity import Amenity
            if isinstance(obj, Amenity) and obj.id not in self.amenity_ids:
                self.amenity_ids.append(obj.id)
