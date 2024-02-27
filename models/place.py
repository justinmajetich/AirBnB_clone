# #!/usr/bin/python3

""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from .review import Review
from .amenity import Amenity
from .place_amenities import place_amenity
from sqlalchemy import Column, String, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship



class Place(BaseModel, Base):
     """ A place to stay """
     __tablename__ = 'places'
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

     reviews = relationship('Review', back_populates='place', cascade='all, delete-orphan')
     user = relationship('User', back_populates='places')
     amenities = relationship('Amenity', secondary=place_amenity, back_populates='places', viewonly=False)

     # @property
     # def reviews(self):
     #      """Getter that returns the list of Amenity instances based on amenity_ids"""
     #      return [review for review in self.reviews if review.place_id == self.id]    

     # @amenities.setter
     # def amenities(self, value):
     #      """Setter that handles append method for adding an Amenity.id to amenity_ids"""
     #      if isinstance(value, Amenity):
     #           self.amenity_ids.append(value.id)
