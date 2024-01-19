#!/usr/bin/python3
"""This is the file storage class for AirBnB"""

import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import shlex

classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class FileStorage:
    """This class serializes instances to a JSON file and
    deserializes JSON file to instances
    Attributes:
        __file_path: path to the JSON file
        __objects: objects will be stored
    """
    # string - path to the JSON file
    __file_path = os.path.abspath("file.json")
    # dictionary - empty but will store all objects by <class name>.id
    __objects = {}

    def all(self, cls=None):
        """returns a dictionary
        Return:
            returns a dictionary of __object
        """
        if cls is not None:
            new_dict = {}
            for key, value in FileStorage.__objects.items():
                if cls == value.__class__ or cls == value.__class__.__name__:
                    new_dict[key] = value
            return new_dict
        return FileStorage.__objects

    def new(self, obj):
        """sets __object to given obj
        Args:
            obj: given object
        """
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            FileStorage.__objects[key] = obj

    def save(self):
        """serialize the file path to JSON file path
        """
        json_objects = {}
        for key in FileStorage.__objects:
            json_objects[key] = FileStorage.__objects[key].to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            json.dump(json_objects, f)

    def reload(self):
        """serialize the file path to JSON file path
        """
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                jo = json.load(f)
            for key in jo:
                FileStorage.__objects[key] = classes[jo[key]["__class__"]]
                (**jo[key])
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """ delete an existing element
        """
        if obj is not None:
            key = obj.__class__.__name__ + '.' + obj.id
            del FileStorage.__objects[key]

    def create_state(self, state_name):
        """Crea un nuevo estado y devuelve su ID"""
        # Generar nueva ID
        new_id = str(len(FileStorage.__objects) + 1)

        # Crear una nueva instancia de State
        new_state = State(id=new_id, name=state_name)

        # Agregar el nuevo estado al diccionario de objetos
        self.new(new_state)

        # Guardar los datos actualizados en el archivo
        self.save()

        # Devolver la nueva ID
        return new_id
