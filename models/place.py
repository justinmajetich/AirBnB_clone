#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship
from models.review import Review
from models.amenity import Amenity
from os import getenv


association_table = Table(
    "place_amenity",
    Base.metadata,
    Column("place_id", String(60), ForeignKey("places.id"), primary_key=True,
           onupdate='CASCADE', nullable=False),
    Column("amenity_id", String(60), ForeignKey("amenities.id"),
           primary_key=True, onupdate='CASCADE', nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)

    amenity_ids = []

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship('Review', backref='places', cascade='delete')
        amenities = relationship('Amenity', secondary='place_amenity',
                                 viewonly=False)
    else:

        @property
        def reviews(self):
            """Returns list of reviews associated with place"""
            from models import storage
            my_list = []
            for i in storage.all(Review):
                if self.id == i.place_id:
                    my_list.append(i)
            return my_list

        @property
        def amenities(self):
            """Returns list of amenities associated with place"""
            from models import storage
            my_list = []
            for i in storage.all(Amenity).values():
                if i.id in self.amenity_ids:
                    my_list.append(i)
            return my_list

        @amenities.setter
        def amenities(self, value):
            if type(value) == Amenity:
                self.amenity_ids.append(value.id)
