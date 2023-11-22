#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from base_model import BaseModel, Base


class Review(BaseModel, Base):
    """ Review classto store review information """
    __tablename__ = 'reviews'
    place_id = Column(String(1024), nullable=False, ForeignKey('places.id'))
    user_id = Column(String(60), nullable= False, ForeignKey('users.id'))
    text = Column(String(60), nullable=False)
