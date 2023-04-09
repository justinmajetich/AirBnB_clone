#!/usr/bin/python3
""" Place Module for HBNB project """
import os
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base

storage_type = os.getenv("HBNB_ENV")
# INTERMIDATE TABLE
intermidiate_table = Table("place_amenity", Base.metadata, Column("place_id", String(60), ForeignKey("places.id"), nullable=False), Column("amenity_id", String(60), ForeignKey("amenities.id"), nullable=False))

class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(60), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    if storage_type == "db":
        reviews = relationship("Review", backref="place")
        amenities = relationship("Amenity", secondary=intermidiate_table, viewonly=False)
    else:
       from models.review import Review
       from models.engine.file_storage import FileStorage
       storage = FileStorage()
       review_objs = storage.all(Review)
       reviews = []
       for obj in review_objs:
           if self.id == obj.place_id:
               reviews.append[obj]

       @property
       def reviews(self):
           return self.reviews

       @property
       def amenities(self):
           return self.amenity_ids

       @amenities.setter
       def amenities(self, obj):
           """ Setter for amenities """
           self.amenity_ids = []
           cls = obj.__class__.__name__
           if cls == "Amenity":
               self.amenity.append(obj)
