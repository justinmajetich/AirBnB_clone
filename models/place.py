#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship

place_amenity = Table('place_amenity', Base.metadata,
                        Column('place_id', String(60),
                            ForeignKey('places.id'),
                            primary_key=True, nullable=False),
                        Column('amenity_id', String(60),
                                ForeignKey('amenities.id'),
                                primary_key=True, nullable=False))

class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'),nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    reviews = relationship("Review", cascade="all, delete", backref='place')
    amenities = relationship("Amenity", secondary=place_amenity, viewonly=False)

    @property
    def reviews(self):
        """method reviews"""
        from models import storage #NEW
        from models.review import Review #NEW
        temp = [] #NEW
        dictio = storage.all(Review) #NEW
        for value in dictio.values(): #NEW
            if value.place_id == self.id: #NEW
                temp.append(value) #NEW
        return temp #NEW

    @property
    def amenities(self):
        from models import storage #NEW
        from models.amenity import Amenity #NEW
        temp = [] #NEW
        dictio = storage.all(Amenity) #NEW
        for value in dictio.values(): #NEW
            if value.id == self.id: #NEW NEW2 hhhhhhhhh
                temp.append(value) #NEW
        return temp #NEW

    @amenities.setter
    def amenities(self, value):
        from models.amenity import Amenity
        if isinstance(value, Amenity):
            self.amenity_ids.append(value.id)
