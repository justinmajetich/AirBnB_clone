#!/usr/bin/python3

import json


class FileStorage:
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        if cls is None:
            return FileStorage.__objects
        else:
            filtered_objects = {}
            for key, value in FileStorage.__objects.items():
                if isinstance(value, cls):
                    filtered_objects[key] = value
            return filtered_objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
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
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        if obj is not None:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            FileStorage.__objects.pop(key, None)
