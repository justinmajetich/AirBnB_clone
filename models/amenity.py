#!/usr/bin/python3
""" State Module for HBNB project """
# KASPER edited 1:45pm 10/28/2023
from models.base_model import BaseModel, Base
from sqlalchemy import (
    Column,
    String
)


class Amenity(BaseModel, Base):
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    # place_amenities = ""  update in task 10
