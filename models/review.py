#!/usr/bin/python3
""" Review module for the HBNB project """
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship

from models.base_model import Base, BaseModel


class Review(BaseModel, Base):
    """ Review class to store review information """
    __tablename__ = 'reviews'
    text = Column(String(1024), nullable=False)
    user_id = Column(String(60), ForeignKey('places.id'), nullable=False)
    place_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    user = relationship('User', back_populates='reviews', cascade='all, delete-orphan', single_parent=True)
    place = relationship('Place', back_populates='reviews', cascade='all, delete-orphan', single_parent=True)
