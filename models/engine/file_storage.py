#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is None:
            return FileStorage.__objects
        return {k: v for k, v in FileStorage.__objects.items()
                if isinstance(v, cls)}

    def new(self, obj):
        """Adds new object to storage dictionary"""
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            new_dict = {}
            for key, value in FileStorage.__objects.items():
                new_dict[key] = value.to_dict()
            json.dump(new_dict, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {'BaseModel': BaseModel, 'User': User, 'Place': Place,
                   'State': State, 'City': City, 'Amenity': Amenity,
                   'Review': Review}

        try:
            with open(FileStorage.__file_path, mode='r') as f:
                dict_reloaded = json.load(f)
                for key, value in dict_reloaded.items():
                    name_class = value["__class__"]
                    if name_class in classes:
                        instance = classes[name_class](**value)
                        key = "{}.{}".format(name_class, value["id"])
                        FileStorage.__objects[key] = instance
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Delete obj From dictionary"""
        if obj is None:
            return
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        if key in self.__objects:
            del self.__objects[key]
            self.save()