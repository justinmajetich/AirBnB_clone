#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import Base, BaseModel
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from os import getenv
from sqlalchemy.orm import relationship


class Place(BaseModel, Base):
    """ A place to stay """

    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey('cities.id', ondelete='CASCADE'),
                     nullable=False)
    user_id = Column(String(60), ForeignKey('users.id', ondelete='CASCADE'),
                     nullable=False)
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
        reviews = relationship("Review", backref="place",
                               cascade="all, delete, delete-orphan")
    else:
        @property
        def reviews(self):
            '''return a reviews list'''
            from models import storage

            reviwes_list = []
            for place in storage.all('Review'):
                if place.place_id == self.id:
                    reviwes_list.append(place)
            return reviwes_list

    def __init__(self, *args, **kwargs):
        """initializes place"""
        super().__init__(*args, **kwargs)
