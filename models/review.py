#!/usr/bin/python3
""" Review module for the HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey


class Review(BaseModel, Base):
    """ Represents a Review, with its various parameters
    
    Inherits the BaseModel and Base(from sqlalchemy) and links to the mysql table reviews
    Attributes:
      __tablename__(str): name of the MySQL table
      text(sqlalchemy String): Review text
      place_id(sqlalchemy String): id for the place being reviewed
      user_id(sqlalchemy String): id for the user writing the  review
    """

    if models.storage_type == "db":
        __tablename__ = "reviews"
        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    else:
        def __init__(self, place_id = "", user_id = "", text = ""):
            """ If storage is not db (FileStorage) instantiate the values """
            self.place_id = place_id
            self.user_id = user_id
            self.text = text
            super().__init__()
