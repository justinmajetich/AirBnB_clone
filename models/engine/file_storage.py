#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """
        If cls=None, returns a dictionary of models
        currently in storage, else returns a dictionary
        of models with class=cls
        """
        # print(FileStorage.__objects)
        if cls is None:
            return FileStorage.__objects

        cls_objects = {}
        for value in FileStorage.__objects.values():
            if type(value) == cls:
                cls_objects.update({value.to_dict()['__class__'] +
                                    '.' + value.id: value})
        return cls_objects

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
        """deletes an object from __objects"""
        if obj is None:
            return
        for key, value in dict(FileStorage.__objects).items():
            if value == obj:
                del FileStorage.__objects[key]

    def close(self):  # p1170t7
        """
        Calls the reload() method for de-
        serializing the JSON file to objects.
        """
        self.reload()
