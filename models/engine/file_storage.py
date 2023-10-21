#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review



class FileStorage:
    __file_path = 'file.json'
    __objects = {}
    CLASS_KEY = '__class__'
    ID_KEY = 'id'

    def all(self, cls=None):
        if cls:
            return {k: v for k, v in self.__objects.items() if v.__class__.__name__ == cls}
        else:
            return self.__objects

    def delete(self, obj=None):
        if obj is not None:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            if key in self.__objects:
                del self.__objects[key]
                self.save()

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        with open(FileStorage.__file_path, 'w') as f:
            json_obj = {key: value.to_dict() for key, value in self.__objects.items()}
            json.dump(json_obj, f)

    def reload(self):
        try:
            with open(FileStorage.__file_path, 'r') as f:
                json_data = json.load(f)
                for k, v in json_data.items():
                    cls_name = v[FileStorage.CLASS_KEY]
                    del v[FileStorage.CLASS_KEY]
                    self.__objects[k] = eval(cls_name)(**v)
        except (FileNotFoundError, json.JSONDecodeError):
            pass
