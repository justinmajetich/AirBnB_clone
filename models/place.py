#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from models.review import Review
from models.amenity import Amenity


place_amenity = Table("place_amenity", Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True, nullable=False))

class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
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
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """This method happens as soon as a instance is created"""
        super().__init__(*args, **kwargs)

    reviews = relationship("Review", cascade="all, delete", backref="place")
    amenities = relationship("Amenity", secondary=place_amenity,
                                  viewonly=False, backref='place_amenities')

    @property
    def reviews(self):
        """Getter attribute that returns the list of Reviews"""
        from models import storage
        reviews_list = []
        for review in storage.all(Review).values():
            if review.place_id == self.id:
                reviews_list.append(review)
        return reviews_list

    @property
    def amenities(self):
        """getter for the linked amenities"""
        from models import storage
        ame_list = []
        for amenity in list(storage.all(Amenity).values()):
            if amenity.id in self.amenity_ids:
                ame_list.append(amenity)
        return ame_list

    @amenities.setter
    def amenities(self, value):
        if type(value) == Amenity:
            self.amenity_ids.append(value.id)