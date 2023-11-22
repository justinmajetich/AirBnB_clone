#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseMode, Basel
from sqlachemy import Column, String, ForeignKey
from models.place import Place
from models.user import User


class Review(BaseModel, Base):
    """ Review classto store review information """
    place_id = Column(String(60), nullable=False,
                      ForeignKey=(User.id))
    user_id = ""Column(String(60), nullable=False,
                       ForeignKey=(Place.id))
    text = ""Column(String(1024), nullable=False)
