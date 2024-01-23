#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json

class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def delete(self, obj=None):
        """
        to delete obj from __objects if its inside-
        if obj is equal to None, the method should
        not do anything.
        """
        if obj is None:
            return
        obj_id = obj.id
        obj_class_name = type(obj).__name__
        obj_key = f"{obj_class_name}.{obj_id}"
        del self.all()[obj_key]

    def all(self, cls=None):
        """
        Returns a dictionary of models currently in storage
        if cls == None or that returns the list of 
        objects of one type of class if cls == a classname
        """
        if cls is None:
            return FileStorage.__objects
        obj_list = {
            key: self.all()[key]
            for key in list(self.all())
            if cls.__name__ in key
        }

        return obj_list

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
