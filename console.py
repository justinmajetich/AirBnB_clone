#!/usr/bin/python3
"""Define the HBNBCommand class."""
import cmd
from models.base_model import BaseModel
from models import storage
from shlex import split
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


def parse(text_args):
    """Parse all argurments for the console"""
    # print("============")
    text_args = text_args.replace('"', '\\"')
    # print(text_args)
    return split(text_args)


def cast(text_value):
    """Cast in int or float a value"""
    if text_value[0] == '"' and text_value[-1] == '"':
        return text_value[1:-1]
    elif text_value.isnumeric():
        return int(text_value)
    else:
        try:
            return float(text_value)
        except:
            return None


def get_arg(met):
    """ Get argument inside of ' ( arg) ' """

    idx = met.find('(')
    return met[idx + 1: -1]


class HBNBCommand(cmd.Cmd):
    """Defines the HolbertonBnB command interpreter.
    Attributes:
    ===========
        prompt (str): The command prompt.
    """

    prompt = "(hbnb) "
    __classes = {
        "BaseModel": BaseModel,
        "User": User,
        "Place": Place,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Review": Review
    }

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """Exit with 'EOF' signal.
        """
        print("")
        return True

    def emptyline(self):
        """Ignore an empty line.
        """
        pass

    # Commands

    def do_create(self, arg):
        """Usage --> create <class>
        Create a new instance of the indicated class and:
            - Saves it (to the JSON file)
            - Prints the id
        Errors:
        =======
        ```
        (hbnb) create
        ** class name missing **
        ```
        ```
        (hbnb) create MyModel
        ** class doesn't exist **
        ```
        """

        l_args = parse(arg)
        d_cls = HBNBCommand.__classes

        if len(l_args) == 0:
            print("** class name missing **")
        elif l_args[0] not in d_cls.keys():
            print("** class doesn't exist **")
        else:
            key_cls = l_args[0]
            obj = d_cls[key_cls]()
            # Set parameters
            if len(l_args) > 1:
                params = [tp.split("=") for tp in l_args[1:] if " " not in tp]
                for p in params:
                    if len(p) == 2:
                        key, tex_value = p
                        value = cast(tex_value.replace("_", " "))
                        if value is not None:
                            setattr(obj, key, value)
            print(obj.id)
            storage.new(obj)
            storage.save()

    def do_show(self, arg):
        """Usage --> show <class> <id>
        Prints the string representation of an instance
        based on the class name and id
        Errors:
        =======
        ```
        (hbnb) show
        ** class name missing **
        ```
        ```
        (hbnb) show MyModel 1234-1234
        ** class doesn't exist **
        ```
        ```
        (hbnb) show BaseModel
        ** instance id missing **
        ```
        ```
        (hbnb) show BaseModel 12341234
        ** no instance found **
        ```
        """

        l_args = parse(arg)
        d_cls = HBNBCommand.__classes

        if len(l_args) == 0:
            print("** class name missing **")
        elif l_args[0] not in d_cls.keys():
            print("** class doesn't exist **")
        elif len(l_args) == 1:
            print("** instance id missing **")
        else:
            key_obj = l_args[0] + "." + l_args[1]
            if key_obj not in storage.all().keys():
                print("** no instance found **")
            else:
                print(storage.all()[key_obj])

    def do_destroy(self, arg):
        """Usage --> destroy <class> <id>
        Deletes an instance based on the class name and id,
        also update the JSON file.
        Errors:
        =======
        ```
        (hbnb) destroy
        ** class name missing **
        ```
        ```
        (hbnb) destroy MyModel 1234-1234
        ** class doesn't exist **
        ```
        ```
        (hbnb) destroy BaseModel
        ** instance id missing **
        ```
        ```
        (hbnb) destroy BaseModel 12341234
        ** no instance found **
        ```
        """

        l_args = parse(arg)
        d_cls = HBNBCommand.__classes

        if len(l_args) == 0:
            print("** class name missing **")
        elif l_args[0] not in d_cls.keys():
            print("** class doesn't exist **")
        elif len(l_args) == 1:
            print("** instance id missing **")
        else:
            key_obj = l_args[0] + "." + l_args[1]
            if key_obj not in storage.all().keys():
                print("** no instance found **")
            else:
                del storage.all()[key_obj]
                storage.save()

    def do_all(self, arg):
        """Usage --> all <class>
        Prints all string representation of all instances
        based or not on the class name.
        Note: <class> is optional.
        Errors:
        =======
        ```
        (hbnb) all MyModel
        ** class doesn't exist **
        ```
        """

        l_args = parse(arg)
        d_cls = HBNBCommand.__classes
        val_obj = storage.all().values()

        if len(l_args) == 0:
            print([str(obj) for obj in val_obj])
        elif l_args[0] not in d_cls.keys():
            print("** class doesn't exist **")
        else:
            def flt(x):
                return x.__class__.__name__ == l_args[0]
            text = "["
            for obj in val_obj:
                if flt(obj):
                    text += str(obj) + ", "
            if text[0:-2] == ", ":
                text = text[0:-2] + "]"
            else:
                text += "]"
            print(text)

    def do_update(self, arg):
        """Usage --> update <class name> <id> <attribute name> "<attribute value>"
        Updates an instance based on the class name and id by adding
        or updating attribute also update the JSON file.
        Errors:
        =======
        ```
        (hbnb) update
        ** class name missing **
        ```
        ```
        (hbnb) update MyModel 1234-1234
        ** class doesn't exist **
        ```
        ```
        (hbnb) update BaseModel
        ** instance id missing **
        ```
        ```
        (hbnb) update BaseModel 12341234
        ** no instance found **
        ```
        ```
        (hbnb) update BaseModel existing-id
        ** attribute name missing **
        ```
        ```
        (hbnb) update BaseModel existing-id first_name
        ** value missing **
        ```
        """

        l_args = parse(arg)
        d_cls = HBNBCommand.__classes

        if len(l_args) == 0:
            print("** class name missing **")
        elif l_args[0] not in d_cls.keys():
            print("** class doesn't exist **")
        elif len(l_args) == 1:
            print("** instance id missing **")
        else:
            key_obj = l_args[0] + "." + l_args[1]
            if key_obj not in storage.all().keys():
                print("** no instance found **")
            elif len(l_args) == 2:
                print("** attribute name missing **")
            elif len(l_args) == 3:
                print("** value missing **")
            else:
                obj = storage.all()[key_obj]
                attr = l_args[2]
                value = cast(l_args[3])
                setattr(obj, attr, value)
                storage.save()

    def do_count(self, arg):
        """Usage -> <class name>.count()
        Retrieve the number of instances of a class.
        Errors:
        =======
        ```
        (hbnb) pizza.all()
        ** class doesn't exist **
        ```
        """

        l_args = parse(arg)
        d_cls = HBNBCommand.__classes
        val_obj = storage.all().values()
        if l_args[0] not in d_cls.keys():
            print("** class doesn't exist **")
        else:
            def flt(x):
                return x.__class__.__name__ == l_args[0]
            print(len([obj for obj in val_obj if flt]))

    def launch_update(self, class_name, text_args):
        """Parsing the arguments and lauch the update command"""

        if text_args == "":
            args = "{}".format(class_name)
            return HBNBCommand.do_update(self, args)
        else:
            l_args = text_args.split(", ", 1)
            len_args = len(l_args)

        if len_args == 1:
            args = "{} {}".format(class_name, l_args[0])
            return HBNBCommand.do_update(self, args)
        else:
            obj_id = l_args[0]
            # Dictionary input
            if l_args[1][0] == "{" and l_args[1][-1] == "}":
                l_items = l_args[1][1:-1].split(", ")
                # Validate items and launch update command
                if all(": " in item for item in l_items):
                    for item in l_items:
                        attr, value = item.split(": ")
                        t_args = (class_name, obj_id, attr, value)
                        args = "{} {} {} {}".format(*t_args)
                        HBNBCommand.do_update(self, args)
                    return

            # Simple input
            if ", " not in l_args[1]:
                args = "{} {} {}".format(class_name, obj_id, l_args[1])
                HBNBCommand.do_update(self, args)
                return

            l_args_attr_val = l_args[1].split(", ")
            t_args = (
                class_name,
                obj_id, l_args_attr_val[0],
                l_args_attr_val[1])
            args = "{} {} {} {}".format(*t_args)
            HBNBCommand.do_update(self, args)

    def default(self, arg):
        """ Usage -> <class name>.action()
        Command interpreter retrieve all instances of class by using:
        '<class name>.all()'
        Errors:
        =======
        ```
        (hbnb) pizza.all()
        ** class doesn't exist **
        ```
        """

        if '.' in arg:
            l_args = arg.split('.', 1)
            d_cls = HBNBCommand.__classes
            if l_args[1] == "all()":
                HBNBCommand.do_all(self, l_args[0])
            elif l_args[1] == "count()":
                HBNBCommand.do_count(self, l_args[0])
            elif l_args[1][:4] == "show":
                args = get_arg(l_args[1])
                HBNBCommand.do_show(self, l_args[0] + " " + args)
            elif l_args[1][:7] == "destroy":
                args = get_arg(l_args[1])
                HBNBCommand.do_destroy(self, l_args[0] + " " + args)
            elif l_args[1][:6] == "update":
                text_args = get_arg(l_args[1])
                HBNBCommand.launch_update(self, l_args[0], text_args)
            else:
                print("*** Unknown syntax: {}.{}".format(
                    l_args[0],
                    l_args[1]
                    ))
        else:
            cmd.Cmd.default(self, arg)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
