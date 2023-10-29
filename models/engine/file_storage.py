#!/usr/bin/python3
# KASPER edited at 9:17 am 10/28/2023
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is not None:   # if cls was passed
            all_class = {}    # make empty dictionary
            for objs in FileStorage.__objects:  # for each item in __objects
                # if the type of the object stored in __objects is
                # the same as cls
                if type(FileStorage.__objects[objs]) == cls:
                    # update the new dictionary  with the objects that match
                    # the class
                    all_class.update({objs: FileStorage.__objects[objs]})
            return all_class   #return the new dictionary
        else:   # if cls was not passed
            return FileStorage.__objects  # return __objects

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
        """ removes a key value pair stored in __objects """
        if obj is not None:    # check if obj was passed, if yes
            key = obj.to_dict()['__class__'] + '.' + obj.id    # make key
            if key in self.__objects:   #if the key is in __objects, delete they key value pair
                self.__objects.pop(key)
        else:     #if not, do nothing
            pass
