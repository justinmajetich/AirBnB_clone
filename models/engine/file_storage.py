#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """returns the list of objects of one type of class."""
        if cls is not None:
            new_list = []
            for obj in FileStorage.__objects.values():
                if isinstance(obj, cls) and (isinstance(
                    cls, type) and obj.__class__.__name__ == cls or
                    isinstance(cls, str) and obj.__class__.__name__ == cls):
                    new_list.append(obj)
            return new_list
        else:
            return list(FileStorage.__objects.values())

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
        public instance method to delete obj from 
        __objects which is a dictionary
        obj: The object to be deleted. no action is taken if obj is None
        """
        if obj is not None:
            dictionary_key = "{}.{}".format(obj.__class__.__name__, obj.id)
            if dictionary_key in __objects:
                del self.__objects[dictionary_key]
            else:
                pass
