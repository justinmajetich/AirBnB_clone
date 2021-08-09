#!/usr/bin/python3
'''
    Define the class Place.
'''
import os
import models
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from sqlalchemy.orm import relationship
from sqlalchemy import Column, ForeignKey, String, Integer, Float, Table

if os.getenv('HBNB_TYPE_STORAGE') == 'db':
    association_table = Table('place_amenity', Base.metadata,
                              Column('place_id', String(60), ForeignKey(
                                  'places.id'), nullable=False),
                              Column('amenity_id', String(60), ForeignKey(
                                  'amenities.id'), nullable=False)
                              )


class Place(BaseModel, Base):
    '''
        Define the class Place that inherits from BaseModel.
    '''
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = "places"
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
        reviews = relationship("Review", cascade="delete", backref="place")
        amenities = relationship("Amenity",
                                 secondary=association_table,
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
        def amenities(self):
            '''
                 Returns a list containing the amenities ids
            '''
            return self.amenity_ids

        @amenities.setter
        def amenities(self, obj=None):
            '''
                Sets the amenities ids to a list
            '''
            self.amenity_ids = obj.id
            if obj.__class__.__name__ != "Amenity":
                return
            amenity_dict = models.storage.all(obj)
            place_id = self.id
            for key, val in amenity_dict.items():
                if self.id == val.place_id:
                    self.amenity_ids.append(val.id)
