#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Review(BaseModel, Base):
    """ Review class to store review information """
    place_id = ""
    user_id = ""
    text = ""

    __tablename__ = "reviews"
    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    user = relationship("User", cascade="all, delete-orphan")
    place = relationship("Place", cascade="all, delete-orphan")

    def __init__(self, *args, **kwargs):
        """ Constructor method to initialize user instances
        Args:
            args: list of arguments
        kwargs:
            key/value dictionary of arguments
        """
        super().__init__(args, kwargs)
