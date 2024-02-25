#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
import sys
from uuid import uuid4

class State(BaseModel):
    """ State class """
    name = ""
