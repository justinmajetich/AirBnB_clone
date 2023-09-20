#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey, Table
from models.base_model import Base


class Amenity(BaseModel, Base):
    """Amenity  class
    Attributes:
        name (str): Amenity  name
    """

    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)

    def __init__(self, *args, **kwargs):
        """User class init
        """
        super().__init__(*args, **kwargs)
