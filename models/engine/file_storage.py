"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """
        Returns a dictifile_storage.pyonary
        of models currently in storage
        """
        filtered_objects = {}
        # This will be executed if cls is passed
        # It will return a new dictionary containing
        # value filtered by cls
        if cls is not None:
            # If __objects is empty return the empty filterd dictionary
            if len(FileStorage.__objects) == 0:
                return filtered_objects
            for key, val in FileStorage.__objects.items():
                if isinstance(val, cls):
                    filtered_objects[key] = val
            return filtered_objects
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
            with open(FileStorage.__file_path, 'r') as f:
                try:
                    temp = json.load(f)
                    for key, val in temp.items():
                        self.all()[key] = classes[val['__class__']](**val)
                except Exception:
                    pass
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """deletes an object from __objects"""
        temp = {}
        if obj is None:
            pass
        else:
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                if val is obj:
                    FileStorage.__objects.pop(key)
            self.save()
