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

classes = {"Amenity": Amenity,
           "Basemodel": BaseModel, 
           "City": City, 
           "Place": Place,
           "Review": Review, 
           "State": State, 
           "User": User}

class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    #path to JSON file
    __file_path = 'file.json'
    #empty dictionary
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls != None:
            new_dict = {}
            for key, value in self.__objects.items():
                if cls == value.__class__ or cls == value.__class__.__name__:
                    new_dict[key] = value
            return new_dict
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj"""
        #self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})
        if obj is not None:
            key = obj.__class__.__name__ + '.' + obj.id
            self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        json_object = {}
        for key in self._objects:
            json_object[key] = self.__objects[key].to_dict()
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(json_object, f)

    def reload(self):
        """deserializes the JSON file"""

        try:
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                        self.__objects[key] = classes[temp[key]["__class__"]](**temp[key])
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """
         Delete obj from __objects
        """
        if obj != None:
            key = obj.__class__.__name__ + '.' + obj.id
        if key in self.__objects:
            del self.__objects[key]

    def close(self):
        """call reload() for deserialization"""
        self.reload()
