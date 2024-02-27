#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship


place_amenity = Table('place_amenity', Base.metadata,
    Column('place_id', String(60), ForeignKey('places.id'), primary_key=True, nullable=False),
    Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True, nullable=False)
)

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
    _reviews = relationship("Review", backref="place", cascade="all, delete, delete-orphan")
    _amenities = relationship("Amenity", secondary=place_amenity, back_populates="place_amenities", viewonly=False)

    @property
    def reviews(self):
        """Returns the list of Review instances for the current place"""
        from models import storage
        all_reviews = storage.all(BaseModel.Review)
        return [review for review in all_reviews.values() if review.place_id == self.id]

    @property
    def amenities(self):
        """Getter for amenities that are linked to this place."""
        from models import storage
        all_amenities = storage.all(BaseModel.Amenity)
        return [amenity for amenity in all_amenities.values() if amenity.id in self.amenity_ids]

    @amenities.setter
    def amenities(self, value):
        """Adds an amenity.id to the list of linked amenities if not already present."""
        if type(value) == BaseModel.Amenity and value.id not in self.amenity_ids:
            self.amenity_ids.append(value.id)
