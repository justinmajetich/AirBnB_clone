#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
import os
import sqlalchemy


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "cities"
    name = ""
