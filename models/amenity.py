#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import Mapped
from sqlalchemy import Column, Integer, String, DateTime, TIMESTAMP, text, Float
from sqlalchemy import String, ForeignKey


class Amenity(BaseModel, Base):
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
