#!/usr/bin/python3

import json


class FileStorage:
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
<<<<<<< HEAD
=======
        """Returns a dictionary or list of models currently in storage"""
>>>>>>> dd568910edba756fb6434455eb1b9f67ab495477
        if cls is None:
            return FileStorage.__objects
        else:
            filtered_objects = {}
            for key, value in FileStorage.__objects.items():
<<<<<<< HEAD
                if isinstance(value, cls):
=======
                class_name = key.split('.')[0]
                if class_name == cls.__name__:
>>>>>>> dd568910edba756fb6434455eb1b9f67ab495477
                    filtered_objects[key] = value
            return filtered_objects

    def new(self, obj):
<<<<<<< HEAD
=======
        """Adds new object to storage dictionary"""
>>>>>>> dd568910edba756fb6434455eb1b9f67ab495477
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
<<<<<<< HEAD
        temp_dict = {}
        for key, value in FileStorage.__objects.items():
            temp_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(temp_dict, file)

    def reload(self):
        try:
            with open(FileStorage.__file_path, 'r') as file:
                temp_dict = json.load(file)
                for key, value in temp_dict.items():
                    cls_name = value['__class__']
                    cls = eval(cls_name)
                    FileStorage.__objects[key] = cls(**value)
=======
        """Saves storage dictionary to file"""
        temp = {}
        for key, val in FileStorage.__objects.items():
            temp[key] = val.to_dict()
        with open(FileStorage.__file_path, 'w') as f:
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
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    class_name = val['__class__']
                    obj = classes[class_name](**val)
                    FileStorage.__objects[key] = obj
>>>>>>> dd568910edba756fb6434455eb1b9f67ab495477
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
<<<<<<< HEAD
        if obj is not None:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            FileStorage.__objects.pop(key, None)
=======
        """Deletes obj from __objects if it exists"""
        if obj is not None:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            if key in FileStorage.__objects:
                del FileStorage.__objects[key]
>>>>>>> dd568910edba756fb6434455eb1b9f67ab495477
