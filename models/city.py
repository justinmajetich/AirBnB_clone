#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.place import Place
from models.review import Review

class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = "cities"

    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)

    #place = relationship('Place', back_ref='city', cascade="all, delete-orphan")
    review = relationship('Review', backref='city', cascade="all, delete-orphan")
