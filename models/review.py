#!/usr/bin/python3
"""
    contains review class to represent reviews
"""
from models.base_model import BaseModel, Base
from models.place import Place
from models.user import User
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.sql.schema import ForeignKey
from os import environ

storage_engine = environ.get("HBNB_TYPE_STORAGE")


class Review(BaseModel, Base):
    """
        Review class
    """
    if (storage_engine == 'db'):
        __tablename__ = "reviews"
        place_id = Column(String(60), ForeignKey("places.id"))
        user_id = Column(String(60), ForeignKey("users.id"))
        text = Column(String(1024), nullable=False)
        place = relationship("Place", back_populates="reviews")
    else:
        place_id = ""
        user_id = ""
        text = ""
