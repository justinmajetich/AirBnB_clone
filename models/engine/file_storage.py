#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone
Removed class list """
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is not None:
            if type(cls) is str:
                cls = eval(cls)
            my_class = {}
            for key, value in self.__obects.items():
                if type(value) is cls:
                    my_class[key] = value
            return my_class
        return self.__objects

    def new(self, obj):
        """Adds new object to storage dictionary
        Restrctured to simplify """
        self.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj

    def save(self):
        """Saves storage dictionary to file
        restructured to ensure clean processing"""
        temp = {o: self.__objects[o].to_dict() for o in self.__objects.keys()}
        with open(self.__file_path, 'w') as f:
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""

        try:
            with open(self.__file_path, 'r') as f:
                for obj in json.load(f).values():
                    cls_name = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(cls_name)(**obj))
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Deletes object from __objects if it exists"""
        try:
            del self.__objects["{}.{}".format(type(obj).__name__, obj.id)]
        except (AttributeError, KeyError):
            pass

    def close(self):
        """ Calls reload() for deserialization  of JSON file to obj"""
        self.reload()
