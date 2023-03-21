#!/usr/bin/python3

""" Review module for the HBNB project """
from sqlalchemy import Column,  Integer, String, ForeignKey, Float
from models.base_model import BaseModel, Base


class Review(BaseModel, Base):
    """ Review class to map the reviews table"""
    __tablename__ = "reviews"
    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
