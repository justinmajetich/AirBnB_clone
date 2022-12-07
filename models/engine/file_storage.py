#!/usr/bin/python3
"""\
Serializes instances to JSON file and deserializes JSON file to instances.\
"""
import json
import os.path
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class FileStorage:
    """Serializes to a JSON file and deserializes from a JSON file."""

    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Returns the dictionary object"""
        if cls is None:
            return self.__objects
        else:
            filtered_dict = {}
            for key, value in self.__objects.items():
                if (value.__class__ == cls):
                    filtered_dict[key] = value
            return filtered_dict

    def new(self, obj):
        """Sets in __objects the given obj with key <obj class name>.id"""
        self.__objects[obj.__class__.__name__ + "." + obj.id] = obj

    def delete(self, obj=None):
        """Deletes a given object from __objects"""
        if obj is None:
            return
        else:
            try:
                tmp = obj.__class__.__name__ + "." + obj.id
                self.__objects.pop(tmp)
            except:
                print("{} object not found!".format(obj.__class__.__name__))
            finally:
                return

    def save(self):
        """Serializes __objects to defined JSON file"""
        with open(self.__file_path, "w") as file:
            tmp_dict = {key: obj.to_dict() for key, obj in
                        self.__objects.items()}
            json.dump(tmp_dict, file)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, "r") as file:
                tmp_dict = json.load(file)
                for key, value in tmp_dict.items():
                    self.__objects[key] = eval(key.split(".")[0])(**value)

    def close(self):
        """Closes the storage engine."""
        self.reload()
