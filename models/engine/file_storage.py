#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from models.city import City
from models.user import User
from models.place import Place
from models.state import State
from models.review import Review
from models.amenity import Amenity
from models.base_model import BaseModel

classes = {
    'BaseModel': BaseModel,
    'User': User,
    'Place': Place,
    'State': State,
    'City': City,
    'Amenity': Amenity,
    'Review': Review
}


class FileStorage:
    """ Storage of hbnb models in JSON format """
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """ Returns dictionary of models currently in storage """
        if cls is not None:
            if type(cls) is str:
                cls = classes.get(cls)
            obj_dict = {}
            for val in FileStorage.__objects.values():
                if type(val) is cls:
                    obj_dict[f"{val.to_dict()['__class__']}.{val.id}"] = val
            return obj_dict
        else:
            return FileStorage.__objects

    def new(self, obj):
        """ Adds new object to storage dictionary """
        self.all().update({f"{obj.to_dict()['__class__']}.{obj.id}": obj})

    def save(self):
        """ Serialization of __objects to JSON file """
        with open(FileStorage.__file_path, "w") as outfile:
            obj_dict = {}
            obj_dict.update(FileStorage.__objects)
            for key, value in FileStorage.__objects.items():
                obj_dict[key] = value.to_dict()
            json.dump(obj_dict, outfile)

    def reload(self):
        """ Deserialization to __objects from saved JSON file """
        try:
            obj_dict = {}
            with open(FileStorage.__file_path, 'r') as f:
                obj_dict = json.load(f)
                for key, value in obj_dict.items():
                    self.all()[key] = classes[value['__class__']](**value)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """ Deletes specified object from dictionary """
        if obj is not None:
            key = f"{type(obj).__name__}.{obj.id}"
            if key in self.__objects:
                del self.__objects[key]
