#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    __file_path = "file.json"
    __objects = {}

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
        """Loads storage dictionary from file"""
        classes = self.model_classes
        if os.path.isfile(self.__file_path):
            temp = {}
            with open(self.__file_path, "r") as file:
                temp = json.load(file)
                for key, val in temp.items():
                    self.all()[key] = classes[val["__class__"]](**val)

    def delete(self, obj=None):
        """Deletes obj from __objects if it's inside."""
        if obj is not None:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            FileStorage.__objects.pop(key, None)
