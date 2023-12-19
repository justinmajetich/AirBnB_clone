#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, Table, ForeignKey
from sqlalchemy.orm import relationship
import os

if os.getenv("HBNB_TYPE_STORAGE") == "db":
    place_amenity = Table(
            'place_amenity',
            Base.metadata,
            Column('place_id', String(60), ForeignKey('places.id'), primary_key=True, nullable=False),
            Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True, nullable=False)
            )


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"

    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        """__tablename__ = 'places'"""
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, default=0, nullable=False)
        number_bathrooms = Column(Integer, default=0, nullable=False)
        max_guest = Column(Integer, default=0, nullable=False)
        price_by_night = Column(Integer, default=0, nullable=False)
        latitude = Column(Float)
        longitude = Column(Float)
        amenity_ids = []
        reviews = relationship("Review", backref="place", cascade="all,\
                               delete-orphan")
        amenities = relationship(
                "Amenity",
                secondary=place_amenity,
                viewonly=False
        )
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
        amenity_ids = []

    @property
    def reviews(self):
        reviews_list = []
        for review in models.storage.all(Review).values():
            if review.place_id == self.id:
                reviews_list.append(review)
        return reviews_list
    
    if os.getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def amenities(self):
            """ Getter attribute for amenities in FileStorage. """
            from models import storage, Amenity

            amenities_list = []
            for amenity_id in self.amenity_ids:
                amenityObj = models.storage.all().get("Amenity.{}"
                                                       .format(amenity_id))
                if amenityObj:
                    amenities_list.append(amenityObj)
            return amenities_list

        @amenities.setter
        def amenities(self, amenity):
            """Setter attribute for amenities in FileStorage."""
            if isinstance(amenity, Amenity):
                if amenity.id not in self.amenity_ids:
                    self.amenity_ids.append(amenity.id)
