#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from os import getenv

place_amenity = Table("place_amenity", Base.metadata,
                     Column("place_id", String(60), ForeignKey("places.id"), primary_key=True, nullable=False),
                     Column("amenity_id", String(60), ForeignKey("amenity.id"), primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """

    storgae = getenv("HBNB_TYPE_STORAGE")

    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []

    if storgae == "db":
        reviews = relationship("Review", backref="user", cascade="delete")
        amenities = relationship("Amenity", secondary="place_amenity", viewonly=False)

    if storgae == "fs":
        
        @property
        def reviews(self):
            from models import storage
            review_list = []
            for review in list(storage.all().values()):
                if review.place_id == self.id:
                    review_list.append(review)
            return review_list

        @property
        def amenities(self):
            from models import storage
            amenity_list = []
            for amenity in list(storage.all(Amenity).values()):
                if amenity.id in self.amenity_ids:
                    amenity_list.append(amenity)
            return amenity_list

        @amenities.setter
        def amenities(self, object):
            if isinstance(object, Amenity):
                self.amenity_ids.append(object.id)
