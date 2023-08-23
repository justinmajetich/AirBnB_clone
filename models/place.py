#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer, ForeignKey, Float, Table


class Place(BaseModel, Base):
    """ A place to stay """

    __tablename__ = "places"
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
    amenity_ids = []
    reviews = relationship("Review", backref='place', cascade="all, delete")

    @property
    def reviews(self):
        """
        Getter attribute to return the list of Review instances with
        place_id equals to the current Place.id
        """
        from models import storage
        my_obj = []
        extracted_reviews = storage.all('Review').values()
        for review in extracted_reviews:
            if self.id == review.place_id:
                review_obj.append(review)
        return my_obj

    @property
    def amenities(self):
        """
        Getter attrib that returns list based on amenity_ids
        """
        from models import storage
        my_obj = []
        extracted_amenities = storage.all('Amenity').values()
        for amenity in extracted_amenities:
            if self.id == amenity.amenity_ids:
                my_obj.append(amenity)
        return my_obj

    @amenities.setter
    def amenities(self, obj):
        """
        setter attrib to the amenity_ids attribute
        """
        if isinstance(obj, 'Amenity'):
            self.amenity_id.append(obj.id)
