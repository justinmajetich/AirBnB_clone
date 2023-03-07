#!/usr/bin/python3
"""Review class for AirBnb project"""
from models.base_model import Base, BaseModel
from sqlalchemy import Column, ForeignKey, String


class Review(BaseModel, Base):
    """Review class that creates reviews table"""
    __tablename__ = 'reviews'
    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)