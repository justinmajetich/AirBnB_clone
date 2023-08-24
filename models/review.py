#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel
from models.base_model import BaseModel, Base
from sqlalchemy import column, String, Integer, Nullable, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv

class Review(BaseModel):
    """ Review classto store review information """
    _tablename__ = "reviews"
    if getenv("HBNB_TYPE_STORAGE") == "db":
        text = column(String(1024), nullable=False)
        place_id = column(String(60), ForeignKey("places.id"), nullable=False)
        user_id = column(String(60), ForeignKey("users.id"), nullable=False)
    else:
        place_id = ""
        user_id = ""
        text = ""
