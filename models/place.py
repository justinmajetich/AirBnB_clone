#!/usr/bin/python3
""" Place Module for HBNB project """
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.review import Review
from models.amenity import Amenity


place_amenity = Table('place_amenity', Base.metadata,
    Column('place_id', String(60), ForeignKey('places.id'), primary_key=True, nullable=False),
    Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True, nullable=False)                      
)

class Place(BaseModel, Base):
    """Place model for HBNB"""

    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=True)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    reviews = relationship("Review", backref="place", cascade="all, delete")
    place_amenities = relationship("Amenity", secondary=place_amenity, backref="places")
    amenities = relationship("Amenity", secondary=place_amenity, backref="places", viewonly=False)

    
    @property
    def reviews(self):
        """Getter for reviews"""
        from models.review import Review
        return [review for review in Review.all() if review.place_id == self.id]

     @property
    def amenities(self):
        """Getter for amenities"""
        return [Amenity.all()[id] for id in self.amenity_ids]

    @amenities.setter
    def amenities(self, value):
        """Setter for amenities"""
        if isinstance(value, Amenity):
            self.amenity_ids.append(value.id)