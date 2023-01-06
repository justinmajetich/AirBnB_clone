#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base

from sqlalchemy import MetaData, Column, String, Integer, Float, ForeignKey
from sqlalchemy import Table
from sqlalchemy.orm import relationship


# define a many-to-many relationship table (Place and Amenity)
place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey(
                          'places.id'), primary_key=True, nullable=False),
                      Column('amenity_id', String(60), ForeignKey(
                          'amenities.id'), primary_key=True, nullable=False)
                      )


class Place(BaseModel, Base):
    """ A place to stay """
    # define schema: name and properties/fields
    __tablename__ = 'places'
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
    reviews = relationship("Review", backref="place",
                           cascade="all, delete, delete-orphan")
    amenities = relationship("Amenity", backref="place_amenities",
                             cascade="all, delete, delete-orphan",
                             secondary=place_amenity, viewonly=False)

    amenity_ids = []

    @property
    def reviews(self):
        """ getter attribute that returns the list of Review instances
        with place_id = current Place.id (self.id). This' the FileStorage
        relationship between Place and Review """
        # get all reviews and filter by self.id
        reviews = models.storage.all(Review)
        my_reviews = []
        for key, val in reviews.items():
            if self.id == val['place_id']:
                my_reviews.append = str(reviews[key])
        return my_reviews

    @property
    def amenities(self):
        """ getter attribute that returns the list of Amenity instances
        based on the attribute amenity_ids that contains all Amenity.id
        linked to the Place (this i.e. self.id) """
        # get all amenities and filter by self.id
        amenities = models.storage.all(Amenity)
        my_amenities = []
        for key, val in amenities.items():
            # id amenity id in amenity_ids, add to my_amenities
            if key.partition('.')[2].strip() in amenity_ids:
                my_amenities.append = str(amenities[key])
        return my_amenities

    @amenities.setter
    def amenities(self, obj):
        """ setter attribute: adds an Amenity.id to the attribute amenity_ids.
        Args:
            obj - the Amenity instance whose id to add to amenity_ids list """
        # check that object is an Amenity instance
        if obj.__class__.__name__ is Amenity:
            amenity_ids.append(obj.id)
