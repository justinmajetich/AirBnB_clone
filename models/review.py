#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey


class Review(BaseModel, Base):
    """Review class to store review information

    Attributes:
        __tablename__ (str): represents the table name in the database
        text (str): a colomn containing review
        place_id (str): a foreign key to connect review to a place
        user_id (str): a foreign key to connect a review to a user
    """

    __tablename__ = "reviews"
    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
