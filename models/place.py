#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Table, Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship, backref
from models import storage
from models.amenity import Amenity

class Place(BaseModel, Base):
    """ The Place class """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []

    reviews = relationship("Review", backref="place", cascade="all, delete")
    amenities = relationship('Amenity', secondary='place_amenity',viewonly=False)
    
    if getenv('HBNB_TYPE_STORAGE') != 'db': 
        @property
        def reviews(self):
            my_list = {}
            all_review = self.reviews
            for rev in all_review:
                if self.id == rev.id:
                    my_list.append(rev)
            return my_list

        @property
        def amenities(self):
            """getter amenity that returns the list of Amenity"""
            my_list = {}
            all_amenities = self.amenities
            for ament in all_amenities:
                if self.id = ament.id:
                    my_list.append(ament)
            return(my_list)
        
        @amenities.setter
        def amenities(sef, obj=None):
            """Setter amenities"""
            self.amenities.append(obj.id)

            
    
    place_amenity = Table('place_amenity', metadata = Base.metadata,
    Column('place_id', String(60), ForeignKey('places.id'), nullable=False),
    Column('amenity_id', String(60), ForeignKey('amenity.id'), nullable=False))