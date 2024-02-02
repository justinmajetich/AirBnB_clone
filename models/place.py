#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from models import storage_t, storage
from sqlalchemy import Column, String, Integer, Float, Table, ForeignKey
from sqlalchemy.orm import relationship
from models.review import Review
from models.amenity import Amenity


if storage_t == "db":
    place_amenity = Table('place_amenity', Base.metadata,
                          Column('place_id', String(60),
                                 ForeignKey('places.id', ondelete="CASCADE",
                                            onupdate="CASCADE"),
                                 primary_key=True),
                          Column('amenity_id', String(60),
                                 ForeignKey('amenities.id', ondelete="CASCADE",
                                            onupdate="CASCADE"),
                                 primary_key=True))


class Place(BaseModel, Base):
    """ A place to stay """
    if storage_t == "db":
        __tablename__ = 'places'
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024))
        number_rooms = Column(Integer, default=0, nullable=False)
        number_bathrooms = Column(Integer, default=0, nullable=False)
        max_guest = Column(Integer, default=0, nullable=False)
        price_by_night = Column(Integer, default=0, nullable=False)
        latitude = Column(Float)
        longitude = Column(Float)
        reviews = relationship('Review', backref='place')
        amenities = relationship('Amenity', secondary='place_amenity',
                                 backref='place_amenities',
                                 viewonly=False)

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
        my_list = [review for review in storage.all(Review).values()
                   if review.place_id == self.id]
        return my_list

    @property
    def amenities(self):
        my_list = [amenity for amenity in storage.all(Amenity).values()
                   if amenity.place_id == self.id]
        return my_list
