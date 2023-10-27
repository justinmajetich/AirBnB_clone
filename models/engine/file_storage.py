#!/usr/bin/python3
"""file storage class for AirBnBV2"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """Serializes instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Returns all the valid objects"""

        if cls:
            same_type = dict()

            for key, obj in self.__objects.items():
                if obj.__class__ == cls:
                    same_type[key] = obj

            return same_type

        return self.__objects

    def new(self, obj):
        """sets obj to the objects"""
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """Saveto JSON file path"""
        my_dict = {}
        for key, value in self.__objects.items():
            my_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(my_dict, f)

    def reload(self):
        """Serial the paths to json"""
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                for key, value in (json.load(f)).items():
                    value = eval(value["__class__"])(**value)
                    self.__objects[key] = value
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Delete objest inside if there"""
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)

            if self.__objects[key]:
                del self.__objects[key]
                self.save()

    def close(self):
        """Deserialize into obj in json"""
        self.reload()
