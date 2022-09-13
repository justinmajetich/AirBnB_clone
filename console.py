#!/usr/bin/python3
"""The console"""


import cmd
import shlex
import models
from models.amenity import Amenity
from models.base_model import BaseModel
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

classes = {
    "BaseModel": BaseModel,
    "User": User,
    "Amenity": Amenity,
    "State": State,
    "Place": Place,
    "Review": Review,
}


class HBNBCommand(cmd.Cmd):
    """An entry point for the airbnb clone HBNB CLI"""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """quits the console program"""
        return True

    def do_EOF(self, arg):
        """Exits the console"""
        return True

    def emptyline(self):
        """overite/skip the emptyline method"""
        return False

    def _key_value_parser(self, args):
        """creates a dictionary from a list of strings"""
        new_dict = {}
        for arg in args:
            if "=" in arg:
                kvp = arg.split("=", 1)
                key = kvp[0]
                value = kvp[1]
                if value[0] == value[-1] == '"':
                    value = shlex.split(value)[0].replace("_", " ")
                else:
                    try:
                        value = int(value)
                    except:
                        try:
                            value = float(value)
                        except:
                            continue
                new_dict[key] = value
        return new_dict

    def do_create(self, arg):
        """Usage: create <class> <key 1>=<value 2> <key 2>=<value 2> ...
        Create a new class instance with given keys/values and print its id.
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in classes:
            new_dict = self._key_value_parser(args[1:])
            instance = classes[args[0]](**new_dict)
            models.storage.new(instance)
            models.storage.save()
        else:
            print("** class doesn't exist **")
            return False
        print(instance.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance
        based on the class name and id.
        Ex: $ show BaseModel 1234-1234-1234.
        """
        args = shlex.split(arg)
        if len(arg) == 0:
            print("** class name missing **")
            return False
        if args[0] in classes:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in models.storage.all():
                    print(models.storage.all()[key])
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """
        Delets an instance base on the class name and id
        saves changes in a JSON file.
        Ex: $ destroy BaseModel 1234-1234-1234
        """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] in classes:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in models.storage.all():
                    models.storage.all().pop(key)
                    models.storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** instace id missing **")
        else:
            print("** class name missing **")

    def do_all(self, arg):
        """
        Prints a list of strings (string representation) of all instances
        based on either the class name or not
        Ex: $ all BaseModel or $ all.
        """
        args = shlex.split(arg)
        instance_list = []
        if len(args) == 0:
            for value in models.storage.all().values():
                instance_list.append(str(value))
            print("[", end="")
            print(", ".join(instance_list), end="")
            print("]")
        elif args[0] in classes:
            for key in models.storage.all():
                if args[0] in key:
                    instance_list.append(str(models.storage.all()[key]))
            print("[", end="")
            print(", ".join(instance_list), end="")
            print("]")
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """
        updates an instance based on the class name and id
        Adds or updates an attribute & saves changes in the JSON file
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] in classes:
            if len(args) > 1:
                k = args[0] + "." + args[1]
                if k in models.storage.all():
                    if len(args) > 2:
                        if len(args) > 3:
                            setattr(models.storage.all()[k], args[2], args[3])
                            models.storage.all()[k].save()
                        else:
                            print("** value missing **")
                    else:
                        print("** attribute name missing **")
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
