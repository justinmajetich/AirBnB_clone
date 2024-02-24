#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
import os


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is None:
            return FileStorage.__objects
        else:
            filtered_objects = {}
            for key, obj in FileStorage.__objects.items():
                if isinstance(obj, cls):
                    filtered_objects[key] = obj
            return filtered_objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            for key, val in FileStorage.__objects.items():
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
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    cls_name = val['__class__']
                    cls = classes.get(cls_name)
                    if cls:
                        self.__objects[key] = cls(**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Deletes obj from __objects if it's inside"""
        if obj is not None:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            if key in FileStorage.__objects:
                del FileStorage.__objects[key]


if __name__ == "__main__":
    fs = FileStorage()

    # All States
    all_states = fs.all(State)
    print("All States: {}".format(len(all_states.keys())))
    for state_key in all_states.keys():
        print(all_states[state_key])

    # Create a new State
    new_state = State()
    new_state.name = "California"
    fs.new(new_state)
    fs.save()
    print("New State: {}".format(new_state))

    # All States
    all_states = fs.all(State)
    print("All States: {}".format(len(all_states.keys())))
    for state_key in all_states.keys():
        print(all_states[state_key])

    # Create another State
    another_state = State()
    another_state.name = "Nevada"
    fs.new(another_state)
    fs.save()
    print("Another State: {}".format(another_state))

    # All States
    all_states = fs.all(State)
    print("All States: {}".format(len(all_states.keys())))
    for state_key in all_states.keys():
        print(all_states[state_key])

    # Delete the new State
    fs.delete(new_state)


    # All States
    all_states = fs.all(State)
    print("All States: {}".format(len(all_states.keys())))
    for state_key in all_states.keys():
        print(all_states[state_key])
