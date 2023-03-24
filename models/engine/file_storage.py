#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def delete(self, obj=None):
        """ Delete a instance obj """
        if obj:
            obj = obj.to_dict()
            key = f"{obj['__class__']}.{obj['id']}"
            del self.__objects[key]
	    	
    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls:
            cls = str(cls).split(" ")[1].split(".")[-1][:-2]
            
            __obj = {}
            for k, v in self.__objects.items():
                new_k = f"{cls}.{v.id}"
                if new_k == k:
                    __obj[k] = v
            return __obj
        return FileStorage.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        __dict = obj.to_dict()
        key = f"{__dict['__class__']}.{__dict['id']}"
        self.__objects[key] = obj

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            for key, val in self.__objects.items():
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
