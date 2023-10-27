#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """ represents amenity"""
    __tablename__ = 'amenities'
    name = Column(
        String(128), nullable=False
    ) if getenv('HBNB_TYPE_STORAGE') == 'db' else ''
