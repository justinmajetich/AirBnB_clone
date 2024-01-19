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

    classes = {
                        'BaseModel': BaseModel,
                        'User': User,
                        'Place': Place,
                        'State': State,
                        'City': City,
                        'Amenity': Amenity,
                        'Review': Review
                    }

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls:
            if type(cls) == str:
                # cls = eval(cls) security vulnerability
                cls = globals()[cls]
                cls_dict = {}
                for key, value in self.__objects.items():
                    if type(value) == cls:
                        cls_dict[key] = value
                return cls_dict
        return self.__objects

    def new(self, obj):
        """Adds new object to storage dictionary
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})"""
        self.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj

    def save(self):
        """Saves storage dictionary to file
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)"""
        with open(FileStorage.__file_path, 'w', encoding="utf-8") as file:
            json.dump({key: value.to_dict() for key,
                       value in FileStorage.__objects.items()}, file)

    def reload(self):
        """Loads storage dictionary from file


        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State,
                    'City': City,
                    'Amenity': Amenity,
                    'Review': Review
                }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                        self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass"""
        try:
            # os.path.exists(FileStorage.__file_path)
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                # print("hereee")
                new_dict = json.load(file)
                for key, value in new_dict.items():
                    obj = eval(value["__class__"])(**value)
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """delete obj in __objects"""
        if obj:
            key = f"{obj.__class__.__name__}.{obj.id}"
            try:
                del self.__objects[key]
            except KeyError:
                pass

    def close(self):
        """Call the reload method."""
        self.reload()
