#!/usr/bin/python3
import json
'''
module - file_storage:
this module defines a class to manage file storage for hbnb clone
'''


class FileStorage:
    '''class manages storage of hbnb models in JSON format
    '''
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        '''all
        returns a list of objects of one type of if class name arg exist
        else returns dictionary of models currently in storage
        '''
        if cls:
            cls_objects = {}
            for key, value in self.__objects.items():
                if isinstance(value, cls):
                    cls_objects[key] = value
            return cls_objects
        else:
            return FileStorage.__objects

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
        '''delete
        remove/delete an object from __objects if it exists
        '''
        if obj is not None:
            obj_key = f'{obj.__class__.__name__}.{obj.id}'
            if obj_key in self.__objects:
                del self.__objects[obj_key]
        else:
            pass

    def close(self):
        '''This refreshes the FileStorage'''
        self.reload()
