#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""

    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is None:
            return FileStorage.__objects
        else:
            # fmt: off
            return {key: my_object 
                    for key, my_object
                    in FileStorage.__objects.items()
                    if isinstance(my_object, cls)}
            # fmt: on

    def new(self, obj):
        """Adds new object to storage dictionary"""
        # fmt: off
        self.all().update(
            {obj.to_dict()["__class__"] + "." + obj.id: obj})
        # fmt: on

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, "w") as file:
            dictionary_to_json = {}
            dictionary_to_json.update(FileStorage.__objects)
            for key, my_object in dictionary_to_json.items():
                dictionary_to_json[key] = my_object.to_dict()
            json.dump(dictionary_to_json, file)

    def reload(self):
        """Loads storage dictionary from file.json"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        cls_dictionary = {
            "BaseModel": BaseModel,
            "User": User,
            "Place": Place,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Review": Review,
        }

        try:
            dict_from_json = {}
            with open(FileStorage.__file_path, "r") as file:
                dict_from_json = json.load(file)
                for key, obj_dictionary in dict_from_json.items():
                    class_name = obj_dictionary["__class__"]
                    class_to_call = cls_dictionary[class_name]
                    self.__objects[key] = class_to_call(**obj_dictionary)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Deletes obj from __objects"""
        if obj is not None:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            del FileStorage.__objects[key]
