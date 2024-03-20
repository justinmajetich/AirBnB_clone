#!/usr/bin/python3
"""This module defines the file storage class for AirBnB"""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import shlex

class FileStorage:
    """This class serializes instances to a JSON file and
    deserializes JSON file to instances
    Attributes:
        __file_path: path to the JSON file
        __objects: dictionary to store serialized objects
    """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Returns all objects or objects of a specific class"""
        if cls:
            filtered_objects = {}
            for key, obj in self.__objects.items():
                class_name = key.split('.')[0]
                if class_name == cls.__name__:
                    filtered_objects[key] = obj
            return filtered_objects
        else:
            return self.__objects

    def new(self, obj):
        """Adds a new object to the dictionary of objects"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes the objects to a JSON file"""
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(serialized_objects, f)

    def reload(self):
        """Deserializes the JSON file to objects"""
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                serialized_objects = json.load(f)
                for key, value in serialized_objects.items():
                    class_name = value['__class__']
                    del value['__class__']
                    obj = eval(class_name)(**value)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Deletes an object from __objects dictionary"""
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            del self.__objects[key]

    def close(self):
        """Reloads the objects from JSON file"""
        self.reload()
