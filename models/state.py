#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
import sys
from uuid import uuid4
import shlex
import models
from models.city import City
class State(BaseModel):
    """This is the class for State"""
    name = ""
    def __init__(self):
        super().__init__()
        self.id = str(uuid4())
