#!/usr/bin/python3
""" State Module for HBNB project """
from re import X
from models.base_model import BaseModel
import os
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship

class Amenity(BaseModel):
    """
    creates the tables of amenities
    """
    __tablename__ = "amenities"
    name = Column(128), nullable = False
    #ideas
    #age = Column(Integer, default=1)
    #gender = Column(String(30), default='female')
    #name = ""
    #def __init__(self, *args, **kwargs):
    #super().__init__(*args, **kwargs)