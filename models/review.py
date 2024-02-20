#!/usr/bin/python3
"""
Review module for the HBNB project
"""

import os
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import Base, BaseModel

storage_type = os.getenv("HBNB_TYPE_STORAGE")


class Review(BaseModel, Base):
    """
    Review classto store review information

    Attributes:
      place_id (str)
      user_id (str)
      text (str)
    """
    __tablename__ = "reviews"

    place_id = ""
    user_id = ""
    text = ""

    if storage_type == "db":
        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
