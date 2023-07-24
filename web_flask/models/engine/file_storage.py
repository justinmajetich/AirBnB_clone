#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
import models

class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is not None:
            return {k: v for k, v in self.__objects.items() if type(v) == cls}
        return self.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj

    def save(self):
        """Saves storage dictionary to file"""
        json_dict = {}
        for k in self.__objects.keys():
            json_dict[k] = self.__objects[k].to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(json_dict, f)

    def reload(self):
        """Loads storage dictionary from file"""
        try:
            with open(self.__file_path, 'r') as f:
                self.__objects = json.load(f)
            for k in self.__objects.keys():
                self.__objects[k] = eval(self.__objects[k]["__class__"])(**self.__objects[k])
        except FileNotFoundError:
            pass

    def close(self):
        """call reload() method for deserializing the JSON file to objects"""
        self.reload()
