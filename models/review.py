#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy import Float


class Review(BaseModel, Base):
    """ Review class to store review information """
    __tablename__ = 'reviews'

    text = Column(String(1024),nullable=False)
    place_id = Column(String(60),ForeignKey('place.id'),nullable=False)
    user_id = Column(String(60), ForeignKey('user.id'), nullable=False)
