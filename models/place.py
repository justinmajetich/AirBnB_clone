#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship



place_amenity = Table('place_amenity', Base.metadata,
    Column('place_id', String(60), ForeignKey('places.id'), nullable=False, primary_key=True),        
    Column('amenity_id', String(60), ForeignKey('amenities.id'), nullable=False, primary_key=True)    
)

class Place(BaseModel, Base):
    """ A place to stay """

    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    reviews = relationship("Review", backref="place",
                           cascade="all, delete, delete-orphan")
    _amenities = relationship("Amenity", backref="amenities", overlaps="_amenities", secondary=place_amenity, viewonly=False)
    amenity_id = ''
    
    @property
    def reviews(self):
        """Returns the list of Review instances from current place"""
        from models import storage
        all_reviews = storage.all(BaseModel.Review)
        return [review for review in all_reviews.values()
                if review.place_id == self.id]
    
    @property
    def amenities(self):
        """returns the list of amenity instances from current place"""
        from models import storage
        from models.amenity import Amenity
        import os
        if os.getenv("HBNB_MYSQL_DB") == 'db':
            pass
        else:
            list = []
            for id in self.amenity_id:
                for key in storage.all().keys():
                    if id == key.split('.')[1]:
                        list.append(storage.all()[key])
            return list

            # all_amenities = storage.all(Amenity)
            # self.amenity_ids = [amenity for amenity in all_amenities.values()
            #         if place_amenity.place_id == self.id]
            # return self.amenity_ids
    
    @amenities.setter
    def amenities(self, value):
        """sets value of amenity property"""
        from models.amenity import Amenity
        #  if value.__class__.__name__ == "Amenity":
        print("The setter has run")
        self.amenity_id = []
        if isinstance(value, Amenity):
            self.amenity_id.append(value.id) 
