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
        with open(FileStorage.__file_path, "w") as f:
            dict_for_json = {}
            dict_for_json.update(FileStorage.__objects)
            for key, obj in dict_for_json.items():
                dict_for_json[key] = obj.to_dict()
            json.dump(dict_for_json, f)

    def reload(self):
        """Loads storage dictionary from file.json"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes_dict = {
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
            with open(FileStorage.__file_path, "r") as f:
                dict_from_json = json.load(f)
                for key, obj_dictionary in dict_from_json.items():
                    class_name = obj_dictionary["__class__"]  # Get class name
                    class_to_call = classes_dict[class_name]
                    self.__objects[key] = class_to_call(**obj_dictionary)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Deletes obj from __objects"""
        if obj is not None:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            del FileStorage.__objects[key]
