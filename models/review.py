#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship


class Review(BaseModel, Base):
    """ Review classto store review information """
    __tablename__ = "reviews"
    place_id = Column('place_id', String(60),
                      ForeignKey("places.id"), nullable=False)
    user_id = Column('user_id', String(60),
                     ForeignKey("users.id"), nullable=False)
    text = Column('text', String(1024), nullable=False)
