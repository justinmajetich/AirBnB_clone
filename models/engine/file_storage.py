#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
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

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls:
            filtered = {}
            for key in self.__objects.keys():
                if key.split('.')[0] == cls.__name__:
                    filtered[key] = self.__objects[key]
            return filtered
        return FileStorage.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        json_objects = {}
        for key in self.__objects:
                json_objects[key] = self.__objects[key].to_dict(save_check=True)
        with open(self.__file_path, 'w') as f:
            json.dump(json_objects, f)

    def reload(self):
        """Loads storage dictionary from file"""
        try:
            with open(self.__file_path, 'r') as f:
                temp = json.load(f)
            for key in temp:
                self.__objects[key] = classes[temp[key]['__class__']](**temp[key])
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Deletes object if obj is passed, else do nothing"""
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            del (self.__objects[key])
