#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from os import getenv


class State(BaseModel, Base):
    """ State class """

    __tablename__ = "states"

    name = Column(String(128), nullable=False)

if getenv('HBNB_TYPE_STORAGE') == "FileStorage":
    name = ""

else:
    """ storage = db """