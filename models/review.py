#!/usr/bin/python3
""" Review module for the HBNB project """
from sqlalchemy import Column
from models.base_model import BaseModel, Base
from sqlalchemy import String, ForeignKey


class Review(BaseModel, Base):
    """ Review classto store review information """

    __tablename__ = "reviews"

    place_id = Column(String(60), ForeignKey(
        "places.id", ondelete='CASCADE'), nullable=False)
    user_id = Column(String(60), ForeignKey(
        "users.id", ondelete='CASCADE'), nullable=False)
    text = Column(String(1024), nullable=False)
