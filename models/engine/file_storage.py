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
import shlex


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of objects
        Args:
            cls: Optional class to filter objects by
        Return:
            A dictionary of objects
        """
        if cls:
            filtered_objects = {}
            for key, value in self.__objects.items():
                class_name = key.split('.')[0]
                if class_name == cls.__name__:
                    filtered_objects[key] = value
            return filtered_objects
        else:
            return self.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """Saves storage dictionary to file"""
        obj_dict = {}
        for key, value in self.__objects.items():
            obj_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Loads storage dictionary from file"""
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name = value["__class__"]
                    instance = eval(class_name)(**value)
                    self.__objects[key] = instance
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """ delete an existing element"""
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            del self.__objects[key]

    def close(self):
        """ calls reload()"""
        self.reload()
