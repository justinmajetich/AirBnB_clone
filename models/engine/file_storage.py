#!/usr/bin/python3
"""This is the file storage class for AirBnB"""
import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models.city import City

class FileStorage:
    '''
    Class that serializes instances to a JSON file
    '''
    __file_path= 'file.json'
    __object ={}

    def all(self, cls=None):
        """
        returns a dictionary
        """
        if cls is None:
            return self.__objects
        dic = {}
        for key, value in self.__objects.items():
            if type(value) is cls:
                dic[key] = value
        return dic
    
    def new(self, obj):
        """
        sets __object to given obj
        """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """
        serialize the file path to JSON file path
        """
        my_dict = {}
        for key, value in self.__objects.items():
            my_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(my_dict, f)

    def reload(self):
        """
        serialize the file path to JSON file path
        """
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                for key, value in (json.load(f)).items():
                    value = eval(value["__class__"])(**value)
                    self.__objects[key] = value
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """
        Update FileStorage, add a new instance publica
        """
        if obj in self.__objects.values():
            del self.__objects["{}.{}".format(type(obj).__name__, obj.id)]
