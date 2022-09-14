#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from models.review import Review
from models.amenity import Amenity
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from os import getenv
from sqlalchemy.orm import relationship
from models import storage

place_amenity = Table("place_amenity", Base.metadata,
                      Column("place_id", String(60),
                             ForeignKey("places.id"),
                             nullable=False, primary_key=True),
                      Column("amenity_id", String(60),
                             ForeignKey("amenities.id"),
                             nullable=False, primary_key=True))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id', ondelete="CASCADE"),
                     nullable=False)
    user_id = Column(String(60), ForeignKey('users.id', ondelete="CASCADE"),
                     nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship("Review", backref="place",
                               cascade="all, delete", passive_deletes=True)

    else:
        @property
        def reviews(self):
            """returns the list of Review"""
            new_list = []
            all_review = storage.all(Review)
            for element in all_review.values():
                if self.id == element.place_id:
                    new_list.append(element)
            return new_list

    if getenv("HBNB_TYPE_STORAGE") == "db":
        amenities = relationship("Amenity", viewonly=False,
                                 secondary=place_amenity,
                                 backref="place_amenities")

    else:
        @property
        def amenities(self):
            """returns the list of amenities
            """
            new_list = []
            all_ami = storage.all(Amenity)
            for element in all_ami.values():
                if self.id == element.place_id:
                    new_list.append(element)
            return new_list

        @amenities.setter
        def amenities(self, cls):
            if not isinstance(cls, Amenity):
                return
            self.amenity_ids.append(cls.id)
