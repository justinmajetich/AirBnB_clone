#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey, Float, PrimaryKey
from sqlalchemy.orm import relationship
from os import getenv

place_amenity = Table("place_amenity", Base.metadata, 
                               Column('place_id', ForeignKey('place.id'), String(60), 
                                      nullable=False, PrimaryKey=True),
                                Column('amenities_id', ForeignKey('amenities.id'), String(60), 
                                       nullable=False, PrimaryKey=True)
                                       ) 
class Place(BaseModel, Base):
    """ A place to stay """
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
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
    amenity_id = Column(String(60), ForeignKey('amenities.id'), nullable=False, PrimaryKey=True)
    
    if getenv("HBNB_TYPE_STORAGE") == "db":
        reviews =relationship("Review", cascade='all, delete, delete-orphan', backref="place")

        amenities = relationship("Amenity", secondary=place_amenity, 
                                 viewonly=False, back_populates="place_amenities")
    else:
        @property
        def reviews(self):
            """ returns the list of Review instances """
            reviews_list = []
            all_reviews = models.storage.all(Review)
            for review in all_reviews.values():
                if review.place_id == self.id:
                    reviews_list.append(review)
            return reviews_list
        @property
        def amenities(self):
            """returns the list of Amenity instances based on the attribute amenity_ids"""
            amenities_list = []
            all_amenities = models.storage.all(Amenity)
            for amenity in all_amenities.values():
                if amenity.place_id == self.id:
                    amenities_list.append(amenity)
            return amenities_list
        @amenities.setter
        def amenities(self, obj=None):
            """handles append method for adding an Amenity.id to the attribute amenity_ids"""
            if type(obj) is Amenity and obj.id not in self.amenity_ids:
                self.amenity_ids.append(obj.id)


    


