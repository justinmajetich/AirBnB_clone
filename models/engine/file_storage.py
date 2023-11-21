#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
import os
from collections.abc import Mapping


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
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
        class_objs = {}
        if cls:
            for key, value in self.__objects.items():
                class_name = key.split('.')[0]
                if class_name == cls.__name__:
                    new_instance = classes[class_name](**value)
                    class_objs[key] = str(new_instance)
            return class_objs
        else:
            for key, value in self.__objects.items():
                class_name = key.split('.')[0]
                new_instance = classes[class_name](**value)
                class_objs[key] = str(new_instance)
            return class_objs
    def objects(self):
        """Getter method for __objects"""
        return self.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        new_obj = obj
        if not self.is_subscriptable(obj):
            new_obj = obj.to_dict()
        key = f"{new_obj['__class__']}.{new_obj['id']}"
        self.__objects[key] = new_obj

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
            for key, value in self.__objects.items():
                if key != obj_key:
                    temp_obj[key] = value
            self.__objects = temp_obj
            self.save()

    def is_subscriptable(self, obj):
        """Checks whether a dict is subscriptable"""
        return isinstance(obj, Mapping)
