#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
import os
from importlib import import_module


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def __init__(self):
        """Initializes a FileStorage instance"""
        self.model_classes = {
            'BaseModel': import_module('models.base_model').BaseModel,
            'User': import_module('models.user').User,
            'State': import_module('models.state').State,
            'City': import_module('models.city').City,
            'Amenity': import_module('models.amenity').Amenity,
            'Place': import_module('models.place').Place,
            'Review': import_module('models.review').Review
        }

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage

        Args:
            cls (class): class to filter objects by (optional)

        Returns:
            dict: dictionary of models in storage
        """
        if cls is None:
            return self.__objects
        return {key: val for key, val in self.__objects.items() if type(val) == cls}

    def delete(self, obj=None):
        """Removes an object from the storage dictionary
        
        Args:
            obj (BaseModel): object to remove from storage dictionary
        """
        if obj is not None:
            obj_key = "{}.{}".format(obj.__class__.__name__, obj.id)
            if obj_key in self.__objects.keys():
                del self.__objects[obj_key]
                self.save()

    def new(self, obj):
        """Adds new object to storage dictionary

        Args:
            obj (BaseModel): object to add to storage dictionary
        """
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """Saves storage dictionary to file"""
        with open(self.__file_path, 'w') as file:
            temp = {}
            for key, val in self.__objects.items():
                temp[key] = val.to_dict()
            json.dump(temp, file)

    def reload(self):
        """Loads storage dictionary from file"""
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                for key, val in json.load(file).items():
                    val = eval(val['__class__'])(**val)
                    self.__objects[key] = val
        except FileNotFoundError:
            pass
    def close(self):
        """Closes the storage engine."""
        self.reload()
