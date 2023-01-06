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


classes = {
    'BaseModel': BaseModel, 'User': User, 'Place': Place,
    'State': State, 'City': City, 'Amenity': Amenity,
    'Review': Review
}


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        # Return only instances of cls if provided
        if cls and cls in classes.keys() or cls in classes.values():
            # if cls and cls in classes.keys():
            if cls in classes.values():
                cls = cls.__name__  # so that we are dealing with a string
            objs = {}
            # reload objects
            curr_objs = self.all()
            if curr_objs:
                for key, val in curr_objs.items():
                    if key[:key.find('.')] == cls:
                        objs[key] = val
                return objs
        # else, Return all objects
        return FileStorage.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def delete(self, obj=None):
        """Delete object"""
        # check if object exists and delete it if it does
        if obj:
            # self.reload()  # reload current objects
            if self.all():
                objs_keys = self.all().keys()
                this_key = obj.to_dict()['__class__'] + '.' + obj.id
                if this_key in objs_keys:
                    del (self.all()[this_key])
                # save objects after deletion
                self.save()

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
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass
