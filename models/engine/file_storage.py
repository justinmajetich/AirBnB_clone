#!/usr/bin/python3
"""
module containing FileStorage used for file storage
"""
import json
import models


class FileStorage:
    """
    serializes and deserializes instances to and from JSON file
    saved into file_path

    """

    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """
        returns a dictionary containing every object
        """
        if (not cls):
            return self.__objects
        result = {}
        for key in self.__objects.keys():
            if (key.split(".")[0] == cls.__name__):
                result.update({key: self.__objects[key]})
        return result

    def new(self, obj):
        """
        creates a new object and saves it to __objects
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        update the JSON file to reflect any change in the objects
        """
        temp = {}
        for id, obj in self.__objects.items():
            temp[id] = obj.to_dict()
        with open(self.__file_path, "w") as json_file:
            json.dump(temp, json_file)

    def reload(self):
        """
        update __objects dict to restore previously created objects
        """
        try:
            with open(self.__file_path, "r") as json_file:
                temp = json.load(json_file)
            for id, dict in temp.items():
                temp_instance = models.dummy_classes[dict["__class__"]](**dict)
                self.__objects[id] = temp_instance
        except:
            pass

    def close(self):
        """display our HBNB data
        """
        self.reload()

    def delete(self, obj=None):
        """
            delete obj from __objects if it’s inside - if obj is None,
            the method should not do anything
        """
        if (obj):
            self.__objects.pop("{}.{}".format(type(obj).__name__, obj.id))
