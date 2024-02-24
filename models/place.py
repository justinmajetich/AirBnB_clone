#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Table
from sqlalchemy.orm import relationship
import models
from models.review import Review

if models.env_stroage == 'db':
    place_amenity = Table(
        "place_amenity",
        Base.metadata,
        Column('place_id', String(60), ForeignKey('places.id'),
               nullable=False, primary_key=True),
        Column('amenity_id', String(60), ForeignKey('amenities.id'),
               nullable=False, primary_key=True),
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
        amenity_ids = []
        city = relationship('City', back_populates='places')
        user = relationship("User", back_populates="places",
                            cascade="all, delete, save-update")
        reviews = relationship('Review', backref='place',
                               cascade="all, delete, save-update")
        amenities = relationship('Amenity', secondary=place_amenity)

else:
    class Place(BaseModel):
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

        @property
        def reviews(self):
            """
            for FileStorage: getter attribute reviews
            that returns the list of Review instances
            """
            allReviews = models.storage.all(Review)
            return [review for review in allReviews
                    if review.place_id == self.id]

        @property
        def amenities(self):
            """
            Getter attribute amenities that returns the list of Amenity
            instances based on the attribute amenity_ids
            that contains all Amenity.id linked to the Place
            """
            listDesiredObjs = []
            dictAllobjs = models.storage.all('Amenity').values()
            for obj in dictAllobjs:
                if obj.id in self.amenity_ids:
                    listDesiredObjs.append(obj)
            return listDesiredObjs

        @amenities.setter
        def amenities(self, obj):
            from models import Amenity
            """
            Setter attribute amenities
            """
            if isinstance(obj, Amenity):
                if obj.place_id == self.id:
                    self.amenity_ids.append(obj.id)
