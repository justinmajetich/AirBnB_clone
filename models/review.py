#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base

from sqlalchemy import MetaData, Column, String, ForeignKey


class Review(BaseModel, Base):
    """ Review classto store review information """
    # define the schema: name and fields
    __tablename__ = "reviews"
    place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    text = Column(String(1024), nullable=False)
