#!/usr/bin/python3
""" File Storage Module """
import json
from models.base_model import BaseModel


class FileStorage:
    """ Serializes instances to a JSON file and deserializes JSON file to instances """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """ Returns the list of objects of one type of class """
        if cls is None:
            return FileStorage.__objects
        else:
            objects_by_cls = {}
            for key, obj in FileStorage.__objects.items():
                if type(obj) == cls:
                    objects_by_cls[key] = obj
            return objects_by_cls

    def new(self, obj):
        """ Sets in __objects the obj with key <obj class name>.id """
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            FileStorage.__objects[key] = obj

    def save(self):
        """ Serializes __objects to the JSON file (path: __file_path) """
        serializable_objs = {}
        for key, obj in FileStorage.__objects.items():
            serializable_objs[key] = obj.to_dict()
        with open(FileStorage.__file_path, mode="w", encoding="utf-8") as file:
            json.dump(serializable_objs, file)

    def reload(self):
        """ Deserializes the JSON file to __objects """
        try:
            with open(FileStorage.__file_path, mode="r", encoding="utf-8") as file:
                FileStorage.__objects = json.load(file)
            for key, value in FileStorage.__objects.items():
                class_name = value['__class__']
                del value['__class__']
                obj = eval(class_name)(**value)
                self.new(obj)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """ Deletes obj from __objects if it exists """
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            if key in FileStorage.__objects:
                del FileStorage.__objects[key]
                self.save()
