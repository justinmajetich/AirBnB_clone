#!/usr/bin/env python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """Represent an abstracted storage engine.

    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Return a dictionary of instantiated objects in __objects.

        Args:
            cls (str): The class name to filter objects by.

        Return:
            If cls is specified, a dictionary of objects of that type.
            Otherwise, the __objects dictionary.
        """
        if cls:
            if isinstance(cls, str):
                cls = eval(cls)
            return {key: obj for key, obj in self.__objects.items() if isinstance(obj, cls)}
        return self.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id."""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        dictionary = {}
        for key, obj in self.__objects.items():
            dictionary[key] = obj.to_dict(remove_password=False)
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(dictionary, f)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                for o in json.load(f).values():
                    name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(name)(**o))
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Delete a given object from __objects, if it exists."""
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects.pop(key, None)

    def close(self):
        """Call the reload method."""
        self.reload()

    def get(self, cls, id):
        """Returns a given instance from __objects.

        Args:
            cls (str): The class name of the instance to retrieve.
            id  (str): The ID of the instance to retrieve.
        """
        if cls is None or id is None:
            return None
        key = '{}.{}'.format(cls, id)
        return self.__objects.get(key, None)

    def count(self, cls=None):
        """Returns a count of all instances of the given class in __objects.

        If no class is given, returns the total object count.

        Args:
            cls (str): The class type to count instances of.
        """
        if not cls:
            return len(self.__objects)
        return sum(1 for key in self.__objects if key.startswith(cls))
