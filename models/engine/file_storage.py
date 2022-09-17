#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format."""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage.
        args:
            cls: Name of model to return.
        """
        if cls is None:
            return FileStorage.__objects
            
        if type(cls) == str:
                cls = eval(cls)
        d = {}
        for k, v in self.__objects.items():
            if type(v) == cls:
                d[k] = v
        return d

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        dictionary = {}
        for key, obj in self.__objects.items():
            dictionary[key] = obj.to_dict()
        with open(self.__file_path, "w") as json_file:
            json.dump(dictionary, json_file, ensure_ascii=False)

    def delete(self, obj=None):
        """Removes on instance from self.__objects if obj != None."""
        if obj is None:
            return
        for k, v in self.__objects.items():
            if obj == v:
                del self.__objects[k]
                break

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

    def close(self):
        """Deserializes the JSON file to objects."""
        self.reload()
        