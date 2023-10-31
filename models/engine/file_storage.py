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
    "User": User,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Place": Place,
    "Review": Review
}

class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is None:
            return FileStorage.__objects
        else:
            if isinstance(cls, str):
                cls = classes.get(cls)
            filter_dict = {}
            for obj in FileStorage.__objects.values():
                if type(obj) == cls:
                    filter_dict.update({obj.to_dict()['__class__'] + "."
                                        + obj.id: obj})
            return filter_dict

    def generate_new_id(self):
        """Generate a new ID for objects with string IDs"""
        if not self.__objects:
            # If there are no existing objects, start with ID '1'
            new_id = '1'
        else:
            # Find the maximum string ID and increment it to generate a new ID
            existing_ids = [key.split('.')[1] for key in self.__objects.keys()]
            new_id = str(int(max(existing_ids)) + 1)
        return new_id

    def new(self, obj):
        """Adds new object to storage dictionary"""
        obj_id = obj.id if obj.id is not None else self.generate_new_id()
        self.all().update({obj.to_dict()
                           ['__class__'] + '.' + str(obj_id): obj})

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

    def delete(self, obj=None):
        """Deletes object from __objects if it exists"""
        if obj is not None:
            key = f"{type(obj).__class__.__name__}.{obj.id}"
            if key in self.__objects:
                del self.__objects[key]
                self.save()
