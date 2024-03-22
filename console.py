#!/usr/bin/python3
"""
Console Module
"""
import cmd
import sys
from models.base_model import BaseModel
from models.__init__ import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    Contains the functionality for the HBNB console
    """

    prompt = '(hbnb) '

    classes = {
        'BaseModel': BaseModel, 'User': User, 'Place': Place,
        'State': State, 'City': City, 'Amenity': Amenity,
        'Review': Review
    }
    dot_cmds = ['all', 'count', 'show', 'destroy', 'update']
    types = {
        'number_rooms': int, 'number_bathrooms': int,
        'max_guest': int, 'price_by_night': int,
        'latitude': float, 'longitude': float
    }

    def do_quit(self, command):
        """Method to exit the HBNB console"""
        exit()

    def do_EOF(self, arg):
        """Handles EOF to exit program"""
        exit()

    def emptyline(self):
        """Overrides the emptyline method of CMD"""
        pass

    def _create_dict_instance(self, line):
        """
        Parse input and convert it to Dict for do_create
        """
        new_dict = {}
        for item in line:
            if "=" in item:
                new_arg = item.split("=", 1)
                key = new_arg[0]
                value = new_arg[1]
                if value[0] == '"' == value[-1]:
                    value = value.replace('"', "").replace("_", " ")
                else:
                    try:
                        value = int(value)
                    except Exception:
                        try:
                            value = float(value)
                        except Exception:
                            continue
                new_dict[key] = value
        return new_dict

    def do_create(self, args):
        """Create an object of any class"""
        args = args.split()
        if not args[0]:
            print("** class name missing **")
            return
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        new_dict = self._create_dict_instance(args[1:])
        new_instance = HBNBCommand.classes[args[0]](**new_dict)
        print(new_instance.id)
        new_instance.save()

    def do_count(self, args):
        """Count current number of class instances"""
        count = 0
        for k in storage.all().keys():
            if args == k.split('.')[0]:
                count += 1
        print(count)

    def do_update(self, args):
        """Updates a certain object with new info"""
        # Code for update method

    def do_show(self, arg):
        """
        Show command to Prints the string representation of an instance based
        on the class name and id
        """
        # Code for show method

    def do_destroy(self, arg):
        """
        Destroy command to Deletes an instance based on the class name and id
        """
        # Code for destroy method

    def do_all(self, arg):
        """Prints string representations of instances"""
        # Code for all method


if __name__ == "__main__":
    HBNBCommand().cmdloop()

