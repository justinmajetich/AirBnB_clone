#!/usr/bin/python3
"""This is the file storage class for AirBnB"""
import json

from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """This class serializes instances to a JSON file and
    deserializes JSON file to instances
        Attributes:
                __file_path: path to the JSON file
                        __objects: objects will be stored
                            """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """returns a dictionary
                                    Return:
                                            returns a dictionary of __object
                                                    """
        if cls is None:
            return self.__objects.copy()
        else:
            return {key: obj
                    for key, obj in self.__objects.items()
                    if type(obj) is cls}

    def new(self, obj):
        """sets __object to given obj
                                                            Args:
                                                                        obj: given object
                                                                                """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def delete(self, obj=None):
        """delete obj from __objects
                                                                                        """
        if isinstance(obj, BaseModel):
            key = "{}.{}".format(type(obj).__name__, obj.id)
            if key in self.__objects:
                del self.__objects[key]

    def save(self):
        """serialize data to the JSON file
                                                                                                """
        new_dict = {key: obj.to_dict()
                    for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(new_dict, f)

    def reload(self):
        """deserialize data from the JSON file
                                                                                                        """
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                for key, value in (json.load(f)).items():
                    value = eval(value["__class__"])(**value)
                    self.__objects[key] = value
        except FileNotFoundError:
            pass

    def close(self):
        """alias for reload
                                                                                           """
        self.reload()
