#!/usr/bin/python3
"""
Contains FileStorage class
"""


import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review

classes = {
    "BaseModel": BaseModel,
    "User": User,
    "Amenity": Amenity,
    "State": State,
    "Place": Place,
    "Review": Review,
}


class FileStorage:
    """serializes objects to JSON strings
    deserializes JSON strings back to objects"""

    # string - path to JSON file
    __file_path = "file.json"
    # dictionary - (empty) but will store all objects by <class name>.id
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class>.id"""
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path:__file_path)"""
        object_to_json = {}
        for key in self.__objects:
            object_to_json[key] = self.__objects[key].to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(object_to_json, f)

    def reload(self):
        """deserialize the JSON file to __objects
        only if file (__file_path) exists"""
        try:
            with open(self.__file_path, "r") as f:
                jo = json.load(f)
            for key in jo:
                self.__objects[key] = classes[jo[key]["__class__"]](**jo[key])
        except Exception:
            pass
