#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """
            Returns only list of instances currently in storage
            that match the value of given parameter cls

            Args:
                cls (Model): Input for a specific class value (optional)

            Attributes:
                cls (Model): support class

            Returns:
                dict
        """
        collections = {}

        if cls is not None:
            for (key, value) in FileStorage.__objects.items():
                if isinstance(value, cls):
                    collections[key] = value
            return collections
        return FileStorage.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """
            Search and remove a given obj in a list of
            instances, otherwise do nothing.

            Args:
                obj (instance obj): Input instance to delete / remove

            Attributes:
                obj (instance obj): Placeholder for obj instance

            Returns:
                None
        """
        if obj is not None:
            for (key, value) in FileStorage.__objects.items():
                if value is obj:
                    del (FileStorage.__objects[key])
                    break
