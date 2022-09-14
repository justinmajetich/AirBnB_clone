#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel
import models
from sqlalchemy import (
    Column,
    String,
    ForeignKey
)


class Review(BaseModel):
    """ Review class to store review information """
    if models.storage_type == "db":
        __tablename__ = "reviews"
        text = Column(String(1024), nullable=False)
        place_id = Column(
            String(60), ForeignKey('places.id '),
            nullable=False, ondelete="CASCADE")
        user_id = Column(
            String(60), ForeignKey('users.id '),
            nullable=False, ondelete="CASCADE")
    else:
        place_id = ""
        user_id = ""
        text = ""
