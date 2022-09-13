#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """returns the dictionary __objects"""
        if cls is not None:
            if type(cls) == str:
                cls = eval(cls)
            new_dict = {}
            for key, value in self.__objects.items():
                if type(value) == cls:
                    new_dict[key] = value
            return new_dict
        return self.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        if obj:
            self.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Deserialise json file to __objects, if it exists"""
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                json_dict = json.load(f)
                for value in json_dict.values():
                    cls = value['__class__']
                    self.new(eval('{}({})'.format(cls, '**value')))
        except(FileNotFoundError):
            pass

    def delete(self, obj=None):
        """deletes obj from __objects"""
        if obj is not None:
            try:
                key = obj.__class__.__name__ + "." + obj.id
                if key in self.__objects:
                    del self.__objects[key]
            except(KeyError):
                pass
