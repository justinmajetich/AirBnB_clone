#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""


import json

from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

classes = {
    'BaseModel': BaseModel, 'User': User, 'Place': Place,
    'State': State, 'City': City, 'Amenity': Amenity,
    'Review': Review
}


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is not None:
            newDict = dict()
            for k, v in self.__objects.items():
                if cls == v.__class__.__name__ or cls == v.__class__:
                    newDict[k] = v
                return newDict
            return self.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        if obj is not None:
            key = "{}.{}".format(
                obj.__class__.__name__, obj.id
            )
            self.__objects[key] = obj

    def save(self):
        """Saves storage dictionary to file"""
        all_obj = dict()
        for k in self.__objects:
            all_obj[k] = self.__objects[k].to_dict()

        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(all_obj, f)

    def reload(self):
        """Loads storage dictionary from file"""

        try:
            with open(self.__file_path, "r") as f:
                jsn_file = json.load(f)

            for k in jsn_file:
                self.__objects[k] = classes[jsn_file[k]["__class__"]](
                    **jsn_file[k]
                )

        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """
        deletes obj from __objects
        """

        if obj is not None:
            objectKey = "{}.{}".format(
                obj.__class__.__name__, obj.id
            )
            if objectKey in self.__objects:
                del self.__objects[objectKey]

    def close(self):
        """call reload()"""
        self.reload()
