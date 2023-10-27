#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship


class Review(BaseModel, Base):
    """ Review classto store review information

    Inherits from SQLAlchemy Base and links to the reviews table

    Attributes:
        __tablename__ (str): The name to use.
        text (sqlalchemy String): The review description.
        place_id (sqlalchemy String): The review's place ID.
        user_id (sqlalchemy String): Te review's user id.
    """
    __tablename__ = "reviews"
    place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    text = Column(String(1024), nullable=False)
