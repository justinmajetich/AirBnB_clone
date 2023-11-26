#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel
import models
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey


class Review(BaseModel):
    """ Review classto store review information """
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'review'
        place_id = Column(
                String(60),
                ForeignKey('places.id'),
                nullable=False
            )
        user_id = Column(
                String(60),
                ForeignKey('users.id'),
                nullable=False
            )
        text = Column(
                String(1024),
                nullable=False
            )
    else:
        text = ""
        place_id = ""
        user_id = ""

    def __init__(self, *args, **kwargs):
        """initializes Review"""
        super().__init__(*args, **kwargs)
