#!/usr/bin/python3
""" This module defines a class to manage file storage for hbnb clone"""
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """This class manages storage of hbnb models in JSON format

    Attributes:
        __file_path (str): The file to save to.
        __objects (dict): A dictionary of object instances.
    """

    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage of class"""
        if cls is not None:
            if type(cls) == str:
                cls = eval(cls)
            cls_dict = {}
            for key, value in self.__objects.items():
                if type(value) == cls:
                    cls_dict[key] = value
            return cls_dict
        return self.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj

    def save(self):
        """Saves storage dictionary to file"""
        td = {o: self.__objects[o].to_dict() for o in self.__objects.keys()}
        with open(self.__file_path, 'w') as file:
            json.dump(td, file)

    def reload(self):
        """Loads storage dictionary from file"""

        try:
            with open(self.__file_path, 'r') as file:
                for obj in json.load(file).values():
                    cname = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(cname)(**obj))
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """ Deletes a given object from __objects if it exists """
        try:
            del self.__objects["{}.{}".format(type(obj).__name__, obj.id)]
        except (AttributeError, KeyError):
            pass

    def close(self):
        """ Call the reload method."""
        self.reload()
