#!/usr/bin/python3
"""This is the file storage class for AirBnB"""
import json


class FileStorage:
    '''
    Class that serializes instances to a JSON file
    '''
    __file_path= 'file.json'
    __object ={}

    def all(self, cls=None):
        """
        returns a dictionary
        """
        if cls is None:
            return self.__objects
        else:
            filtered_obj = {}
            for key, value in self.__objects.items():
                if type(value) == cls:
                    filtered_obj[key] = value
            return 
    
    def new(self, obj):
        """
        sets __object to given obj
        """
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})
    def delete(self, obj=None):
        """
        Update FileStorage, add a new instance publica
        """
        if obj is not None:
            key = key = obj.__class__.__name__ + "." + obj.id
            if key in self.__objects:
                del self.__objects[key]
                self.save()

    def save(self):
        """
        serialize the file path to JSON file path
        """
        with open(self.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """
        serialize the file path to JSON file path
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        from models.state import State
        from models.city import City 

        classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
        }
       
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    
