#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship
from models.review import Review
import os

STORAGE = os.getenv("HBNB_TYPE_STORAGE")

class Place(BaseModel, Base):
    """ A place to stay """

    __tablename__ = 'places'
    if STORAGE == "db":
        id = Column(String(60), primary_key=True, nullable=False, unique=True)
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship('Review', cascade="all, delete,\
                            delete-orphan", backref='place')
        place_amenity = Table('place_amenity', Base.metadata,
                              Column('place_id', String(60),
                                     ForeignKey('places.id'),
                                     primary_key=True, nullable=False),
                              Column('amenity_id', String(60),
                                     ForeignKey('amenities.id'),
                                     primary_key=True, nullable=False))

        amenities = relationship('Amenity', secondary=place_amenity,
                                 viewonly=False, backref="places")
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
    def reviews(self):
        """Returns the cities"""
        from models import storage
        review_list = []
        for key, value in storage.all(Review).items():
            if self.id == value.place.id:
                review_list.append(value)
        return review_list

    @property
    def amenities(self):
        """Getter method for amenities."""
        from models import storage
        from models.amenity import Amenity
        amenity_objs = storage.all(Amenity)
        amenity_ids = [pa.amenity_id for pa in self.place_amenities]
        return [amenity_objs[aid] for aid in amenity_ids]

    @amenities.setter
    def amenities(self, amenity_obj):
        from models.amenity import Amenity
        """Setter method for amenities."""
        if isinstance(amenity_obj, Amenity):
            self.place_amenities.append(Place.place_amenity(
                place_id=self.id,
                amenity_id=amenity_obj.id))

