#!/usr/bin/python3
"""
A module handling file storage engine of the application
"""

import json
import datetime
from models.base_model import BaseModel
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """
    custom FileStorage class
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns dict repr of all objects
        """
        if cls is not None:
            cls = cls.__name__
            new_dict = {}
            for key in self.__objects.keys():
                if key.split(".")[0] == cls:
                    new_dict[key] = self.__objects[key]
            return new_dict
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id
        Args:
            obj (obj): accepts the object to write
        """
        key = obj.__class__.__name__ + "." + str(obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        json_object = {}
        for key in self.__objects:
            json_object[key] = self.__objects[key].to_dict()

        with open(self.__file_path, 'w') as f:
            json.dump(json_object, f, indent=2)

    def reload(self):
        """
        deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists;
        otherwise, do nothing)
        """
        try:
            with open(self.__file_path, encoding="utf-8") as f:
                data = json.load(f)
                for obj in data.values():
                    self.new(eval(obj["__class__"])(**obj))
        except FileNotFoundError:
            return

    def classes(self):
        """Returns a dictionary of a valid classes"""

        classes = {
            "BaseModel": BaseModel,
            "Amenity": Amenity,
            "City": City,
            "Place": Place,
            "State": State,
            "User": User,
            "Review": Review
        }
        return classes

    def delete(self, obj=None):
        """Deletes obj(an object) from __objects"""
        if obj:
            key = obj.__class__.__name__ + '.' + obj.id
            del self.__objects[key]

    def close(self):
        """Reload JSON objects
        """
        return self.reload()
