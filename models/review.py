#!/usr/bin/python3
""" This module defines the class Review """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey


class Review(BaseModel, Base):
    """ Represents a Review for a MySQL database

    Public class attributes (with sqlalchemy):

        __tablename__ (str): Name of MySQL table to store Reviews.

        text (Column: String): The review description.
        place_id (Column: String): Foreign key to 'places.id'.
        user_id (Column: String): Foreign key to 'users.id'.
    """
    __tablename__ = "reviews"

    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
