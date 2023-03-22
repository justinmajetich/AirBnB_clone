#!/usr/bin/python3
""" Review module for the HBNB project """
#  from sqlalchemy import Column, String, ForeignKey
from models.base_model import BaseModel
#  from models import storage_type


class Review(BaseModel):
    """ Review classto store review information."""
#    __tablename__ = 'reviews'
#    if storage_type == 'db':
#        place_id = Column(String(60), nullable=False, ForeignKey("places.id"))
#        user_id = Column(String(60), nullable=False, ForeignKey("users.id"))
#        text = Column(String(1024), nullable=False)
#    else:
    place_id = ""
    user_id = ""
    text = ""
