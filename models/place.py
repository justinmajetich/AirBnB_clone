#!/usr/bin/python3
""" Place Module for HBNB project """
# from models.amenity import Amenity
from models.base_model import Base, BaseModel
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table
from os import getenv
from sqlalchemy.orm import relationship
from models import storage

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True, nullable=False))


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
        amenities = relationship("Amenity", secondary=place_amenity,
                                 viewonly=False, back_populates="place_amenities")
    else:
        @property
        def reviews(self):
            '''return a reviews list'''

            reviwes_list = []
            for place in storage.all('Review'):
                if place.place_id == self.id:
                    reviwes_list.append(place)
            return reviwes_list

        @property
        def amenities(self):
            amenities_list = []
            for amenity_obj in storage.all('Amenity').values():
                if amenity_obj.id in self.amenity_ids:
                    amenities_list.append(amenity_obj)
            return amenities_list

        @amenities.setter
        def amenities(self, obj):
            if isinstance(obj, Amenity):
                self.amenity_ids.append(obj.id)

    def __init__(self, *args, **kwargs):
        """initializes place"""
        super().__init__(*args, **kwargs)
