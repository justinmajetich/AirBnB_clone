#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from models.review import Review
from models.amenity import Amenity
from sqlalchemy import Table, Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv


if getenv('HBNB_TYPE_STORAGE') == 'db':
    place_amenity = Table('place_amenity', Base.metadata,
                          Column('place_id',
                                 String(60), ForeignKey('places.id'),
                                 primary_key=True, nullable=False),
                          Column('amenity_id',
                                 String(60), ForeignKey('amenities.id'),
                                 primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'places'
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024))
        number_rooms = Column(Integer, default=0, nullable=False)
        number_bathrooms = Column(Integer, default=0, nullable=False)
        max_guest = Column(Integer, default=0, nullable=False)
        price_by_night = Column(Integer, default=0, nullable=False)
        latitude = Column(Float)
        longitude = Column(Float)
        amenity_ids = []
        reviews = relationship("Review",
                               backref="place",
                               cascade="all, delete, delete-orphan")
        amenities = relationship("Amenity",
                                 secondary='place_amenity',
                                 back_populates="place_amenities",
                                 viewonly=False)
    else:
        city_id = ''
        user_id = ''
        name = ''
        description = ''
        number_rooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            """Returns a list of 'Review' instances for this place"""
            from models import storage
            all_reviews = storage.all(Review)
            my_reviews = [rr for rr in all_reviews.values()
                          if rr.place_id == self.id]
            return my_reviews

        @property
        def amenities(self):
            """Return a list of 'Amenity' instances for this place"""
            from models import storage
            all_amenities = storage.all(Amenity)
            my_amenities = [amen for amen in all_amenities.values()
                            if amen.id in self.amenity_ids]

        @amenities.setter
        def amenities(self, value):
            """Add amenity id of amenity available at this place
            in amenity_ids
            """
            if (type(value) is Amenity):
                amenity_ids.append(value.id)
