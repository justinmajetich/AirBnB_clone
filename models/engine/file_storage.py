#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.city import City

classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
        }


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        mydict = {}
        if cls:                
            for k, v in FileStorage.__objects.items():
                if isinstance(v, cls):
                    mydict[k] = v
            return mydict
        else:
            return FileStorage.__objects

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
                if '_sa_instance_state' in temp:
                    del temp['_sa_instance_state']
            json.dump(temp, f)

    def reload(self):
        """deseriaizes objescts"""
        try:
            with open(self.__file_path, mode='r', encoding='utf-8') as f:
                moby = json.load(f)
                for key, value in moby.items():
                    obj = eval(value['__class__'])(**value)
                    self.__objects[key] = obj

        except FileNotFoundError:
            pass
        except json.decoder.JSONDecodeError:
            pass

    def delete(self, obj=None):
        """deletes objects"""
        if obj == None:
            return
        else:
            ob = ("{}.{}").format(obj.__class__.__name__, obj.id)
            if ob in self.__objects:
                del self.__objects[ob]
                self.save()