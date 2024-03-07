#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is None:
            return self.__objects
        else:
            return {
                k: v for k, v in self.__objects.items()
                if k.startswith(cls.__name__)
            }

    def new(self, obj):
        """Adds new object to storage dictionary"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Saves storage dictionary to file"""
        temp = {key: val.to_dict() for key, val in self.__objects.items()}
        print("Updated Instances: ", temp)
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""

        classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
        }
        try:
            with open(self.__file_path, 'r') as f:
                temp = json.load(f)
                self.__objects = {}
                for key, val in temp.items():
                    class_obj = classes[val['__class__']]
                    instance = class_obj(**val)
                    self.__objects[key] = instance
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Deletes obj from storage dictionary"""
        if obj is None:
            return
        key = f"{obj.__class__.__name__}.{obj.id}"
        if key in self.__objects:
            del self.__objects[key]
