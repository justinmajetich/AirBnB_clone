#!/usr/bin/python3
"""This module defines a class to manage file storage for HBNB clone"""
import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """This class manages storage of HBNB models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns the dictionary __objects"""
        # Code for all method

    def new(self, obj):
        """Adds new object to storage dictionary"""
        # Code for new method

    def save(self):
        """Saves storage dictionary to file"""
        # Code for save method

    def reload(self):
        """Loads storage dictionary from file"""
        # Code for reload method

    def delete(self, obj=None):
        """Method that deletes obj from __objects"""
        # Code for delete method

    def close(self):
        """
        Closes the session
        """
        # Code for close method

