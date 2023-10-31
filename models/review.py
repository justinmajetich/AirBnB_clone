#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Review(BaseModel, Base):
    """Review class to store review information"""
    __tablename__ = 'reviews'  # Table name as specified

    place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    text = Column(String(1024), nullable=False)

    # Define the relationships
    user = relationship('User', back_populates='reviews')  # Assuming a 'User' model exists with 'reviews' relationship
    place = relationship('Place', back_populates='reviews')  # Assuming a 'Place' model exists with 'reviews' relationship

