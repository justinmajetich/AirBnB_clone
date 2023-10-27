#!/usr/bin/python3
"""Define class FileStorage"""
import json
import models


class FileStorage:
    """Serializes instances to JSON file and deserializes to JSON file"""
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Return the dictionary"""
        obje = {}
        if cls is None:
            return (self.__objects)
        else:
            if type(cls) is str:
                cls = models.classes[cls]
            for key, val in self.__objects.items():
                if cls.__name__ == val.__class__.__name__:
                    obje[key] = val
            return (obje)

    def new(self, obj):
        """Set objects with key """
        key = str(obj.__class__.__name__) + "." + str(obj.id)
        value_dict = obj
        FileStorage.__objects[key] = value_dict

    def save(self):
        """Serializes to JSON file. """
        objects_dict = {}
        for key, val in FileStorage.__objects.items():
            objects_dict[key] = val.to_dict()

        with open(FileStorage.__file_path, mode='w', encoding="UTF8") as fd:
            json.dump(objects_dict, fd)

    def delete(self, obj=None):
        """delete objects"""
        if not obj:
            return
        key = '{}.{}'.format(type(obj).__name__, obj.id)
        if key in self.__objects:
            del self.__objects[key]
            self.save()

    def reload(self):
        """Deserializes JSON file to an object."""
        try:
            with open(FileStorage.__file_path, encoding="UTF8") as fd:
                FileStorage.__objects = json.load(fd)
            for key, val in FileStorage.__objects.items():
                class_name = val["__class__"]
                class_name = models.classes[class_name]
                FileStorage.__objects[key] = class_name(**val)
        except FileNotFoundError:
            pass

    def close(self):
        """Reload object from JSON file"""
        self.reload()
