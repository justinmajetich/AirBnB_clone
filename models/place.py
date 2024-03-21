#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy import Column, String, ForeignKey, Table
from sqlalchemy.orm import relationship
# from models.review import Review
from os import getenv


metadata = Base.metadata
place_amenity = Table('user', metadata,
    Column('place_id', String(60), ForeignKey('places.id'), nullable=False, primary_key=True),
    Column('amenity_id', String(60), ForeignKey('amenities.id'), nullable=False, primary_key=True),
)

class Place(BaseModel, Base):
    """ The Place class, contains infor about a BnBs"""
    __tablename__ = 'places'


    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, default=0)
    longitude = Column(Float, default=0)
    amenities = []
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship("Review", backref='place',
                            cascade='all, delete, delete-orphan')
        amenities = relationship("Amenity", secondary=place_amenity, viewonly=False,  overlaps="amenities")
    else:
        @property
        def reviews(self):
            """Gets reviews from FileStorage"""
            from models import storage
            from models.review import Review

            review_list = []
            for review in list(storage.all(Review).values()):
                if review.place_id == self.id:
                    review_list.append(review)
            return review_list
        
        @property
        def amenities(self):
            """Getter attribute amenities that returns the list of Amenity instances"""
            from models import storage
            from models.amenity import Amenity

            return [amenity for amenity in storage.all(Amenity).values() if amenity.place_id == self.id]

        @amenities.setter
        def amenities(self, value):
            from models.amenity import Amenity
            """Setter attribute amenities that handles append method for adding an Amenity.id"""
            if isinstance(value, Amenity):
                self.amenity_ids.append(value.id)