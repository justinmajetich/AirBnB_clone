#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column, Integer, ForeignKey, Float, Table
from sqlalchemy.orm import relationship


place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey('places.id'),
                             nullable=False, primary_key=True),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             nullable=False, primary_key=True))

class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    number_rooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    reviews = relationship("Review", cascade="all, delete", backref="place")
    amenities = relationship("Amenity", secondary=place_amenity,
                             viewonly=False)

    @property
    def reviews(self):
        """Returns a list of reviews with matching place id """
        from models import Review
        from models import storage
        reviews = storage.all(Review)
        all_reviews = [review for review in reviews.values()
                       if review.place_id == self.id]
        return all_reviews

    @property
    def amenities(self):
        """Returns a list of amenities with matching place id"""
        from models import Amenity
        from models import storage
        return self.amenity_ids

    @amenities.setter
    def amenities(self, obj=None):
        """Returns a list of amenities with matching place id"""
        from models import Amenity
        from models import storage
        if type(obj) == Amenity:
           self.amenity_ids.append(obj.id)
