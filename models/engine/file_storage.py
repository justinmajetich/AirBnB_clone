#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
import re


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls:
            cls_dict = {}
            keys = self.__objects.keys()
            if type(cls) is not str:
                cls = cls.__name__
            for key in keys:
                cls_name = key.split('.')[0]
                if cls_name == cls:
                    cls_dict[key] = self.__objects[key]
            return cls_dict
        return FileStorage.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.__class__.__name__ + '.' + obj.id: obj})

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
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    cls_name = re.findall(r"^\w+", key)
                    self.__objects[key] = eval(cls_name[0])(**val)

        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """deletes an object"""
        if obj:
            key = obj.__class__.__name__ + '.' + obj.id
            del self.__objects[key]
