#!/usr/bin/python3
""" Place Module for HBNB project """
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Table
from models.base_model import BaseModel, Base
from models.review import Review
from sqlalchemy.orm import relationship
from os import getenv

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
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
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship("Review",
                               cascade="all, delete, delete-orphan",
                               backref="place")
        amenities = relationship('Amenity',
                                 secondary=place_amenity,
                                 viewonly=False)
    else:
        @property
        def reviews(self):
            """review method"""
            from models import storage
            review_list = []
            review_dict = storage.all(Review)
            for key, obj in review_dict.items():
                if self.id == obj.place_id:  # if self.id == obj.place_id:
                    review_list.append(obj)
            return review_list

        @property
        def amenities(self):
            """getter"""
            from models import storage
            from models.amenity import Amenity
            amenity_list = []
            amenity_dict = storage.all(Amenity)
            for obj in amenity_dict.values():
                if self.id == obj.amenity_id:  # if self.id == obj.amenity_ids:
                    amenity_list.append(obj)
            return amenity_list

        @amenities.setter
        def amenities(self, value=None):
            """setter"""
            from models import storage
            from models.amenity import Amenity
            if type(value) == Amenity:
                # if type(value) == Amenity:
                self.append(value)  # self.append(value)
