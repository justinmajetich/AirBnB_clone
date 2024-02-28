# #!/usr/bin/python3

""" Place Module for HBNB project """
from .amenity import Amenity
from sqlalchemy import Column, String, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship
import os
from models.base_model import BaseModel, Base

storage_type = os.getenv('HBNB_TYPE_STORAGE')


class Place(BaseModel, Base):
     """ A place to stay """
     __tablename__ = 'places'

     if storage_type == 'db':
          city_id = Column('city_id', String(60), ForeignKey('cities.id'), nullable=False)
          user_id = Column('user_id', String(60), ForeignKey('users.id'), nullable=False)
          name = Column('name', String(128), nullable=False)
          description = Column('description', String(1024))
          number_rooms = Column('number_rooms', Integer, nullable=False, default=0)
          number_bathrooms = Column('number_bathrooms', Integer, nullable=False, default=0)
          max_guest = Column('max_guest', Integer, nullable=False, default=0)
          price_by_night = Column('price_by_night', Integer, nullable=False, default=0)
          latitude = Column('latitude', Float)
          longitude = Column('longitude', Float)
          amenity_ids = []

          reviews = relationship('Review', backref='place', cascade='all, delete')
          city = relationship('City', backref='places')

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
          """Getter that returns the list of Amenity instances based on amenity_ids"""
          return [review for review in self.reviews if review.place_id == self.id]   

     @property
     def amenities(self):
          return [amenity for amenity in self.amenities if amenity.place_id == self.id]

     @amenities.setter
     def amenities(self, value):
          """Setter that handles append method for adding an Amenity.id to amenity_ids"""
          if isinstance(value, Amenity):
               self.amenity_ids.append(value.id)
