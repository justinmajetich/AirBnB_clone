#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from ..amenity import Amenity
from ..city import City
from ..place import Place
from ..review import Review
from ..state import State
from ..user import User


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    # Create a dictionary mapping class names to their corresponding classes
    class_mapping = {
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review,
        "State": State,
        "User": User,
    }

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage."""
        if cls is not None:
            filtered_objects = {
                k: v
                for k, v in FileStorage.__objects.items()
                if isinstance(v, cls)
            }
            return filtered_objects
        return FileStorage.__objects

    def new(self, obj):
        """Adds new object to storage dictionary."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Saves storage dictionary to file."""
        with open(FileStorage.__file_path, "w") as f:
            temp = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file."""
        try:
            with open(FileStorage.__file_path, "r") as f:
                temp = json.load(f)
                for key, val in temp.items():
                    cls_name, obj_id = key.split(".")
                    cls = FileStorage.class_mapping.get(cls_name)
                    if cls:
                        obj = cls(**val)
                        FileStorage.__objects[key] = obj
                    else:
                        print(
                            f"Warning: Class {cls_name}"
                            + "not found during reload."
                        )
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Deletes obj from __objects if it's inside."""
        if obj is not None:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            FileStorage.__objects.pop(key, None)
