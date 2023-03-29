#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
import shlex  # for splitting lines
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
            }


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def __init__(self):
        """gettin' init, if you will"""
        pass

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage
        is cls is specified, only returns that class"""
        if cls is not None:
            if type(cls) is str:
                cls = eval(cls)
            spec_dict = {}
            for key, val in self.__objects.items():
                if cls == type(val):
                    spec_dict[key] = val
            return spec_dict
        return self.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""

        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Deletes an instance"""

        if obj is None:
            pass
        else:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            if key in self.__objects:
                del self.__objects[key]
                self.save()

    def close(self):
        """Reloads a sesh"""
        self.reload()
