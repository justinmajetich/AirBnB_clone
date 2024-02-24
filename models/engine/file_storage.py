#!/usr/bin/python3
"""The module specifies a class for file management of hbnb clone """
import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.state import State
from models.place import Place
from models.user import User
from models.review import Review

classes = {"BaseModel": BaseModel, "Amenity": Amenity, "City": City, "State": State,
           "Place": Place, "Review": Review, "User": User}


class FileStorage:
    """
    The class manages storage of hbnb models in JSON format
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """It returns the dict of models stored"""
        if cls is None:
            return self.__objects
        cls_name = cls.__name__
        dct = {}
        for key in self.__objects.keys():
            if key.split('.')[0] == cls_name:
                dct[key] = self.__objects[key]
        return dct

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.__objects.update(
            {obj.to_dict()['__class__'] + '.' + obj.id: obj}
            )

    def save(self):
        """Saves storage dictionary to file"""
        with open(self.__file_path, 'w') as f:
            temp = {}
            temp.update(self.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        try:
            temp = {}
            with open(self.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """ Deletes the obj object from __objects if inside.
        Otherwise returns without doing anything."""
        if obj is None:
            return
        obj_key = obj.to_dict()['__class__'] + '.' + obj.id
        if obj_key in self.__objects.keys():
            del self.__objects[obj_key]

    def close(self):
        """call the reload method."""
        self.reload()

    def get(self, cls, id):
        """Retrieves a class object from the storage."""
        if cls is not None and type(cls) is str and id is not None and\
           type(id) is str and cls in classes:
            key = cls + '.' + id
            obj = self.__objects.get(key, None)
            return obj
        else:
            return None

    def count(self, cls=None):
        """Counts the number of instances of a specific class in storage."""
        total = 0
        if type(cls) == str and cls in classes:
            total = len(self.all(cls))
        elif cls is None:
            total = len(self.__objects)
        return total
