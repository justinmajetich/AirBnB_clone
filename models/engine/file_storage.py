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

    #code change
    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        dict = {}
        if cls:
            _dicts = self.__objects
            for key in _dicts:
                parts = key.replace('.', ' ')
                parts = shlex.split(partition)
                if (partition[0] == cls.__name__):
                    dict[key] = self.__objects[key]
            return (dict)
        else:
            return self.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    #change is made
    def save(self, obj):
        """Saves storage dictionary to file"""
        #new code
         if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def reload(self):
        """Loads storage dictionary from file"""
        # change has been made
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                for key, value in (json.load(f)).items():
                    value = eval(value["__class__"])(**value)
                    self.__objects[key] = value
        except FileNotFoundError:
            pass
    
    # new code
    def delete(self, obj=None):
        """ delete an existing element"""
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            del self.__objects[key]
# new code
    def close(self):
        """ calls reload() """
        self.reload()

