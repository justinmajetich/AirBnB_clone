#!/usr/bin/python3

"""
Module for FileStorage class, which manages storage of objects in JSON files.
"""

import json
from datetime import datetime
from models import *


class FileStorage:
    """
    Class to manage storage of objects in JSON files.
    """
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """
        Initializes FileStorage by reloading existing objects from the
        JSON file.
        """
        self.reload()

    def all(self, cls=None):
        """
        Returns a dictionary of all objects or specific class objects.
        Args:
            cls (str): Class name to filter objects.
        Returns:
            dict: Dictionary of objects (all or filtered by class).
        """
        if cls is None:
            return FileStorage.__objects

        storage = {}
        for obj_id in FileStorage.__objects:
            obj_cls = FileStorage.__objects[obj_id].__class__.__name__
            if cls == obj_cls:
                storage[obj_id] = FileStorage.__objects[obj_id]

        return storage

    def new(self, obj):
        """
        Adds a new object to the storage dictionary.
        Args:
            obj: Object to be added.
        """
        if obj is not None:
            FileStorage.__objects[obj.id] = obj

    def save(self):
        """
        Serializes objects to JSON and writes them to the JSON file.
        """
        store = {}
        for k in FileStorage.__objects.keys():
            store[k] = FileStorage.__objects[k].to_json()

        with open(FileStorage.__file_path, mode="w", encoding="utf-8") as fd:
            fd.write(json.dumps(store))

    def update(self, cls, obj_id, key, new_value):
        """
        Updates an object attribute value.
        Args:
            cls (str): Class name of the object.
            obj_id (str): ID of the object.
            key (str): Attribute name to be updated.
            new_value: New value for the attribute.
        Returns:
            int: 1 if successful, 0 if object ID not found.
        """
        if obj_id not in FileStorage.__objects:
            return 0

        obj = FileStorage.__objects[obj_id]
        setattr(obj, key, new_value)
        return 1

    def reload(self):
        """
        Deserializes JSON file and reloads objects into memory.
        """
        try:
            with open(FileStorage.__file_path,
                      mode="r+", encoding="utf-8") as fd:
                FileStorage.__objects = {}
                temp = json.load(fd)
                for k in temp.keys():
                    cls = temp[k].pop("__class__", None)
                    cr_at = temp[k]["created_at"]
                    cr_at = datetime.strptime(cr_at, "%Y-%m-%d %H:%M:%S.%f")
                    up_at = temp[k]["updated_at"]
                    up_at = datetime.strptime(up_at, "%Y-%m-%d %H:%M:%S.%f")
                    FileStorage.__objects[k] = eval(cls)(temp[k])
        except Exception as e:
            pass

    def delete(self, obj=None):
        """
        Deletes an object from the storage dictionary.
        Args:
            obj: Object to be deleted.
        """
        if obj is None:
            return

        FileStorage.__objects.pop(obj.id, 0)

    def close(self):
        """
        Calls the save() method to save objects to JSON file.
        """
        self.save()
