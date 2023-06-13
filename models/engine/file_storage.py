#!/usr/bin/python3
"""
Define the class ``FileStorage`` for serializing and deserailizing
instances from file to JSON, vice versa
"""

import json


class FileStorage():
    """
    Serialize instances to JSON file and deserialze JSON file to instances
    """
    __file_path = "file.json"   # Path to the JSON file
    __objects = dict()      # Stores all objects by <class name>.id

    def all(self, cls=None):
        """
        Return a dictionary of objects currently in storage
        cls (optional): The class of objects to return
        """
        if cls is None:
            return FileStorage.__objects

        # cls is not None
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        all_objs = dict()
        for key, obj in FileStorage.__objects.items():
            if type(obj) == cls:
                all_objs.update({key: obj})

        return all_objs

    def new(self, obj):
        """
        Set in ``__objects the ``obj`` with the key ``<obj class name>.id``

        Where, object is an instance of ``<obj class name>``
        """
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """
        Serialize ``__objects`` to the JSON file ``__file_path``
        """
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """
        Deserialize the JSON file to ``__objects``
        """
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
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """
        Delete an instance from `__objects` collection

        Note: if obj is None or obj is not in self.__objects, do nothing
        """
        if obj is None:
            return

        for key, value in FileStorage.__objects.items():
            if value == obj:
                FileStorage.__objects.pop(key)
                return
