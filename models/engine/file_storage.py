#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is not None:
            newDict = {}
            for key, value in self.__objects.items():
                if cls == value.__class__ or cls == type(value).__name__:
                    newDict[key] = value
            return newDict
        return FileStorage.__objects

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
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as f:
                dataDict = json.load(f)
            for key in dataDict:
                self.__objects[key] = \
                    classes[dataDict[key]["__class__"]](**dataDict[key])
        except Exception:
            pass

    def delete(self, obj=None):
        """Deletes obj from __objects if it is inside"""
        if obj is not None:
            key = type(obj).__name__ + '.' + obj.id
            if key in self.__objects:
                del self.__objects[key]

    def close(self):
        """method for deserializing the JSON file to objects"""
        try:
            self.reload()
        except Exception:
            pass