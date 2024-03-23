#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship
from os import getenv


place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'), primary_key=True,
                             nullable=False)
                      )


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

    if getenv('HBNB_TYPE_STORAGE') == "db":
        reviews = relationship("Review", cascade="all, delete", backref="place")
        amenities = relatonship("Amenity", secondary=place_amenity, viewonly=False)

    else:
        @property
        def reviews(self):
            """ The FileStorage relationship """
            from models import storage
            from models.review import Review

            review_list = []
            review_dict = storage.all(Review)

            for review in review_dict.values():
                if review.place_id == self.id:
                    review_list.append(review)

            return review_list
        
        @property
        def amenities(self):
            """ Returns the list of Amenity instances based on 'amenity_ids' """
            from models import storage
            
            amenity_list = []
            amenitites = storage.all('Amenity').values()

            for amenity in amenitites:
                if self.id == amenity.amenity_ids:
                    amenity_list.append(amenity)

            return amenity_list
        
        @amenities.setter
        def amenitites(self, obj):
            """ Handles the append method for adding an Amenity.id
                to the attribute amenity_ids
            """
            if isinstance(obj, 'Amenity'):
                self.amenity_id.append(obj.id)