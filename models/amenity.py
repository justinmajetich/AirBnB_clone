#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from os import getenv
from sqlalchemy.orm import relationship

type_storage = getenv('HBNB_TYPE_STORAGE')


class Amenity(BaseModel, Base):
    __tablename__ = 'amenities'
    if type_storage == 'db':
        name = Column(String(128), nullable=False)
        place_amenities = relationship('Place', secondary='place_amenity',
                                       viewonly=False)
    else:
        name = ""
