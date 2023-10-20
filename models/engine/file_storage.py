#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
import os


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""

    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """
        Returns a list of objects, optionally filtered by class.
        """
        if cls:
            filtered_dict = {}
            for key, value in self.__objects.items():
                if cls.__name__ in key:
                    filtered_dict[key] = value
            return filtered_dict
        return self.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Saves storage dictionary to file"""
        with open(self.__file_path, "w") as f:
            json_dict = {key: value.to_dict() for key,
                         value in self.__objects.items()}
            json.dump(json_dict, f)

    def delete(self, obj=None):
        """del obj if not none"""
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            if key in self.__objects:
                del self.__objects[key]
                self.save()

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        list_of_classes = {
            "BaseModel": BaseModel,
            "User": User,
            "Place": Place,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Review": Review,
        }
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r") as f:
                json_dict = json.load(f)
            self.__objects = {}
            for key, value in json_dict.items():
                class_name = value["__class__"]
                value.pop("__class__", None)
                if class_name in list_of_classes:
                    cls = list_of_classes[class_name]
                    obj = cls(**value)
                    self.__objects[key] = obj
        else:
            return
