#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class FileStorage:

    def __init__(self):
        self.__objects = {}

    def new(self, obj):
        self.__objects[obj.id] = obj

    def save(self):
        with open("file.json", "w") as f:
            json.dump(self.__objects, f)

    def get(self, id):
        return self.__objects[id]

    def delete(self, obj=None):
        if obj is not None:
            del self.__objects[obj.id]

    def all(self, cls=None):
        if cls is None:
            return self.__objects.values()
        return {k: v for k, v in self.__objects.items() if isinstance(v, cls)}
