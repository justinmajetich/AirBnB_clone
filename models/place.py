#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, Float, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from os import getenv

asociation = Table('place_amenity', Base.metadata,
                   Column('place_id',
                          String(60),
                          ForeignKey("places.id"),
                          primary_key=True,
                          nullable=False),
                   Column('amenity_id',
                          String(60),
                          ForeignKey("amenities.id"),
                          primary_key=True,
                          nullable=False)
                   )


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship('Review',
                               backref='state', cascade='all, delete')

        amenities = relationship('Amenity',
                                 secondary="place_amenity", viewonly=False)
    else:
        @property
        def reviews(self):
            """Getter method for cities
            Return: list of reviews with state_id equal to self.id
            """
            from models import storage
            from models.review import Review
            reviews_dict = storage.all(Review)
            reviews_list = []

            for review in reviews_dict.values():
                if review.place_id == self.id:
                    reviews_list.append(review)
            return reviews_list

        @property
        def amenities(self):
            """Getter method for reviews Return: reviews list """
            from models import storage
            from models.amenities import Amenity
            save_amenities = storage.all(Amenity)
            obj_amenities = []

            for obj in save_amenities.values():
                if obj.id in amenity_ids:
                    obj_amenities.append(obj)
            return obj_amenities

        @amenities.setter
        def amenities(self, obj):
            """obj inside """
            from models.amenities import Amenity
            if isinstance(obj, Amenity):
                amenity_ids.append(obj.id)
