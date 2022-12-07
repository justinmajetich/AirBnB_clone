#!/usr/bin/python3
"""This is the place class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship
from models.review import Review
from models.amenity import Amenity
import os


class Place(BaseModel, Base):
    """This is the class for Place
    """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    reviews = relationship("Review", cascade="all,delete", backref="place")
    _amenities = relationship('Amenity', secondary='place_amenity',
                              viewonly=False, back_populates="place_amenities")
    amenity_ids = []

    @property
    def reviews(self):
        """
        reviews getter
        """
        from models import storage
        rev = []
        all_reviews = storage.all(Review)
        for val in all_reviews.values():
            if val.place_id == self.id:
                rev.append(val)
        return rev

    @property
    def amenities(self):
        """
        Getter attribute amenities that returns the list of Amenity instances
        based on the attribute amenity_ids that contains all Amenity.id linked
        to the Place
        """

        return self._amenities

    @amenities.setter
    def amenities(self, value):
        """
        Setter attribute amenities that handles append method for adding an
        Amenity.id to the attribute amenity_ids. This method should accept only
        Amenity object, otherwise, do nothing.
        """
        if os.getenv('HBNB_TYPE_STORAGE') != 'db':
            try:
                if value.__class__.__name__ == "Amenity":
                    self.amenity_ids.append(value.id)
            except Exception:
                pass
            from models import storage
            all_amenities = storage.all(Amenity)
            linked_amenities = []
            for value in all_amenities.values():
                if value.id in self.amenity_ids:
                    linked_amenities.append(value)
            self._amenities = linked_amenities
