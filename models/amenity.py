#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
import models
from models.base_model import Base, BaseModel
import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class Amenity(BaseModel):
    name = ""
