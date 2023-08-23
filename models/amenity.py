#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models import storage_type
from sqlalchemy import Column, String
from models.place import place_amenity
from sqlalchemy.orm import relationship
from uuid import uuid4


class Amenity(BaseModel, Base):
    __tablename__ = 'amenities'
    if storage_type == 'db':
        name = Column(String(128), nullable=False)
        place_amenities = relationship('Place', secondary=place_amenity)

        def __init__(self, **kwargs):
            self.id = str(uuid4())
            for key, value in kwargs.items():
                setattr(self, key, value)
    else:
        name = ''
