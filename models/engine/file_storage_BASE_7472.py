#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""


import json
import os
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
<<<<<<< HEAD
=======

from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

classes = {
    'BaseModel': BaseModel, 'User': User, 'Place': Place,
    'State': State, 'City': City, 'Amenity': Amenity,
    'Review': Review
}
>>>>>>> origin/chalo


class FileStorage:
    """ This class manages storage of hbnb models in JSON format

    Attributes:
        __file_path (str): path to the JSON file
        __objects (dict): object storage structure

    """
    __file_path = os.path.relpath('file.json')
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
<<<<<<< HEAD
        dictionary = {}
        if cls:
            for k, o in FileStorage.__objects.items():
                if cls == str(k).split('.')[0]:
                    dictionary.update({k: o})
            return dictionary
        else:
            return FileStorage.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({f"{obj.__class__.__name__}.{obj.id}": obj})
=======
<<<<<<< HEAD
        if cls is not None:
            newDict = dict()
            for k, v in self.__objects.items():
                if cls == v.__class__.__name__ or cls == v.__class__:
                    newDict[k] = v
                return newDict
            return self.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        if obj is not None:
            key = "{}.{}".format(
                obj.__class__.__name__, obj.id
            )
            self.__objects[key] = obj
=======
        dictionary = {}
        if cls:
            for k, o in FileStorage.__objects.items():
                if cls == str(k).split('.')[0]:
                    dictionary.update({k: o})
            return dictionary
        else:
            return FileStorage.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
<<<<<<< HEAD
        self.all().update({f"{obj.to_dict()['__class__']}.{obj.id}": obj})
>>>>>>> e3800d5 (Update class models)
=======
        self.all().update({f"{obj.__class__.__name__}.{obj.id}": obj})
>>>>>>> 40846c0 (Update storage engines)
>>>>>>> origin/chalo

    def save(self):
        """Saves storage dictionary to file"""
        all_obj = dict()
        for k in self.__objects:
            all_obj[k] = self.__objects[k].to_dict()

        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(all_obj, f)

    def reload(self):
        """Loads storage dictionary from file"""
        classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
        }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
<<<<<<< HEAD
            for val in temp.values():
                self.new(classes[val['__class__']](**val))
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            pass

    def delete(self, obj=None):
        """ Deletes object from __objects """
        if obj:
=======
<<<<<<< HEAD
<<<<<<< HEAD
                for key, val in temp.items():
                        self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
=======
            for key, val in temp.items():
                self.all()[key] = classes[val['__class__']](**val)
=======
            for val in temp.values():
                self.new(classes[val['__class__']](**val))
>>>>>>> d110871 (Update class and database engine models)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
>>>>>>> 40846c0 (Update storage engines)
            pass
<<<<<<< HEAD
=======

    def delete(self, obj=None):
        """ Deletes object from __objects """
<<<<<<< HEAD
        if obj is not None:
<<<<<<< HEAD
            obj_name = f"{obj.to_dict()['__class__']}.{obj.id}"
            if obj_name in self.__objects.keys():
                del self.__objects[obj_name]
>>>>>>> e3800d5 (Update class models)
=======
=======
        if obj:
>>>>>>> d110871 (Update class and database engine models)
>>>>>>> origin/chalo
            obj_name = f"{obj.__class__.__name__}.{obj.id}"
            if FileStorage.__objects.get(obj_name):
                del FileStorage.__objects[obj_name]
        self.save()
<<<<<<< HEAD
=======
>>>>>>> 40846c0 (Update storage engines)
>>>>>>> origin/chalo
