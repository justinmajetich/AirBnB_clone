#!/usr/bin/python3
from datetime import datetime
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User
import json
import os


class FileStorage:
    """ A class called FileStorage
    attributes:
    attr1(__file_path): JSON file path
    attr2(__objects): dictionary"""
    __file_path = "file.json"
    open(__file_path, "a")
    __objects = {}

    def all(self):
        """ return all objects"""
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key"""
        key = obj.__class__.__name__ + '.' + obj.id
        self.__objects[key] = obj

    def save(self):
        """ save to JSON"""
        dict = {}
        for key, value in self.__objects.items():
            dict[key] = value.to_dict()
        with open(self.__file_path, mode="w") as my_file:
            json.dump(dict, my_file)

    def reload(self):
        """reload from JSON"""
        my_class = {"BaseModel": BaseModel, "Amenity": Amenity,
                    "City": City, "Place": Place, "Review": Review,
                    "User": User, "State": State}
        dic_to_fill = {}
        if(os.stat(self.__file_path).st_size != 0):
            with open(self.__file_path) as json_file:
                dict_to_fill = json.load(json_file)
                for key, value in dict_to_fill.items():
                    self.__objects[key] =\
                        my_class[value['__class__']](**value)
