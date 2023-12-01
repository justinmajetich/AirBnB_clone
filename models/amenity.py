#!/usr/bin/python3
"""
    State Module for HBNB project
    *Update 1/12/2023: added code to use db storage and associated imports
        part of question 10
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
import os


class Amenity(BaseModel, Base):
    __tablename__ = 'amenities'
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        place_amenity = Table(
            'place_amenity', Base.metadata,
            Column('place_id', String(60), ForeignKey('places.id'),
                   primary_key=True, nullable=False),
            Column('amenity_id', String(60), ForeignKey('amenities.id'),
                   primary_key=True, nullable=False)
        )
        name = Column(String(128), nullable=False)
        places = relationship('Place', secondary='place_amenity',
                              back_populates='amenities')
    else:
        name = ""
