#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        """
       !!! Objects printed in do_all console func have quotes !!!

"""
        #print("from all obj={}".format(FileStorage.__objects))
        if cls is None:
            return FileStorage.__objects
        else:
            return {k: v for k, v in FileStorage.__objects.items() if isinstance(v, cls)}

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

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
            temp = {}
            print(type(temp))
            with open(FileStorage.__file_path, 'r', encoding="UTF-8") as f:
                """Json is recieving None val here """
                print(type(f))
                print("temp in with{}".format(temp))
                temp = json.load(f)
                print("2nd temp in with{}".format(temp))
                for key, val in temp.items():
                        self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """delete obj from storage"""
        if obj is None:
            return
        try:
            del self.__objects["{}.{}".format(type(obj).__name__, obj.id)]
        except KeyError:
            pass
