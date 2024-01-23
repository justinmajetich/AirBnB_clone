#!/usr/bin/python3
"""This is the kind of amenities"""
import models
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from models.place import place_amenity
# from models.place import place_amenity


class Amenity(BaseModel, Base):
    """Esta es la clase de Amenity
    Atributos:
        name: nombre de entrada
    """
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    # place_amenities = relationship('Place', secondary='place_amenity')
