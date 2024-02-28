#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb clone"""
import os
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DatabaseStorage:
    """Database management of storage for hbnb clone"""
    def __init__(self) -> None:
        pass