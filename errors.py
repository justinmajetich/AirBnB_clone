#!/usr/bin/python3
"""Module containing all the error handlers for the console
"""
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
import inspect


class Errors_():
    """class containing all error methods
    """
    def error_checker(cmd_name, arg):
        """Select the error handlers corresponding
        """
        tuple_args = tuple(arg.split())

        if Errors_.class_checker(cmd_name, tuple_args) is False:
            return False
        if cmd_name != 'create' and cmd_name != "all" and cmd_name != "count":
            if Errors_.id_checker(tuple_args) is False:
                return False
        if cmd_name == 'update':
            if Errors_.attribute_checker(tuple_args) is False:
                return False
        return True

    def class_checker(cmd_name, tuple_args):
        """ Validate first arg if its a class
        If cmd_name is all, only check tuple_args[0] if the arg[0] exists
        in the list (meaning len(tuple_args) > 0)
        """
        if len(tuple_args) == 0 and cmd_name != "all":
            print("** class name missing **")
            return False
        if cmd_name != "all" or len(tuple_args) > 0:
            try:
                inspect.isclass(eval(tuple_args[0]))
            except Exception:
                print("** class doesn't exist **")
                return False
        return True

    def id_checker(tuple_args):
        """Validate second arg if the id  matches an object
        """
        if len(tuple_args) < 2:
            print("** instance id missing **")
            return False
        if tuple_args[0] + "." + tuple_args[1] not in storage.all():
            print("** no instance found **")
            return False
        return True

    def attribute_checker(tuple_args):
        """Validate third arg and fourth arg
        if the attribute name and attribute value are valid
        """
        if len(tuple_args) < 3:
            print("** attribute name missing **")
            return False
        if len(tuple_args) < 4:
            print("** value missing **")
            return False
        return True
