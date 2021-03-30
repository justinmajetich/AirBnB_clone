#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.review import Review
from sqlalchemy import Table, Column, Integer, Float, String, ForeignKey
from os import getenv
from sqlalchemy.orm import relationship

type_storage = getenv('HBNB_TYPE_STORAGE')
place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'), primary_key=True,
                             nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'), primary_key=True,
                             nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    amenity_ids = []
    if type_storage == 'db':
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024))
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float)
        longitude = Column(Float)
        reviews = relationship('Review', backref='place',
                               cascade='all, delete')
        amenities = relationship('Amenity', secondary='place_amenity',
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
        reviews = []
        amenities = []

        @property
        def reviews(self):
            """Getter of reviews attribute"""
            reviews_dict = models.FileStorage.all(Review)
            reviews_list = []
            for review in reviews_dict.values():
                if (review.place_id == self.id):
                    reviews_list.append(review)
            return reviews_list

        @property
        def amenities(self):
            """Getter of amenities attribute"""
            amenities_dict = models.FileStorage.all(Amenity)
            amenities_list = []
            for amenity in amenities_dict.values():
                if (amenity.id == self.amenity_ids):
                    amenities_list.append(amenity)
            return amenities_list

        @amenities.setter
        def amenities(self, obj):
            """Setter of amenities attribute"""
            if type(obj) == Amenity:
                self.amenity_ids.append(obj.id)
