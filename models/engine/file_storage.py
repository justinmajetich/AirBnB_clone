#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    
    __file_path = "file.json"
    __objects = {}
    all_classes = {'BaseModel': BaseModel, 'User': User,
                   'State': State, 'City': City, 'Amenity': Amenity,
                   'Place': Place, 'Review': Review}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        all_return = {}

        if cls:
            if cls.__name__ in self.all_classes:
                for key, val in self.__objects.items():
                    if key.split('.')[0] == cls.__name__:
                        all_return.update({key: val})
        else:
            all_return = self.__objects

        return all_return

    def new(self, obj):
        """Adds new object to storage dictionary"""
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """Saves storage dictionary to file"""
        my_dict = {}
        for key, value in self.__objects.items():
            my_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(my_dict, f)

    def reload(self):
        """Loads storage dictionary from file"""
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                for key, value in (json.load(f)).items():
                    value = eval(value["__class__"])(**value)
                    self.__objects[key] = value
        except FileNotFoundError:
            pass

    def close(self):
        """Reloads JSON objects"""
        return self.reload()

    def delete(self, obj=None):
        """Deletes obj from __objects if present"""
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            del self.__objects[key]
