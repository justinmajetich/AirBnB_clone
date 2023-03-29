#!/usr/bin/python3
"""Place class for AirBnb project"""
import models
from os import getenv
from models.base_model import Base, BaseModel
from sqlalchemy import Column, ForeignKey, String, Integer, Float, Table
from sqlalchemy.orm import relationship

place_amenity = Table("place_amenity", Base.metadata, Column("place_id",
                      String(60), ForeignKey("places.id"), primary_key=True,
                      nullable=False),
                      Column("amenity_id", String(60),
                             ForeignKey("amenities.id"), primary_key=True,
                             nullable=False))


class Place(BaseModel, Base):
    """Place class that creates places table"""
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

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship("Review", cascade="all, delete-orphan",
                               backref='place')
        amenities = relationship("Amenity", secondary=place_amenity,
                                 backref="places", viewonly=False)
    else:
        @property
        def reviews(self):
            """"""
            reviewsList = []
            for review in models.storage.all(Review).values():
                if self.id == review.place_id:
                    reviewsList.append(models.storage.all(Review)[review])
            return reviewsList

        @property
        def amenities(self):
            amenityList = []
            for amenity in models.storage.all(Amenity).values():
                if self.id == amenity.place_id:
                    amenityList.append(models.storage.all(Amenity)[amenity])
            return amenityList

        @amenities.setter
        def amenities(self, amenity_object):
            if type(amenity_object).__name__ == "Amenity":
                self.amenity_ids.append(amenity_object.id)