#!/usr/bin/python3

"""
Console Module
"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """ Contains the functionality for the HBNB console"""

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

