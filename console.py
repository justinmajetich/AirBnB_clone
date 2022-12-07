#!/usr/bin/python3
"""program that contains the entry point of the command interpreter"""

import cmd
import shlex
import sys
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class HBNBCommand(cmd.Cmd):
    """Program that contains the entry point of the command interpreter"""

    prompt = '(hbnb) '
    intro = 'Welcome to AirBnB console program.\n'

    list_of_class = ["BaseModel", "User", "Amenity", "City",
                     "Place", "Review", "State"]

    def do_create(self, arg):
        """\nCreates a new class instance.\nUsage: create <class name> \
attributes<key="value"> ...\nNB: Some classes have mandatory attributes. Run object_names command.\n"""
        if not arg:
            print("** class name missing **")
            return
        args = shlex.split(arg)  # Splits arg by shell lexical analysis style
        args_py = arg.split()   # Splits arg by python lexical analisys style
        if args[0] not in self.list_of_class:
            print("** class doesn't exist **")
            return
        else:
            new_inst = eval(args[0] + "()")
            for i in range(1, len(args)):
                param_key = args[i].split("=")[0]
                param_val = (args[i].split("=")[1])
                try:
                    try:
                        # Cast to int if value is int
                        param_val = int(param_val)
                    except ValueError:
                        # Cast to float if value is float
                        param_val = float(param_val)
                except ValueError:
                    if (args_py[i].split("=")[1][0] != "\""):  # Is string in ""?
                        tmp = "{} could not be created!"
                        tmp2 = "String value must be in double quotes."
                        tmp3 = tmp + tmp2
                        print(tmp3.format(args_py[i]))
                        continue
                    # Else value remains as string
                    param_val = param_val.replace("_", " ")
                setattr(new_inst, param_key, param_val)
            new_inst.save()
            print(new_inst.id)
        return

    def do_show(self, arg):
        """\nPrints the string representation of an instance based \
on the class name and id.\nUsage: show <class name> <id>\n"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in self.list_of_class:
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        else:
            try:
                tmp = args[0] + '.' + args[1]
                print(storage.all()[tmp])
            except KeyError:
                print("** no instance found **")
            finally:
                return

    def do_destroy(self, arg):
        """\nDeletes a class instance based on the class name and id.
Usage: destroy <class name> <id>\n"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in self.list_of_class:
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        else:
            try:
                tmp = args[0] + '.' + args[1]
                storage.all().pop(tmp)
                storage.save()
            except:
                print("** no instance found **")
            finally:
                return

    def do_all(self, arg):
        """\nPrints string representation of all instances in storage.
Usage 1 (all class instances): all\nUsage 2 (specific class instances): all <class name>\n"""
        if not arg:
            dic_str_list = []
            for key, value in storage.all().items():
                dic_str_list.append(str(value))
            if dic_str_list != []:
                print(dic_str_list)
                return
            else:
                print("Sorry, storage is empty!")
                return
        else:
            args = arg.split()
            if args[0] in self.list_of_class:
                dic_str_list = []
                for key, value in storage.all().items():
                    if str(key.split(".")[0]) == args[0]:
                        dic_str_list.append(str(value))
                if dic_str_list != []:
                    print(dic_str_list)
                    return
                else:
                    print(
                        "Sorry, no instance of \"{}\" exists in storage!".format(args[0]))
                    return
            else:
                print("** class doesn't exist **")
                return

    def do_update(self, arg):
        """\nUpdates an instance based on the class name and id.
Usage: update <class name> <id> <attribute name> "<attribute value>"\n"""
        if not arg:
            print("** class name missing **")
            return
        args = shlex.split(arg)
        if args[0] not in self.list_of_class:
            print("** class doesn't exist **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        else:
            try:
                tmp = args[0] + "." + args[1]
                storage.all()[tmp]
            except:
                print("** no instance found **")
                return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        elif len(args) == 3:
            print("** value missing **")
            return
        else:
            tmp = args[0] + "." + args[1]
            try:
                try:
                    value = int(args[3])  # Cast to int if value is int
                except ValueError:
                    value = float(args[3])  # Cast to float if value is float
            except ValueError:
                value = args[3].strip(":\"'")  # Else value remains as string
            attr = args[2].strip(":\"'")
            setattr(storage.all()[tmp], attr, value)
            storage.save()

    def preloop(self):
        """Initialization prompter"""
        self.onecmd("help")
        return

    def emptyline(self):
        """Do nothing if no command is given"""
        return False

    def do_quit(self, arg):
        """\nExits the program.\nUsage: quit\n"""
        return True

    def do_EOF(self, arg):
        """\nExits the program.\nUsage 1: EOF\nUsage 2: Ctrl + D\n"""
        return True

    def default(self, line):
        """Initiates response to an invalid command line"""
        print("\"{}\": is not a valid action of AirBnB console program!".format(line))
        return

    def do_object_names(self, arg):
        """
        Prints a list of all object/class names available for instantiation.
        Usage: object_names
        """
        print(self.list_of_class)
        attr_layout = """
            Here is a breakdown of all mandatory attributes associated with
            each object:
            User:
                mandatory: email, password
                optional: first_name, last_name
            State:
                mandatory: name
            Place:
                mandatory: city_id, user_id, name, number_rooms, 
                        number_bathrooms, max_guest, price_by_night
                optional: description, latitude, longitude
            Review:
                mandatory: place_id, user_id, text
            City
                mandatory: name, state_id,
            Amenity
                mandatory: name
            Base_model
                dev purposes only! no mandatory attributes
            """
        print(attr_layout)
        return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
