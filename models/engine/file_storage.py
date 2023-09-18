#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns a dictionary of models curriently in storage"""
        return FileStorage.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        if obj:
            idx = obj.__class__.__name__ + '.' + obj.id
            self.__objects[idx] = obj

    def save(self):
        """Saves storage dictionary to file"""
        temp = {}
        for i, j in self.__objects.items():
            temp[i] = j.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
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
        try:
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
            for key, val in temp.items():
                self.__objects[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass
