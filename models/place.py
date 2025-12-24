#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from os import environ

storage_engine = environ.get("HBNB_TYPE_STORAGE")

place_amenity = Table(
    'place_amenity', Base.metadata,
    Column(
        'place_id',
        String(60),
        ForeignKey('places.id'),
        primary_key=True,
        nullable=False
    ),
    Column(
        'amenity_id',
        String(60),
        ForeignKey('amenities.id'),
        primary_key=True,
        nullable=False
    ),
)


class Place(BaseModel, Base):
    """A place to stay
    """
    __tablename__ = "places"
    if (storage_engine == "db"):
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
        amenity_ids = []
        amenities = relationship("Amenity",
                                 secondary=place_amenity,
                                 back_populates="places",
                                 viewonly=False)
        cities = relationship("City", back_populates="places")
        user = relationship("User", back_populates="places")
        reviews = relationship("Review",
                               cascade='all, delete, delete-orphan',
                               back_populates="place")
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0

        def __init__(self, *args, **kwargs):
            "Initialize place with amenity_ids"
            super().__init__(*args, **kwargs)
            self.amenity_ids = []

        @property
        def reviews(self):
            """
             - It is the FileStorage relationship between Place and Review.
             - Returns the list of Review instances with place_id equals to
             the current Place.id
            """
            from models import storage
            from models.review import Review

            review_list = []
            for review in storage.all(Review).values():
                if place_id == self.id:
                    review_list.append(review)
            return review_list

        @property
        def amenities(self):
            """
            Returns the list of Amenity instances based on the attribute
            amenity_ids that contains all Amenity.id linked to the Place
            """
            from models import storage
            from models.amenity import Amenity

            amenity_list = []
            for amenity in storage.all(Amenity).values():
                if amenity.id in self.amenity_ids:
                    amenity_list.append(amenity)
            return amenity_list

        @amenities.setter
        def amenities(obj, Amenity):
            """
            - Handles append method for adding an Amenity.id to the attribute
              amenity_ids.
            - Should accept only Amenity object, otherwise, do nothing
            """
            from models.amenity import Amenity

            if isinstance(obj, Amenity):
                if obj.id not in self.amenity_ids:
                    self.amenity_ids.append(obj.id)
