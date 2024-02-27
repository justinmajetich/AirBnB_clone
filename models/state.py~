#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
import sys
from uuid import uuid4
import shlex
import models
from models.city import City
from sqlalchemy.ext.declarative import declarative_base


class State(BaseModel):
    """State class"""
    name = ""
    def __init__(self, *args):
        super().__init__(*args)
        id = str(uuid4)
        
