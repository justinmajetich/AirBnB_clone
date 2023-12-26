#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, String, ForeignKey
from os import getenv


class Review(BaseModel):
    """ Review classto store review information """
    name = ""
