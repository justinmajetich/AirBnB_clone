#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from sqlalchemy import Table, Float, ForeignKey
from models.review import Review
from models.amenity import Amenity


place_amenity = Table('place_amenity', Base.metadata,
        Column('place_id', String(60), ForeignKey('places.id'),
                primary_key=True, nullable=False),
        Column('amenity_id', String(60), ForeignKey('amanities.id'),
                primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=False)
    longitude =  Column(Float, nullable=False)
    reviews = relationship('Review', backref='place', cascade='all, delete')
    amenity_ids = []

    @property
    def reviews(self):
        list_review = []
        for review in list(models.storage.all(Review).values):
            if review.place_id == self.id:
                list_review.append(review)
        return list_review

    @property
    def amenities(self):
        """returns the list of Amenity instances based on the attribute
            amenity_ids that contains all Amenity.id linked to the Place
        """
        list_amenity = []
        for amenity in list(model.storage.all(Amenity).values):
            if amenity.id == self.amenity_ids:
                list_amenity.append(amenity)
        return list_amenity

    @amenities.setter
    def amenities(self, value):
        """returns the list of Amenity instances based on the attribute
            amenity_ids that contains all Amenity.id linked to the Place
        """
        if type(value) == Ameity:
            self.amenity_ids.append(value.id)
