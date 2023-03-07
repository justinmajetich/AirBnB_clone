#!/usr/bin/python3
"""Module console
Creating command interpreter console
"""

import cmd
import models
import re 

from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

valid_class = {
    "BaseModel": BaseModel,
    "User": User,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Place": Place,
    "Review": Review
}


class HBNBCommand(cmd.Cmd):
    """class for console"""

    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """handles end of line char"""
        print()
        return True

    def emptyline(self):
        """does nothing on enter"""
        pass

    def do_create(self, arg):
        """Creates new instance of BaseModel"""

        if len(arg) == 0:
            print("** class name missing **")
        elif arg in valid_class:
            new = valid_class[arg]()
            new.save()
            print(new.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """prints a string representation of instance"""

        if arg == "" or arg is None:
            print("** class name missing **")
        else:
            word = arg.split(' ')
            if word[0] not in valid_class:
                print("** class doesn't exist **")
            elif len(word) < 2:
                print("** instance id missing **")
            else:
                key = f'{word[0]}.{word[1]}'
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])

    def do_destroy(self, obj):
        """Deletes an instance based on class name and id"""

        if obj == "" or obj is None:
            print("** class name missing **")
        else:
            word = obj.split(' ')
            if word[0] not in valid_class:
                print("** class doesn't exist **")
            elif len(word) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(word[0], word[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()

    def do_update(self, arg):
        """updates an instance based on the class name and id"""

        list_arg = arg.split(' ')
        if arg == "" or arg is None:
            print("** class name missing **")
        elif list_arg[0] not in valid_class:
            print("** class doesn't exist **")
        elif len(list_arg) < 2:
            print("** instance id missing **")
        elif len(list_arg) < 3:
            print("** attribute name missing **")
        elif len(list_arg) < 4:
            print("** value missing **")
        else:
            obj_search = list_arg[0] + "." + list_arg[1]
            if obj_search in storage.all():
                setattr(storage.all()[obj_search], list_arg[2],
                        list_arg[3].strip('\'"'))
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """
        prints all of the string representations
        of instances
        """

        if arg != "":
            word = arg.split(' ')
            if word[0] not in valid_class:
                print("** class doesn't exist **")
            else:
                n = [
                    str(obj) for key, obj in storage.all().items()
                    if type(obj).__name__ == word[0]
                ]
                print(n)

        else:
            n = [str(obj) for key, obj in storage.all().items()]
            print(n)


if __name__ == '__main__':
    HBNBCommand().cmdloop()