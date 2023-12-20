#!/usr/bin/python3
""" Place Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, INTEGER, String, ForeignKey, Table, Float
from sqlalchemy.orm import declarative_base, relationship   


#presentation of Many to Many DB 
place_amenity = Table('place_amenity', Base.metadata,
             Column('place_id', String(60), ForeignKey('places.id'),
                 primary_key=True, nullable=False),
             Column('amenity_id', String(60),
                 ForeignKey('amenities.id'),
                 primary_key=True, nullable=False)
             )


class Place(BaseModel, Base):
    """A class representing a place in the AirBnB clone application.

    Attributes:
        city_id (str): The ID of the city where the place is located.
        user_id (str): The ID of the user who owns the place.
        name (str): The name of the place.
        description (str): The description of the place.
        number_rooms (int): The number of rooms in the place.
        number_bathrooms (int): The number of bathrooms in the place.
        max_guest (int): The maximum number of guests allowed in the place.
        price_by_night (int): The price per night for the place.
        latitude (float): The latitude coordinate of the place.
        longitude (float): The longitude coordinate of the place.
        reviews (list): A list of reviews associated with the place.
        amenities (list): A list of amenities available in the place.
    """

    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(255), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(INTEGER, nullable=False, default=0)
    number_bathrooms = Column(INTEGER, nullable=False, default=0)
    max_guest = Column(INTEGER, nullable=False, default=0)
    price_by_night = Column(INTEGER, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)

    reviews = relationship('Review', cascade='all, delete',
                           backref='place')

    amenity_ids = []

    @property
    def reviews(self):
        """Getter method for the reviews associated with the place.

        Returns:
            list: A list of Review objects.

        """
        review_list = []
        review_dict = models.storage.all(models.Review)
        for review in models.storage.all(models.Review).values():
            if review.place_id == self.id:
                review_list.append(review)
        return review_list

    @property
    def amenities(self):
        """Getter method for the amenities available in the place.

        Returns:
            list: A list of Amenity objects.

        """
        return self.amenity_ids

    @amenities.setter
    def aminities(self, obj):
        """Setter method for adding an amenity to the place.

        Args:
            obj (Amenity): An Amenity object to be added.

        """
        if isinstance(obj, models.Amenity):
            self.amenity_ids.append(obj.id)
