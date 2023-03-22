#!/usr/bin/python3
""" Review module for the HBNB project """
from typing import Optional
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, DateTime, TIMESTAMP, text, ForeignKey

class Review(BaseModel, Base):
    """ Review classto store review information """

    __tablename__  = "review"

    place_id = Column(String(60), ForeignKey("place.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("user.id"), nullable=False)
    text  = Column(String, nullable=False)
