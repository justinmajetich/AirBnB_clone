#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseMode, Basel
from sqlachemy import Column, String, ForeignKey


class Review(BaseModel, Base):
    """ Review classto store review information """
    place_id = Column(String(60), nullable=False,
                      ForeignKey=('user.id'))
    user_id = ""Column(String(60), nullable=False,
                       ForeignKey=('place.id'))
    text = ""Column(String(1024), nullable=False)
