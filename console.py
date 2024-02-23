#!/usr/bin/python3
""" Console Module """
import cmd
import sys
import json
import re
import os

from models.__init__ import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class HBNBCommand(cmd.Cmd):
    """Contains the functionality for the HBNB console"""

    # determines prompt for interactive/non-interactive modes
    prompt = "(hbnb) "  # There's a prompt either ways

    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "Place": Place,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Review": Review,
    }
    dot_cmds = ["all", "count", "show", "destroy", "update"]
    types = {
        "number_rooms": int,
        "number_bathrooms": int,
        "max_guest": int,
        "price_by_night": int,
        "latitude": float,
        "longitude": float,
    }

    def precmd(self, line):
        """Reformat command line for advanced command syntax.

        Usage: <class name>.<command>([<id> [<*args> or <**kwargs>]])
        (Brackets denote optional fields in usage example.)
        """
        _cmd = _cls = _id = _args = ""  # initialize line elements
        _dict = re.search(r'{.+}', line)
        group1 = r'(?<=\.)[^(]+|[aA-zZ]+(?=\.)'
        group2 = r'(?<=\(\"|\(\')[a-z0-9\-]+'
        if _dict:
            try:
                dct = json.loads(_dict.group().replace("'", '"'))
                args = re.findall(group1 + '|' + group2, line)
                for k, v in dct.items():
                    self.do_update('{} {} {} "{}"'.
                                   format(args[0], args[2], k, v))
                    return ''
            except Exception:
                return line
        # scan for general formating - i.e '.', '(', ')'
        if not ("." in line and "(" in line and ")" in line):
            return line

        try:  # parse line left to right
            pline = line[:]  # parsed line

            # isolate <class name>
            _cls = pline[: pline.find(".")]

            # isolate and validate <command>
            _cmd = pline[pline.find(".") + 1: pline.find("(")]
            if _cmd not in HBNBCommand.dot_cmds and _cmd != "create":
                raise Exception

            # if parantheses contain arguments, parse them
            pline = pline[pline.find("(") + 1: pline.find(")")]
            if pline:
                # partition args: (<id>, [<delim>], [<*args>])
                pline = pline.partition(", ")  # pline convert to tuple

                # isolate _id, stripping quotes
                _id = pline[0].replace('\"', "")
                # possible bug here:
                # empty quotes register as empty _id when replaced

                # if arguments exist beyond _id
                pline = pline[2].strip()  # pline is now str
                if pline:
                    # check for *args or **kwargs
                    if (
                        pline[0] == "{" and pline[-1] == "}" and type(
                            eval(pline)
                            ) is dict
                    ):
                        _args = pline
                    else:
                        _args = pline.replace(",", "")
                        # _args = _args.replace('\"', '')
            line = " ".join([_cmd, _cls, _id, _args])

        except Exception as mess:
            pass
        finally:
            return line

    def do_quit(self, command):
        """Method to exit the HBNB console"""
        return True

    def help_quit(self):
        """Prints the help documentation for quit"""
        print("Exits the program with formatting\n")

    def do_EOF(self, arg):
        """Handles EOF to exit program"""
        print()
        return True

    def help_EOF(self):
        """Prints the help documentation for EOF"""
        print("Exits the program without formatting\n")

    def emptyline(self):
        """Overrides the emptyline method of CMD"""
        pass

    def do_create(self, args):
        """Creates an instance of a given class with provided parameters """
        storage_type = os.getenv("HBNB_TYPE_STORAGE")
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        # Define necessary attributes for each class
        necessary_attributes = {
            "User": ["email", "password"],
            "Place": ["city_id", "user_id", "name"],
            "State": ["name"],
            "City": ["state_id", "name"],
            "Amenity": ["name"],
            "Review": ["place_id", "user_id", "text"],
            }

        # Check if necessary attributes are provided
        if storage_type == "db" and args[0] in necessary_attributes:
            attributes_provided = [arg.split("=")[0] for arg in args[1:]]
            for necessary_attribute in necessary_attributes[args[0]]:
                if necessary_attribute not in attributes_provided:
                    print(f"** {necessary_attribute} missing **")
                    return

        new_instance = HBNBCommand.classes[args[0]]()
        if len(args) > 1:
            for arg in args[1:]:
                try:
                    key, value = arg.split("=")
                    # Check if the attribute is valid for the class
                    if hasattr(new_instance, key):
                        # Convert to the right format (int,float,string,list)
                        if value[0] == "\"":
                            value = value[1:-1].replace("_", " ")
                        elif "." in value:
                            value = float(value)
                        elif value[0] == "[" and value[-1] == "]":
                            value = [
                                    item.strip('\"')
                                    for item in value[1:-1].split(",")
                                    ]
                        else:
                            value = int(value)
                        setattr(new_instance, key, value)
                except ValueError:
                    print(f"** value {value} for {key} is invalid **")
                    continue
        storage.new(new_instance)
        storage.save()
        print(new_instance.id)

    def help_create(self):
        """Help information for the create method"""
        print("Creates a class of any type")
        print("[Usage]: create <className>\n")

    def do_show(self, args):
        """Method to show an individual object"""
        new = args.partition(" ")
        c_name = new[0]
        c_id = new[2]

        # guard against trailing args
        if c_id:
            if " " in c_id:
                c_id = c_id.partition(" ")[0]
            if c_id[0] == "'":
                second_quote = c_id.find("'", 1)
                c_id = c_id[1:second_quote]

        if not c_name:
            print("** class name missing **")
            return

        if c_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if not c_id:
            print("** instance id missing **")
            return

        key = c_name + "." + c_id
        try:
            if os.getenv('HBNB_TYPE_STORAGE') == 'db':
                for obj in storage._DBStorage__session.query(
                        HBNBCommand.classes[c_name]
                        ).all():
                    if obj.id == c_id:
                        print(obj)
                        break
                else:
                    raise KeyError
            else:
                print(storage._FileStorage__objects[key])
        except KeyError:
            print("** no instance found **")

    def help_show(self):
        """Help information for the show command"""
        print("Shows an individual instance of a class")
        print("[Usage]: show <className> <objectId>\n")

    def do_destroy(self, args):
        """Destroys a specified object"""
        new = args.partition(" ")
        c_name = new[0]
        c_id = new[2]
        if c_id:
            if " " in c_id:
                c_id = c_id.partition(" ")[0]
            if c_id[0] == "'":
                second_quote = c_id.find("'", 1)
                c_id = c_id[1:second_quote]

        if not c_name:
            print("** class name missing **")
            return

        if c_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if not c_id:
            print("** instance id missing **")
            return

        key = c_name + "." + c_id

        try:
            del storage.all()[key]
            storage.save()
        except KeyError:
            print("** no instance found **")

    def help_destroy(self):
        """Help information for the destroy command"""
        print("Destroys an individual instance of a class")
        print("[Usage]: destroy <className> <objectId>\n")

    def do_all(self, args):
        """Shows all objects, or all objects of a class"""
        print_list = []

        if args:
            args = args.split(" ")[0]  # remove possible trailing args
            if args not in HBNBCommand.classes:
                print("** class doesn't exist **")
                return
            objects = storage.all(HBNBCommand.classes[args])
        else:
            objects = storage.all()

        for obj in objects.values():
            print_list.append(str(obj))

        print(print_list)

    def help_all(self):
        """Help information for the all command"""
        print("Shows all objects, or all of a class")
        print("[Usage]: all <className>\n")

    def do_count(self, args):
        """Count current number of class instances"""
        count = 0
        if os.getenv('HBNB_TYPE_STORAGE') == 'db':
            objects = storage.all()
            for k, v in objects.items():
                if args == k.split(".")[0]:
                    count += 1
            print(count)
        else:
            for k, v in storage._FileStorage__objects.items():
                if args == k.split(".")[0]:
                    count += 1
            print(count)

    def help_count(self):
        """Help information for the help command """
        print("Usage: count <class_name>")

    def do_update(self, args):
        """Updates a certain object with new info"""
        c_name = c_id = att_name = att_val = kwargs = ""

        # isolate cls from id/args, ex: (<cls>, delim, <id/args>)
        args = args.partition(" ")
        if args[0]:
            c_name = args[0]
        else:  # class name not present
            print("** class name missing **")
            return
        if c_name not in HBNBCommand.classes:  # class name invalid
            print("** class doesn't exist **")
            return

        # isolate id from args
        args = args[2].partition(" ")
        if args[0]:
            c_id = args[0]
            if c_id[0] == "'":
                second_quote = c_id.find("'", 1)
                c_id = c_id[1:second_quote]
        else:  # id not present
            print("** instance id missing **")
            return

        # generate key from class and id
        key = c_name + "." + c_id

        # determine if key is present
        if key not in storage.all():
            print("** no instance found **")
            return

        args = args[2]
        if args and ((args[0] == '"') or (args[0] == "'")):  # check quoted arg
            second_quote = args.replace("'", '"').find('"', 1)
            att_name = args[1:second_quote]
            args = args[second_quote + 1:]

        args = args.partition(" ")  # error, what if ("name", "john smith")

        # if att_name was not quoted arg
        if not att_name and (args[0] != " "):
            att_name = args[0]
        # check for quoted val arg
        if args[2] and ((args[2][0] == '"') or (args[2][0] == "'")):
            att_val = args[2][1: args[2].replace("'", '"').find('"', 1)]

        # if att_val was not quoted arg
        if not att_val and args[2]:
            att_val = args[2].partition(" ")[0]

        args = [att_name, att_val]

        # retrieve dictionary of current objects
        new_dict = storage.all()[key]

        # iterate through attr names and values
        for i, att_name in enumerate(args):
            # block only runs on even iterations
            if i % 2 == 0:
                att_val = args[i + 1]  # following item is value
                if not att_name:  # check for att_name
                    print("** attribute name missing **")
                    return
                if not att_val:  # check for att_value
                    print("** value missing **")
                    return
                # type cast as necessary
                if att_name in HBNBCommand.types:
                    att_val = HBNBCommand.types[att_name](att_val)

                # update dictionary with name, value pair
                new_dict.__dict__.update({att_name: att_val})

        new_dict.save()  # save updates to file

    def help_update(self):
        """Help information for the update class"""
        print("Updates an object with new information")
        print("Usage: update <className> <id> <attName> <attVal>\n")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
