#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship
from os import getenv
from models.review import Review


place_amenity =  Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'),
                             primary_key=True,
                             nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True,
                             nullable=False))

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
        reviews = relationship('Review', backref='place', cascade='all, delete, delete-orphan')
        amenities = relationship("Amenity",
                                 secondary=place_amenity,
                                 back_populates='place_amenities',
                                 viewonly=False)

    else:
       @property
       def reviews(self):
        from models import storage
        li=[]
        for item in storage.all(Review).values():
            if item.place_id == self.id:
                li.append(item)
            return li
     
        @property
        def amenities(self):
            """getter"""
            from models import storage
            from models.amenity import Amenity
            ame = []
            moby = storage.all(Amenity)

            for amenity_inst in moby.values():
                if amenity_inst.id == self.amenity_id:
                    ame.append(amenity_inst)
            return ame

        @amenities.setter
        def amenities(self, amenity_list):
            """setter"""
            from models.amenity import Amenity
            for x in amenity_list:
                if type(x) == Amenity:
                    self.amenity_ids.append(x)