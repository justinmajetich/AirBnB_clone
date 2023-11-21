#!/usr/bin/python3
""" Console Module """
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
from datetime import datetime


class HBNBCommand(cmd.Cmd):
    """ Contains the functionality for the HBNB console"""
    use_rawinput = sys.stdin.isatty()
    prompt = '(hbnb) ' if sys.stdin.isatty() else ''
    classes = {
               'BaseModel': BaseModel, 'User': User, 'Place': Place,
               'State': State, 'City': City, 'Amenity': Amenity,
               'Review': Review
              }
    dot_cmds = ['all', 'count', 'show', 'destroy', 'update']

    def preloop(self):
        """Handle database initialization"""
        pass

    def do_quit(self, _):
        """ Method to exit the HBNB console"""
        sys.exit()

    def help_quit(self):
        """ Prints the help documentation for quit  """
        print("Quit command to exit the program\n\nUsage: quit")

    def do_EOF(self, _):
        """EOF command to exit the program"""
        print()
        return True

    def emptyline(self):
        """Do nothing when emptyline is entered"""
        return False

    def precmd(self, line):
        """Called on an input line when the command prefix is not recognized"""
        _cmd = _cls = _id = _args = ''  # initialize line elements

        # scan for general formating - i.e '.', '(', ')'
        if not ('.' in line and '(' in line and ')' in line):
            return line

        pline = line[:]  # parsed line

        # isolate <class name>
        _cls = pline[:pline.find('.')]

        # isolate and validate <command>
        _cmd = pline[pline.find('.') + 1:pline.find('(')]

        # parse arguments in parenthesis
        pline = pline[pline.find('(') + 1:pline.find(')')]
        if pline:
            # tokenize args by delimiter (<id>, <args>)
            pline = pline.split(', ', 1)

            # strip quotes if exist
            _id = pline[0].replace("\"", "")

            # if arguments exist beyond _id
            if len(pline) > 1:
                if "{" in pline[1] and "}" in pline[1] and ":" in pline[1]:
                    idxs = [i for i, ltr in enumerate(pline[1]) if ltr == "\""]
                    if len(idxs) % 2 == 0:
                        return " ".join([_cmd, _cls, _id, pline[1]])
                    new_idxs = [[idxs[i], idxs[i+1]]
                                for i in range(0, len(idxs), 2)]
                    tokens = []
                    for s, e in new_idxs:
                        tokens.append(pline[1][s:e+1])
                    pline[1:] = tokens

                tokens = []
                for token in pline[1:]:
                    tokens.append(token.replace("\"", ""))
                _args = " ".join(tokens)
        line = ' '.join([_cmd, _cls, _id, _args])
        return line

    def do_create(self, args):
        """ Create an object of any class"""
        if not args:
            print("** class name missing **")
            return
        params = args.split(' ').copy()
        className = params[0]
        if className not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        del params[0]
        if (len(params) > 0):
            params_dict = {
                param[0]: param[1].replace('"', '').replace("'", '')
                for param in (v.split('=') for v in params)
            }
            params_dict['__class__'] = className
            if params_dict.get('created_at') is None:
                params_dict['created_at'] = datetime.now().isoformat()
            if params_dict.get('updated_at') is None:
                params_dict['updated_at'] = datetime.now().isoformat()
            new_instance = HBNBCommand.classes[className](**params_dict)
            storage.new(new_instance)
        else:
            new_instance = HBNBCommand.classes[className]()
        storage.save()
        print(new_instance.id)
        storage.save()

    def help_create(self):
        """ Help information for the create method """
        print("Creates a class of any type")
        print("[Usage]: create <className>\n")

    def do_show(self, line):
        """ Method to show an individual object """
        if not line:
            print("** class name missing **")
            return

        args = line.split()
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if len(args) == 1:
            print("** instance id missing **")
            return

        c_name = args[0]
        c_id = args[1]
        key = c_name + "." + c_id
        try:
            print(storage.all()[key])
        except KeyError:
            print("** no instance found **")

    def help_show(self):
        """ Help information for the show command """
        print("Shows an individual instance of a class")
        print("[Usage]: show <className> <objectId>\n")

    def do_destroy(self, args):
        """ Destroys a specified object """
        new = args.partition(" ")
        c_name = new[0]
        c_id = new[2]
        if c_id and ' ' in c_id:
            c_id = c_id.partition(' ')[0]

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
            del (storage.all()[key])
            storage.save()
        except KeyError:
            print("** no instance found **")

    def help_destroy(self):
        """ Help information for the destroy command """
        print("Destroys an individual instance of a class.\n" +
              "[Usage]: destroy <className> <objectId>")

    def do_all(self, args):
        """ Shows all objects, or all objects of a class"""
        print_list = []

        if args:
            args = args.split()[0]  # remove possible trailing args
            if args not in HBNBCommand.classes:
                print("** class doesn't exist **")
                return
            for k, v in storage._FileStorage__objects.items():
                if k.split('.')[0] == args:
                    print_list.append(str(v))
        else:
            for k, v in storage._FileStorage__objects.items():
                print_list.append(str(v))

        print(print_list)

    def help_all(self):
        """ Help information for the all command """
        print("Shows all objects, or all of a class")
        print("[Usage]: all <className>\n")

    def do_count(self, args):
        """Count current number of class instances"""
        if not args:
            print("** class name is missing **")
        elif args.split()[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            count = 0
            for k in storage.all():
                if args == k.split('.')[0]:
                    count += 1
            print(count)

    def help_count(self):
        """ """
        print("Usage: count <class_name>")

    def do_update(self, args):
        """ Updates a certain object with new info """
        c_name = c_id = attr = val = ''

        # isolate cls from id/args, ex: (<cls>, delim, <id/args>)
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        c_name = args[0]
        if c_name not in HBNBCommand.classes:  # class name invalid
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        c_id = args[1]

        # generate key from class and id
        key = c_name + "." + c_id

        # determine if key is present
        if key not in storage.all():
            print("** no instance found **")
            return

        # retrieve remaining arguments
        new_dict = storage.all()[key]
        args = args[2:]
        args = [[args[i], args[i+1]] for i in range(0, len(args), 2)]

        # iterate through attr names and values
        for attr, val in args:
            if not attr:  # check for attribute
                print("** attribute name missing **")
                return
            if not val:  # check for value
                print("** value missing **")
                return

            # update dictionary with name, value pair
            setattr(new_dict, attr, val)

        new_dict.save()  # save updates to file

    def help_update(self):
        """ Help information for the update class """
        print("Updates an object with new information")
        print("Usage: update <className> <id> <attName> <attVal>\n")


if __name__ == "__main__":
    HBNBCommand().cmdloop(intro="Welcome to HBNBCommand program. " +
                          "Type 'help' for a list of commands")
