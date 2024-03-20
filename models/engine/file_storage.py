#!/usr/bin/python3
"""This module defines the FileStorage class for managing file storage in the AirBnB clone project."""

import json
import shlex
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class FileStorage:
    """The FileStorage class serializes instances to a JSON file and deserializes JSON files to instances.

    Attributes:
        __file_path: A string representing the path to the JSON file.
        __objects: A dictionary containing the objects stored in the file storage.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of objects filtered by class type.

        Args:
            cls (class, optional): The class type to filter objects by. Defaults to None.

        Returns:
            dict: A dictionary containing the filtered objects.
        """
        filtered_objects = {}
        if cls:
            for key, obj in self.__objects.items():
                class_name = key.split('.')[0]
                if class_name == cls.__name__:
                    filtered_objects[key] = obj
            return filtered_objects
        else:
            return self.__objects

    def new(self, obj):
        """Adds a new object to the storage dictionary.

        Args:
            obj (BaseModel): The object to add to storage.
        """
        if obj:
            key = f"{type(obj).__name__}.{obj.id}"
            self.__objects[key] = obj

    def save(self):
        """Serializes the objects dictionary to a JSON file."""
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(serialized_objects, f)

    def reload(self):
        """Deserializes the JSON file to objects."""
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                loaded_objects = json.load(f)
                for key, obj_data in loaded_objects.items():
                    obj = eval(obj_data["__class__"])(**obj_data)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Deletes an object from storage.

        Args:
            obj (BaseModel, optional): The object to delete from storage. Defaults to None.
        """
        if obj:
            key = f"{type(obj).__name__}.{obj.id}"
            del self.__objects[key]

    def close(self):
        """Calls the reload method to deserialize the JSON file."""
        self.reload()
