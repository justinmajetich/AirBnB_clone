#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """Represent an abstracted storage engine.

    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Return a dictionary of instantiated objects in __objects.

        If a cls is specified, returns a dictionary of objects of that type.
        Otherwise, returns the __objects dictionary.
        """
<<<<<<< HEAD
        Returns a dictionary of models currently in storage
        If cls is None, returns all objects in __objects
        """
        if cls:
            dictionary = self.__objects
            for key in dictionary:
                partition = key.replace('.', '')
                partition = shlex.split(partition)
                if (partition[0] == cls.__name__):
                    dictionary[key] = self.__objects[key]
                return (dictionary)
            else:
                return self.__objects
=======
        if cls is not None:
            if type(cls) == str:
                cls = eval(cls)
            cls_dict = {}
            for k, v in self.__objects.items():
                if type(v) == cls:
                    cls_dict[k] = v
            return cls_dict
        return self.__objects
>>>>>>> 1d722d558fa05a230466edc36060ffffd780103a

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id."""
        self.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        odict = {o: self.__objects[o].to_dict() for o in self.__objects.keys()}
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(odict, f)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
<<<<<<< HEAD
            with open(self.__file_path, 'r', encoding="utf-8") as f:
                if f.readable():
                    f.seek(0)
                    data = json.load(f)
                    for key, value in data.items():
                        value = eval(value["__class__"])(**value)
                        self.__objects[key] = value
        except FileNotFoundError:
            pass
        except json.decoder.JSONDecodeError:
            pass
            """for key, value in (json.load(f)).items():
                    value = eval(value["__class__"])(**value)
                    self.__objects[key] = value
        except FileNotFoundError:
            pass"""
=======
            with open(self.__file_path, "r", encoding="utf-8") as f:
                for o in json.load(f).values():
                    name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(name)(**o))
        except FileNotFoundError:
            pass
>>>>>>> 1d722d558fa05a230466edc36060ffffd780103a

    def delete(self, obj=None):
        """Delete a given object from __objects, if it exists."""
        try:
            del self.__objects["{}.{}".format(type(obj).__name__, obj.id)]
        except (AttributeError, KeyError):
            pass

    def close(self):
        """Call the reload method."""
        self.reload()
