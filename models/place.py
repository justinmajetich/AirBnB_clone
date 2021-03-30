#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from models.amenity import Amenity
from models.review import Review
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship

table_relation = Table('place_amenity', Base.metadata, Column('place_id', String(60), ForeignKey('places.id'), primary_key=True,
                       nullable=False), Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
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

    reviews = relationship('Review', backref='place', cascade='delete')
    amenities = relationship(
        'Amenity', secondary='place_amenity', viewonly=False)

    amenity_ids = []