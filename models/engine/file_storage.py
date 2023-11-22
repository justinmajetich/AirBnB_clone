#!/usr/bin/python3
"""
this module defines a class to manage file storage for hbnb clone
"""
import json


class FileStorage:
    """class manages storage of hbnb models in JSON format
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns the dictionary __objects."""
        if cls:
            key = '{}.'.format(cls.__name__)
            return {k: v for k, v in self.__objects.items() if
                    k.startswith(key)}
        return self.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        data = {k: obj.to_dict() for k, obj in
                self.__objects.items()}
        with open(self.__file_path, "w") as f:
            json.dump(data, f)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review
        try:
            with open(self.__file_path) as f:
                data = f.read()
                if not data:  # empty file
                    return
                obj_dict = json.loads(data)
                for o in obj_dict.values():
                    cls_name = o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return

    def delete(self, obj=None):
        """Deletes an object from the storage"""
        if obj is None:
            return
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        if key in self.__objects:
            del self.__objects[key]
        self.save()

    def close(self):
        """This refreshes the FileStorage"""
        self.reload()
