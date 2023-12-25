#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from models.review import Review
from models import storage
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)
    number_rooms = Column(Integer(), default=0, nullable=False)
    number_bathrooms = Column(Integer(), default=0, nullable=False)
    max_guest = Column(Integer(), default=0, nullable=False)
    price_by_night = Column(Integer(), default=0, nullable=False)
    latitude = Column(Float(), nullable=False)
    longitude = Column(Float(), nullable=False)
    reviews = relationship(Review, cascade="all, delete", backref='place')
    amenity_ids = []

    @property
    def reviews(self):
        """
        getter attribute reviews that returns the list of Review instances
        with place_id equals to the current Place.id =>
        It will be the FileStorage relationship between Place and Review
        """
        instances = []
        for obj in storage.all(Review).values():
            if obj.place_id == self.id:
                instances.append(obj)
        return instances
