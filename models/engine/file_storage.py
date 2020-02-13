#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from os import path


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns a dictionary of models currently in storage"""
        return FileStorage.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        FileStorage.__objects.update({obj.to_dict()['__class__'] +
                                     '.' + obj.id: str(obj)})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(FileStorage.__objects, f)

    def reload(self):
        """Loads storage dictionary from file"""
        try:
            with open(FileStorage.__file_path, 'r') as f:
                FileStorage.__objects = json.loads(f.read())
        except IOError:
            pass
