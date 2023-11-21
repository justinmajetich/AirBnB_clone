#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
import os


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls:
            class_objs = {}
            for key, value in self.__objects.items():
                class_name = key.split('.')[0]
                if class_name == cls.__name__:
                    class_objs[key] = value
            return class_objs
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

    def delete(self, obj=None):
        """Deletes an object from the __objects"""
        if obj:
            obj_key = f"{obj.to_dict()['__class__']}.{obj.to_dict()['id']}"
            temp_obj = {}
            for key, value in self.all().items():
                if key != obj_key:
                    temp_obj[key] = value
            self.__objects = temp_obj
