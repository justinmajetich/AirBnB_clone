#!/usr/bin/python3
"""This is the file storage class for AirBnB."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """JSON file storage engine.

    This class serializes instances to a JSON file and
    deserializes JSON file to instances.
    Attributes:
        __file_path: path to the JSON file
        __objects: objects will be stored
    """

    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Return a dictionary.

        Return:
            Returns a dictionary of __object.
            This dictionary can also be filtered to elements of one class.
        """
        objects = {}
        if cls:
            for obj in self.__objects:
                if type(self.__objects[obj]) == cls:
                    objects[obj] = self.__objects[obj]
        else:
            objects = self.__objects
        return objects

    def new(self, obj):
        """Set __object to given obj.

        Args:
            obj: given object
        """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """Serialize the file path to JSON file path."""
        my_dict = {}
        for key, value in self.__objects.items():
            my_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(my_dict, f)

    def reload(self):
        """Serialize the file path to JSON file path."""
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                for key, value in (json.load(f)).items():
                    value = eval(value["__class__"])(**value)
                    self.__objects[key] = value
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Delete obj from __objects (if it exists)."""
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            if key in self.__objects:
                del self.__objects[key]

    def close(self):
        """Deserializes all the JSON objects"""
