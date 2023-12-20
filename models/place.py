#!/usr/bin/python3
""" Place Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import backref, relationship
import os

place_amenity = Table(
    "place_amenity",
    Base.metadata,
    Column("place_id", String(60), ForeignKey("places.id"),
           primary_key=True, nullable=False),
    Column("amenity_id", String(60), ForeignKey("amenities.id"),
           primary_key=True, nullable=False)
)


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
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

    @property
    def reviews(self):
        """getter for reviews relationship for FileStorage"""
        Review_Class = BaseModel.all_classes(BaseModel, 'Review')
        result = models.storage.all(Review_Class)
        selected_reviews = [v for k, v in result.items()
                            if v.place_id == self.id]
        return selected_reviews

    @property
    def amenities(self):
        """getter for amenity relationship for FileStorage"""
        Amenity_Class = BaseModel.all_classes(BaseModel, 'Amenity')
        result = models.storage.all(Amenity_Class)
        selected_amenities = [v for k, v in result.items()
                              if v.place_id == self.id]
        return selected_amenities

    @amenities.setter
    def amenities(self, obj):
        """Setter for handling appending ammenity id to ammenity_ids"""
        if isinstance(obj, models.amenity.Amenity):
            self.amenity_ids.append(obj.id)

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship('Review', backref=backref('place'))
        amenities = relationship('Amenity', secondary=place_amenity,
                                 viewonly=False)
