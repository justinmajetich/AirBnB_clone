#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """ This class manages storage of hbnb models in JSON format

    Attributes:
        __file_path (str): path to the JSON file
        __objects (dict): object storage structure

    """
    __file_path = os.path.relpath('file.json')
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        dictionary = {}
        if cls:
            for k, o in FileStorage.__objects.items():
                if cls == str(k).split('.')[0]:
                    dictionary.update({k: o})
            return dictionary
        else:
            return FileStorage.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({f"{obj.__class__.__name__}.{obj.id}": obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
        }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
            for val in temp.values():
                self.new(classes[val['__class__']](**val))
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            pass

    def delete(self, obj=None):
        """ Deletes object from __objects """
        if obj:
            obj_name = f"{obj.__class__.__name__}.{obj.id}"
            if FileStorage.__objects.get(obj_name):
                del FileStorage.__objects[obj_name]
        self.save()
