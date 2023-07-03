#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship


place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'),
                             primary_key=True,
                             nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True,
                             nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=true)
    longitude = Column(Float, nullable=true)
    amenity_ids = []
    reviews = relationship("Review", backref='place',
                           cascade='all, delete, delete-orphan')
    # for FileStorage: getter attribute reviews that returns the list of Review
    # instances with place_id equals to the current Place.id => It will be the
    # FileStorage relationship between Place and Review
    amenities = relationship("Amenity",
                             secondary=place_amenity,
                             back_populates='place_amenities',
                             viewonly=False)
    # for FileStorage:
    # Getter attribute amenities that returns
    # the list of Amenity instances based
    # on the attribute amenity_ids that contains
    # all Amenity.id linked to the Place
    # Setter attribute amenities that handles
    # append method for adding an Amenity.id
    # to the attribute amenity_ids. This method
    # should accept only Amenity object,
    # otherwise, do nothing.
