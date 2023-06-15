#!/usr/bin/python3
# This module defines a class to manage file storage for hbnb clone


import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if not cls:
            return self.__objects
        elif type(cls) == str:
            return {k: v for k, v in self.__objects.items()
                    if v.__class__.__name__ == cls}
        else:
            return {k: v for k, v in self.__objects.items()
                    if v.__class__ == cls}

    def new(self, obj):
        """Adds new object to storage dictionary"""
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj

    def save(self):
        """Saves storage dictionary to file"""
        temp = {}
        for key in self.__objects:
            temp[key] = self.__objects[key].to_dict(save_to_disk=True)
        with open(self.__file_path, 'w') as f:
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        try:
            with open(self.__file_path, 'r') as f:
                temp = json.load(f)
                for key in temp:
                    self.all()[key] = classes[temp[key]
                             ['__class__']](**temp[key])
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        ''' deletes the object obj from the attribute
            __objects if it's inside it
        '''
        if obj is None:
            return
        key = obj.to_dict()['__class__'] + '.' + obj.id
        if key in self.__objects.keys():
            del self.__objects[key]
            self.save()

    def close(self):
        """Call the reload method"""
        self.close()
