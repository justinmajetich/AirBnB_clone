#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently"""
        if cls:
            if type(cls) == str:
                cls = eval(cls)
            my_dict = {}
            for key, value in self.__objects.items():
                if type(value) == cls:
                    my_dict[key] = value
            return my_dict
        return self.__objects

    def new(self, obj):
        """Provides a new instance of a class"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Provides a save method for a class"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def delete(self, obj=None):
        """Allows to delete objects from the database"""
        if obj is not None:
            key = obj.to_dict()['__class__'] + '.' + obj.id
            self.all().pop(key, None)

    def reload(self):
        """Allows reload of the database"""
        classes = {
            'BaseModel': BaseModel,
            'User': User, 'Place': Place, 'State': State,
            'City': City, 'Amenity': Amenity, 'Review': Review
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
        """Deletes and object from __objects"""
        if (obj):
            key = "{}.{}".format(type(obj).__name__, obj.id)
            del self.__objects[key]

    def close(self):
        """
        It is important to close the file
        """
        self.reload()
