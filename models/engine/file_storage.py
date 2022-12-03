#!/usr/bin/python3
"""
Module containing the class FileStorage that serializes instances
to a JSON file and deserializes JSON file to instances
"""
import json


class FileStorage:
    """
    Serializes instances
    to a JSON file and deserializes JSON file to instances
    """

    # string - path to the JSON file
    __file_path = "file.json"
    # dictionary - empty but will store all objects by <class name>.id
    # (ex: to store a BaseModel object with id=12121212,
    # the key will be BaseModel.12121212)
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls:
            same = dict()
            for key, row in self.__objects.items():
                if row.__class__ == cls:
                    same[key] = row
            return same
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        FileStorage.__objects[obj.__class__.__name__ + "." +
                              str(obj.id)] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        d = {}
        for obj_id, obj in FileStorage.__objects.items():
            d[obj_id] = obj.to_dict()
        try:
            with open(FileStorage.__file_path, 'w+', encoding="utf-8") as f:
                json.dump(d, f, indent=4)
        except Exception:
            pass

    def reload(self):
        """deserializes the JSON file to
        __objects (only if the JSON file (__file_path)
        exists ; otherwise, do nothing. If the file doesn’t exist,
        no exception should be raised)
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review
        try:
            with open(FileStorage.__file_path, 'r', encoding="utf-8") as f:
                d = json.load(f)
            for obj_id, objd in d.items():
                FileStorage.__objects[obj_id] = eval(objd['__class__'])(**objd)
        except Exception:
            pass

    def delete(self, obj=None):
        """delete obj froom __object"""
        if obj is not None:
            key = obj.__class__.__name__ + '.' + obj.id
            if key in self.__objects:
                del self.__objects[key]
