#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
import shlex


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models cls currently in storage"""
        res = {}
        if cls is not None:
            for key in self.__objects:
                part = key.replace('.', ' ')
                part = shlex.split(part)
                if (part[0] == cls.__name__):
                    res[key] = self.__objects[key]
            return (res)
        return self.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj
        """self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})"""

    def save(self):
        """Saves storage dictionary to file"""
        temp = {}
        """temp.update(FileStorage.__objects)"""
        for key, val in self.__objects.items():
            temp[key] = val.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
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
            with open(self.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    value = eval(val["__class__"])(**val)
                    self.__objects[key] = value
                    """self.all()[key] = classes[val['__class__']](**val)"""
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """delete obj from __objects if it exist"""
        if obj is not None:
            key = type(obj).__name__ + '.' + obj.id
            del self.__objects[key]
