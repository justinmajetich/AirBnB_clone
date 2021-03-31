#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship

place_amenity = Table("place_amenity", Base.metadata,
                      Column("place_id", String(60),
                             ForeignKey("places.id"),
                             nullable=False, primary_key=True),
                      Column("amenity_id", String(60),
                             ForeignKey("amenities.id"),
                             nullable=False, primary_key=True)
                      )


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)

    amenity_ids = relationship("Amenity", secondary=place_amenity,
                             viewonly=False)
    reviews = relationship("Review", cascade="all, delete", backref="place")

    @property
    def reviews(self):
        """dictionary of reviews"""
        from models.__init__ import storage
        from models.review import Review

        new = {}
        for key, value in storage.all(Review).items():
            if value.to_dict()["place_id"] == self.id:
                new[key] = value
        return new

    @property
    def amenities(self):
        """amenities getter"""
        return self.amenity_ids

    @amenities.setter
    def amenities(self, obj):
        """amenities setter"""
        from models.amenity import Amenity
        if obj is type(Amenity):
            self.amenity_ids.append(obj.id)
