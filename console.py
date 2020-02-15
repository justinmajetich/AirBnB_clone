#!/usr/bin/python3
""" Console Module """
import cmd
from models.base_model import BaseModel
from models.__init__ import storage


class HBNBCommand(cmd.Cmd):
    """ Contains the functionality for the HBNB console"""
    prompt = '(hbnb)'
    intro = ""
    classes = {'BaseModel': BaseModel, 'User': User}

    def do_quit(self, command):
        """ Method to exit the HBNB console"""
        exit()

    def help_quit(self):
        """ Prints the help documentation for quit  """
        print("Exits the program with formatting")

    def do_EOF(self, arg):
        """ Handles EOF to exit program """
        print()
        exit()

    def help_EOF(self):
        """ Prints the help documentation for EOF """
        print("Exits the program without formatting")

    def emptyline(self):
        """ Overrides the emptyline method of CMD """
        pass

    def do_create(self, args):
        """ """
        if not args:
            print("** class name missing **")
            return
        elif args not in classes:
            print("** class doesn't exist")
            return
        new_instance = classes[args]()
        print(new_instance.id)

    def do_show(self, args):
        """ """
        new = args.partition(" ")
        c_name = new[0]
        c_id = new[2]
        if not c_name:
            print("** class name missing **")
            return

        if c_name not in classes:
            print("** class doesn't exist **")
            return

        if not c_id:
            print("** instance id missing **")
            return

        key = c_name + "." + c_id
        try:
            print(storage._FileStorage__objects[key])
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, args):
        """ """
        new = args.partition(" ")
        c_name = new[0]
        c_id = new[2]
        if not c_name:
            print("** class name missing **")
            return

        if c_name not in classes:
            print("** class doesn't exist **")
            return

        if not c_id:
            print("** instance id missing **")
            return

        key = c_name + "." + c_id
        try:
            del(storage._FileStorage__objects[key])
            storage.save()
        except KeyError:
            print("** no instance found **")

    def do_all(self, args):
        """ """
        print_list = []

        if args:
            if args not in classes:
                print("** class doesn't exist **")
                return
            for k, v in storage._FileStorage__objects.items():
                if k == args.split('.')[0]:
                    print_list.append(str(v))
        else:
            for k, v in storage._FileStorage__objects.items():
                print_list.append(str(v))

        print(print_list)

    def do_update(self, args):
        """ """
        new = args.split(" ")
        try:
            c_name = new[0]
            c_id = new[1]
            key = c_name + "." + c_id
            att_name = new[2]
            att_val = new[3]
        except:
            pass

        if not c_name:
            print("** class name missing **")
            return

        if c_name not in classes:
            print("** class doesn't exist **")
            return

        if not c_id:
            print("** instance id missing **")
            return
        if key not in storage._FileStorage__objects:
            print("** no instance found **")
            return

        if not att_name:
            print("** attribute name missing **")
            return

        if not att_val:
            print("** value missing **")
            return

        try:
            new_dict = storage._FileStorage__objects[key]
            new_dict.__dict__.update({att_name: att_val})
            storage.save()
        except KeyError:
            print("** no instance found **")

if __name__ == "__main__":
    HBNBCommand().cmdloop()
