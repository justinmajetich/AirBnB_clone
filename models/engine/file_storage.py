#!/usr/bin/python3
"""This module defines a class to manage file storage"""
import json
import models


class FileStorage:
    """Serialize and deserialize"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """It return all objects or objects of a specific class"""
        if cls:
            return {
                key: obj for key, obj in self.__objects.items()
                if isinstance(obj, cls)
            }
        else:
            return self.__objects

    def delete(self, obj=None):
        """Delete the instance of a class"""
        if obj is None:
            return

        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        if key in self.__objects:
            del self.__objects[key]

    def new(self, obj):
        """Adds new object to storage dictionary
           Added the condition check to avoid situation when obj is missing or
           incorrectly implemented, returning `DeclarativeMeta` as a class.
        """
        if obj is not None and hasattr(obj, "to_dict"):
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """Serializes objects before saving dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            serialized_objs = {}

            for key, obj in self.all().items():
                serialized_objs[key] = obj.to_dict()
            json.dump(serialized_objs, f)

    def reload(self):
        """Loads storage dictionary from file by creating an instance of
           that class passing in the attributes and storing it in __objects
           under dictionary key.
        """
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
        try:
            obj_dict = {}
            with open(self.__file_path, 'r') as f:
                obj_dict = json.load(f)
                for key, value in obj_dict.items():
                    self.__objects[key] = classes[value['__class__']](**value)
        # json.JSONDecodeError
        except (FileNotFoundError):
            pass

    def close(self):
        """Calls reload after unit of work is done"""
        self.reload()
