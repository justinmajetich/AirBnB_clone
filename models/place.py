#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
import models
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from os import getenv
from sqlalchemy.orm import relationship

if models.storage == "db":
    place_amenity = Table("place_amenity", Base.metadata,
                          Column("place_id", String(60),
                                 ForeignKey("places.id", onupdate= "cascade",
                                            ondelete= "cascade"),
                                primary_key=True),
                          Column("amenity_id", String(60),
                                 ForeignKey("amenities.id", onupdate= "cascade",
                                            ondelete= "cascade"),
                                primary_key=True))
class Place(BaseModel, Base):
    """ A place to stay """
    if models.storage == "db":
        __tablename__ = "places"
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=False)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=False)
        longitude = Column(Float, nullable=False)
        reviews = relationship("Review", backref="user")
        amenity_ids = []
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

    def __init__(self, *args, **kwargs):
        """initializes places"""
        super().__init__(*args, **kwargs)

    if models.storage != "db":
        @property
        def reviews(self):
            """getter attribute that returns list of reviews"""
            from models.review import Review
            review_list = []
            all_reviews =models.storage.all(Review)
            for review in all_reviews.values():
                if review.place_id == self.id:
                    review_list.append(review)
            return review_list
        
        @property
        def amenities(self):
            """getter attribute returns list of amenities"""
            from models.amenity import Amenity
            amenity_list = []
            all.amenities = models.storage.all(Amenity)
            for amenity in all.amenities.values():
                if amenity.place_id == self.id:
                    amenity_list.append(amenity)
            return amenity_list

