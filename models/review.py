#!/usr/bin/python3

"""
Module for the Review class.
"""

from models import *
from sqlalchemy import Column, String, ForeignKey


class Review(BaseModel, Base):
    """
    Class representing a review in the application.
    Inherits from BaseModel and Base.
    """
    __tablename__ = "reviews"
    place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    text = Column(String(1024), nullable=False)

    def __init__(self, *args, **kwargs):
        """
        Initializes a new Review instance.
        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        super().__init__(*args, **kwargs)
