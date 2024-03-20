#!/usr/bin/python3
""" Console Module BACKUP VERSION """
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


class HBNBCommand(cmd.Cmd):
    """ Contains the functionality for the HBNB console"""

    # determines prompt for interactive/non-interactive modes
    prompt = '(hbnb) ' if sys.__stdin__.isatty() else ''

    classes = {
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

    def preloop(self):
        """Prints if isatty is false"""
        if not sys.__stdin__.isatty():
            print('(hbnb)')

    def precmd(self, line):
        """Reformat command line for advanced command syntax.

        Usage: <class name>.<command>([<id> [<*args> or <**kwargs>]])
        EXAMPLE: BaseModel.update("123-456x" {name: Jhon, age; 25})
        (Brackets denote optional fields in usage example.)
        """
        cmd = class_name = id = _args = ''  # initialize line elements

        # scan for general formating - i.e '.', '(', ')'
        if not ('.' in line and '(' in line and ')' in line):
            return line

        try:  # parse line left to right
            pline = line[:]  # parsed line

            # isolate <class name>
            class_name = pline[:pline.find('.')]

            # isolate and validate <command>
            cmd = pline[pline.find('.') + 1:pline.find('(')]
            if cmd not in HBNBCommand.dot_cmds:
                raise Exception

            # if parantheses contain arguments, parse them
            pline = pline[pline.find('(') + 1:pline.find(')')]
            if pline:
                # partition args: (<id>, [<delim>], [<*args>])
                pline = pline.partition(', ')  # pline convert to tuple

                # isolate id, stripping quotes
                id = pline[0].replace('\"', '')
                # possible bug here:
                # empty quotes register as empty id when replaced

                # if arguments exist beyond id
                pline = pline[2].strip()  # pline is now str
                if pline:
                    # check for *args or **kwargs
                    if pline[0] == '{' and pline[-1] == '}'\
                            and type(eval(pline)) is dict:
                        _args = pline
                    else:
                        _args = pline.replace(',', '')
                        # _args = _args.replace('\"', '')
            line = ' '.join([cmd, class_name, id, _args])

        except Exception as mess:
            print(mess)
        finally:
            return line

    def postcmd(self, stop, line):
        """Prints if isatty is false"""
        if not sys.__stdin__.isatty():
            print('(hbnb) ', end='')
        return stop

    def do_quit(self, command):
        """ Method to exit the HBNB console"""
        exit()

    def help_quit(self):
        """ Prints the help documentation for quit  """
        print("Exits the program with formatting\n")

    def do_EOF(self, arg):
        """ Handles EOF to exit program """
        print()
        exit()

    def help_EOF(self):
        """ Prints the help documentation for EOF """
        print("Exits the program without formatting\n")

    def emptyline(self):
        """ Overrides the emptyline method of CMD """
        pass

    def do_create(self, args):
        """Create an object of any class"""
        if not args:
            print("** class name missing **")
            return
        else:
            all_args = args.split()
            class_nm = all_args[0]
        if class_nm not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(all_args) > 0:
            params_dict = {}
            params = all_args[1:]
            for param in params:
                param = param.partition("=")
                key = param[0]
                value = param[2]
                if ('"') in value:
                    value = value.replace('_', ' ')
                    value = value.replace('"', '')
                elif ('.') in value:
                    value = float(value)
                else:
                    value = int(value)
                params_dict[key] = value
        new_instance = HBNBCommand.classes[class_nm](**params_dict)
        print(new_instance.id)
        storage.new(new_instance)
        storage.save()  # Commit changes to the database


    def help_create(self):
        """ Help information for the create method """
        print("Creates a class of any type")
        print("[Usage]: create <className>\n")

    def do_show(self, args):
        """ Method to show an individual object """
        arguments = args.partition(" ")
        class_name = arguments[0]
        id = arguments[2]

        # guard against trailing args with '.partition()'
        # Example: "123AX more_args" = ('123X', ' ', 'more_args')
        if id and ' ' in id:
            id = id.partition(' ')[0]  # Store 1st element from example'123X'

        if not class_name:
            print("** class name missing **")
            return

        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if not id:
            print("** instance id missing **")
            return

        key = class_name + "." + id
        try:
            print(storage._FileStorage__objects[key])
        except KeyError:
            print("** no instance found **")

    def help_show(self):
        """ Help information for the show command """
        print("Shows an individual instance of a class")
        print("[Usage]: show <className> <objectId>\n")

    def do_destroy(self, args):
        """ Destroys a specified object """
        arguments = args.partition(" ")
        class_name = arguments[0]
        id = arguments[2]
        if id and ' ' in id:
            id = id.partition(' ')[0]

        if not class_name:
            print("** class name missing **")
            return

        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if not id:
            print("** instance id missing **")
            return

        key = class_name + "." + id

        try:
            del (storage.all()[key])
            storage.save()
        except KeyError:
            print("** no instance found **")

    def help_destroy(self):
        """ Help information for the destroy command """
        print("Destroys an individual instance of a class")
        print("[Usage]: destroy <className> <objectId>\n")

    def do_all(self, args):
        """ Shows all objects, or all objects of a class"""
        list_to_print = []

        if args:
            args = args.split(' ')[0]  # remove possible trailing args
            if args not in HBNBCommand.classes:
                print("** class doesn't exist **")
                return

            # Retrieve objects from the database using DBStorage
            objects = storage.all(HBNBCommand.classes[args])
            for obj in objects.values():
                list_to_print.append(str(obj))
        else:
            # Retrieve all objects from the database using DBStorage
            objects = storage.all()
            for obj in objects.values():
                list_to_print.append(str(obj))

        print(list_to_print)

    def help_all(self):
        """ Help information for the all command """
        print("Shows all objects, or all of a class")
        print("[Usage]: all <className>\n")

    def do_count(self, args):
        """Count current number of class instances"""
        count = 0
        for k, v in storage._FileStorage__objects.items():
            if args == k.split('.')[0]:
                count += 1
        print(count)

    def help_count(self):
        """ """
        print("Usage: count <class_name>")

    def do_update(self, args):
        """
            Updates a certain object with new info
             Example: update <classname> <id> <attribute_name> <value>
        """
        class_name = id = att_name = att_val = kwargs = ''

        # isolate cls from id/args, ex: (<cls>, delim, <id/args>)
        args = args.partition(" ")
        if args[0]:
            class_name = args[0]
        else:  # class name not present
            print("** class name missing **")
            return
        if class_name not in HBNBCommand.classes:  # class name invalid
            print("** class doesn't exist **")
            return

        # isolate id from args
        args = args[2].partition(" ")
        if args[0]:
            id = args[0]
        else:  # id not present
            print("** instance id missing **")
            return

        # generate key from class and id
        key = class_name + "." + id

        # determine if key is present
        if key not in storage.all():
            print("** no instance found **")
            return

        # first determine if kwargs or args
        if '{' in args[2] and '}' in args[2] and type(eval(args[2])) is dict:
            kwargs = eval(args[2])
            args = []  # reformat kwargs into list, ex: [<name>, <value>, ...]
            for k, v in kwargs.items():
                args.append(k)
                args.append(v)
        else:  # isolate args
            args = args[2]
            if args and args[0] == '\"':  # check for quoted arg
                second_quote = args.find('\"', 1)
                att_name = args[1:second_quote]
                args = args[second_quote + 1:]

            args = args.partition(' ')

            # if att_name was not quoted arg
            if not att_name and args[0] != ' ':
                att_name = args[0]
            # check for quoted val arg
            if args[2] and args[2][0] == '\"':
                att_val = args[2][1:args[2].find('\"', 1)]

            # if att_val was not quoted arg
            if not att_val and args[2]:
                att_val = args[2].partition(' ')[0]

            args = [att_name, att_val]

        # retrieve dictionary of current objects
        new_dict = storage.all()[key]

        # iterate through attr names and values
        for i, att_name in enumerate(args):
            # block only runs on even iterations
            if (i % 2 == 0):
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
        """ Help information for the update class """
        print("Updates an object with new information")
        print("Usage: update <className> <id> <attName> <attVal>\n")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
