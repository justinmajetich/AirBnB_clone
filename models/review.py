#!/usr/bin/python3
""" Review module for the HBNB project """

import models
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from os import getenv


class Review(BaseModel, Base):
    """This is the class for Review

    Attributes:
        place_id, user_id, text
    """
    if getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = "reviews"
        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)

    else:
        place_id = ""
        user_id = ""
        text = ""

    def __init__(self, *args, **kwargs):
        """initialize Review"""
        super().__init__(*args, **kwargs)

