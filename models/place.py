#!/usr/bin/python3
""" Place Module for HBNB project """
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from models.review import Review
from models.amenity import Amenity
from os import getenv

place_amenity_table = Table('place_amenity', Base.metadata,
                            Column('place_id', String(60), 
                                   ForeignKey('places.id'),
                                   primary_key=True, nullable=False),
                            Column('amenity_id', String(60),
                                   ForeignKey('amenities.id'),
                                   primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """The class Place and its attributes"""
    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0)
    number_bathrooms = Column(Integer, default=0)
    max_guest = Column(Integer, default=0)
    price_by_night = Column(Integer, default=0)
    latitude = Column(Float)
    longitude = Column(Float)

    reviews = relationship("Review", backref="place", cascade="delete")
    
    amenities = relationship("Amenity", secondary='place_amenity',
                             viewonly=False)

    amenity_ids = []

    if getenv('HBNB_TYPE_STORAGE', None) == 'file':
        @property
        def reviews(self):
            """Getter attribute for reviews in FileStorage."""
            from models import storage
            review_list = []
            for review in list(storage.all(Review).values()):
                if review.place_id == self.id:
                    review_list.append(review)
            return review_list

        @property
        def amenities(self):
            """Getter attribute for amenities in FileStorage."""
            from models import storage
            amenity_list = []
            for amenity in list(storage.all(Amenity).values()):
                if amenity.id in self.amenity_ids:
                    amenity_list.append(amenity)
            return amenity_list

        @amenities.setter
        def amenities(self, obj):
            """Setter attribute for amenities in FileStorage."""
            if type(obj) in Amenity:
                self.amenity_ids.append(obj.id)
