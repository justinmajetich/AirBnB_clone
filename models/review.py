#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, VARCHAR, ForeignKey


class Review(BaseModel, Base):
    """ Review classto store review information """
    __tablename__ = 'reviews'
    place_id = Column(VARCHAR(60), ForeignKey("places.id"), nullable=False)
    user_id = Column(VARCHAR(60), ForeignKey("users.id"), nullable=False)
    text = Column(VARCHAR(1024), nullable=False)
