#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
import os
from sqlalchemy.orm import relationship
from models import storage
from models.amenity import Amenity


storageType = os.environ.get('HBNB_TYPE_STORAGE')

place_amenity = Table(
    'place_amenity',
    Base.metadata,
    Column(
        'place_id',
        String(60),
        ForeignKey('places.id'),
        primary_key=True,
        nullable=False
    ),
    Column(
        'amenity_id',
        String(60),
        ForeignKey('amenities.id'),
        primary_key=True,
        nullable=False
    )
)


class Place(BaseModel, Base):
    """ A place to stay """
    city_id = Column(
        'city_id',
        String(60),
        ForeignKey('cities.id'),
        nullable=False
    )
    user_id = Column(
        'user_id',
        String(60),
        ForeignKey('users.id'),
        nullable=False
    )
    name = Column('name', String(128), nullable=False)
    description = Column(
        'description',
        String(1024),
        nullable=True
    )
    number_rooms = Column(
        'number_rooms',
        Integer,
        nullable=False,
        default=0
    )
    number_bathrooms = Column(
        'number_bathrooms',
        Integer,
        nullable=False,
        default=0
    )
    max_guest = Column('max_guest', Integer, nullable=False, default=0)
    price_by_night = Column(
        'price_by_night',
        Integer,
        nullable=False,
        default=0
    )
    latitude = Column('latitude', Float, nullable=True)
    longitude = Column('longitude', Float, nullable=True)
    amenity_ids = []
    __tablename__ = 'places'

    if storageType == 'db':
        reviews = relationship(
            'Review',
            backref='place',
            cascade='all, delete, delete-orphan'
        )
        amenities = relationship(
            'Amenity',
            secondary=place_amenity,
            viewonly=False,
            back_populates='place_amenities'
        )
    else:
        @property
        def reviews(self):
            """Returns review instances"""
            revwList = []
            allRevws = storage.all('Review').values()
            for rvw in allRevws:
                if rvw.place_id == self.id:
                    revwList.append(rvw)
            return revwList

        @property
        def amenities(self):
            """amenities getter attribute function"""
            return self.amenity_ids

        @amenities.setter
        def amenities(self, inst=None):
            """amenities setter attribute function"""
            if inst.__class__ == Amenity:
                self.amenity_ids.append(Amenity.id)
