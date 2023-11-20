#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
import os


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns a dictionary of models currently in storage"""
        return FileStorage.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        key = f"{obj['__class__']}.{obj['id']}"
        self.__objects[key] = obj

    def save(self):
        """Saves storage dictionary to file"""
        temp = json.dumps(self.__objects)
        with open(FileStorage.__file_path, 'w') as f:
            f.write(temp)

    def reload(self):
        """Loads storage dictionary from file"""
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                self.__objects = json.load(file)
