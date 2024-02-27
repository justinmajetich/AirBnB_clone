#!/usr/bin/python3
""" Review module for the HBNB project """
from os import getenv
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, String, ForeignKey

env = getenv('HBNB_TYPE_STORAGE')


class Review(BaseModel, Base):
    """"""
    __tablename__ = "reviews"
    if env == 'db':
        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    else:
        text = ""
        place_id = ""
        user_id = ""
