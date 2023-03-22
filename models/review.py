#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey

Base = declarative_base()


class Review(BaseModel, Base):
    """ Review class to store review information """
    __tablename__ = 'reviews'
    user = relationship('User', back_populates='reviews')
    place = relationship('Place', back_populates='reviews')

    place_id = Column(String(60), ForeignKey(places.id), nullable=False)
    user_id = Column(String(60), ForeignKey(users.id), nullable=False)
    text = Column(String(1024), nullable=False)
