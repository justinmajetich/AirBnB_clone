#!/usr/bin/python3
import os.path
import json
import os
"""
Module file_storage
Contains a class FileStorage
that serializes instances to a JSON file and
deserializes JSON file to instances
"""


class FileStorage():
    """
    that serializes instances to a JSON file and deserializes JSON file
    """
    ''' initializing values '''
    __file_path = "file.json"
    __objects = {}

    def all(self):
        ''' returns the dictionary __objects '''
        return self.__objects

    def new(self, obj):
        ''' sets in __objects the obj with key <obj class name>.id '''
        if obj:
            ''' adds the object and the key to __objects if the obj exists '''
            name = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[name] = obj

    def save(self):
        ''' serializes __objects to the JSON file (path: __file_path) '''
        my_dict = {}

        for keys, val in self.__objects.items():
            ''' serialize each object using the key '''
            my_dict[keys] = val.to_dict()

        with open(self.__file_path, "w") as my_file:
            json.dump(my_dict, my_file)

    def reload(self):
        ''' deserializes/loads the JSON file to __objects '''

        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        my_dict = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
        }
        if not os.path.isfile(self.__file_path):
            return
        with open(self.__file_path, "r") as file_path:
            objects = json.load(file_path)
            self.__objects = {}
            for key in objects:
                name = key.split(".")[0]
                self.__objects[key] = my_dict[name](**objects[key])
