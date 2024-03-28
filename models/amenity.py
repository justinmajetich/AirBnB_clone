#!/usr/bin/python3
# models/place.py
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String, Table, ForeignKey
from sqlalchemy.orm import relationship

# Association table for the Many-To-Many relationship between Place and Amenity
place_amenity = Table('place_amenity', Base.metadata,
    Column('place_id', String(60), ForeignKey('places.id'), primary_key=True, nullable=False),
    Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True, nullable=False)
)

class Place(BaseModel, Base):
    __tablename__ = 'places'
    # Existing Place model attributes
    amenities = relationship("Amenity", secondary=place_amenity, viewonly=False)
    # Ensure other Place class attributes and relationships are included here

# Amend models/amenity.py as needed based on the original instruction for Amenity updates
