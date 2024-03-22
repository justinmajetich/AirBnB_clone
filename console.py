#!/usr/bin/python3
"""
Console Module
"""
import cmd
import sys
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """ Contains the functionality for the HBNB console"""
    """
    Contains the functionality for the HBNB console
    """

    prompt = '(hbnb) '

    prompt = '(hbnb) '
    classes = {
        'BaseModel': BaseModel,
    }

    def __init__(self):
        super().__init__()

    def do_quit(self, arg):
        """Exit the console"""
        return True

    def help_quit(self):
        """Help documentation for quit"""
        print("Exit the console.")

    def do_EOF(self, arg):
        """Exit the console at EOF"""
        print()
        return True

    def help_EOF(self):
        """Help documentation for EOF"""
        print("Exit the console at end of file.")

    def emptyline(self):
        """Override the emptyline method of CMD"""
        pass

    def do_create(self, args):
        """Create a new instance of a class"""
        if not args:
            print("** class name missing **")
            return
        class_name = args.split()[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        new_instance = self.classes[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, args):
        """Show an instance based on the class name and id"""
        if not args:
            print("** class name missing **")
            return
        arg_list = args.split()
        class_name = arg_list[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        if len(arg_list) < 2:
            print("** instance id missing **")
            return
        objs = storage.all(class_name)
        obj_id = arg_list[1]
        key = "{}.{}".format(class_name, obj_id)
        if key not in objs:
            print("** no instance found **")
            return
        print(objs[key])

    def do_destroy(self, args):
        """Delete an instance based on the class name and id"""
        if not args:
            print("** class name missing **")
            return
        arg_list = args.split()
        class_name = arg_list[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        if len(arg_list) < 2:
            print("** instance id missing **")
            return
        objs = storage.all(class_name)
        obj_id = arg_list[1]
        key = "{}.{}".format(class_name, obj_id)
        if key not in objs:
            print("** no instance found **")
            return
        del objs[key]
        storage.save()

    def do_all(self, args):
        """Show all instances or all instances of a class"""
        arg_list = args.split()
        if arg_list and arg_list[0] not in self.classes:
            print("** class doesn't exist **")
            return
        objs = storage.all(arg_list[0]) if arg_list else storage.all()
        print([str(obj) for obj in objs.values()])

    def do_count(self, args):
        """Count instances of a class"""
        if not args:
            print("** class name missing **")
            return
        if args not in self.classes:
            print("** class doesn't exist **")
            return
        objs = storage.all(args)
        print(len(objs))
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

    def do_update(self, args):
        """Update an instance based on the class name and id"""
        if not args:
            print("** class name missing **")
            return
        arg_list = args.split()
        class_name = arg_list[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        if len(arg_list) < 2:
            print("** instance id missing **")
            return
        objs = storage.all(class_name)
        obj_id = arg_list[1]
        key = "{}.{}".format(class_name, obj_id)
        if key not in objs:
            print("** no instance found **")
            return
        if len(arg_list) < 3:
            print("** attribute name missing **")
            return
        if len(arg_list) < 4:
            print("** value missing **")
            return
        setattr(objs[key], arg_list[2], arg_list[3])
        storage.save()

if __name__ == "__main__":
    HBNBCommand().cmdloop()

