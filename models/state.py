#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
import sys
import shlex
import models
from models.city import City
from uuid import uuid4

class State(BaseModel):
    """State class"""

    def __init__(self):
        self.id = str(uuid4())
