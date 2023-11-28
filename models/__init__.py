#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


storage = FileStorage()
storage.reload()

classes = {
    'BaseModel': BaseModel,
    'User': User,
    'Place': Place,
    'State': State,
    'City': City,
    'Amenity': Amenity,
    'Review': Review
}

dot_cmds = ['all', 'count', 'show', 'destroy', 'update']

types = {
    'number_rooms': int,
    'number_bathrooms': int,
    'max_guest': int,
    'price_by_night': int,
    'latitude': float,
    'longitude': float
}
