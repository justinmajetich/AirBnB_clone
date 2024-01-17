#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
import models
from sqlalchemy import Column, String, ForeignKey

class Review(BaseModel, Base):
    """Class to store reviews"""
    if models.storage == "db":
        __tablename__ = "reviews"
        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    
    
    place_id = ""
    user_id = ""
    text = ""
