#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, FLOAT, ForeignKey, Table
from sqlalchemy.orm import relationship

class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"

    city_id = Column(String(60), ForeignKey(True), nullable=False)
    user_id = Column(String(60), ForeignKey(True), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(FLOAT, nullable=True)
    longitude = Column(FLOAT, nullable=True)

    user = relationship("User", back_populates="places")
    city = relationship("City", back_populates="places")

    place_amenities = Table("place_amenity", Base.metadata,
                        Column('place_id', String(60), ForeignKey('places.id'), primary_key=True, nullable=False),
                        Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True, nullable=False))
    amenity_ids = relationship("Amenity", secondary="place_amenity", viewonly=False)
