#!/usr/bin/env python3
""" Console Module """
import cmd
import os
import re
import sys
import shlex

from models.base_model import BaseModel
import models
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBService:

    storage = None

    def __init__(self) -> None:
        self.storage = models.storage

    def create(self, entity, **kwargs):
        return self.storage.new(entity, **kwargs)

    def find(self, *args, **kwargs):
        pass

    def find_all(self, arg):
        return self.storage.all(arg)

    def find_by_id(self, *args, **kwargs):
        pass

    def delete(self, *args, **kwargs):
        pass

    def _update(self, *args, **kwargs):
        pass


class HBNBCommand(cmd.Cmd):
    """A command-line parser for interactive use.

    This class provides a command-line interface for interactive use.
    Users can enter commands, and this parser interprets and processes
    those commands.

    Attributes:
        prompt (str): The command prompt to display.
    """
    prompt = '(hbnb) '
    bnbService = HBNBService()

    def __init__(self, completekey="tab", stdin=None, stdout=None):
        """Initialize the HBNBCommand.

        Args:
            completekey (str, optional): The key to trigger tab completion.
            Defaults to "tab".
            stdin (file, optional): The input stream to use. Defaults to None.
            stdout (file, optional): The output stream to use.
            Defaults to None.
        """
        super().__init__(completekey, stdin, stdout)

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Ctrl-D to exit the program"""
        return True

    def do_create(self, *args):
        """Create a new model"""
        _args = (str(args[0]).split(' '))
        kw = self.parse_attr(_args[1:])

        if len(_args) < 1 or args[0] == '':
            print('** class name missing **')
            return
        _id = self.bnbService.create(_args[0], **kw)
        if _id is not None:
            print(_id)
            return

    def do_update(self, *args):
        """Update model data"""
        _args = (str(args[0]).split(' '))
        _model, _attr, _id, _value = list([str()] * 4)
        try:
            _model = _args[0]
            _id = _args[1]
            _attr = _args[2]
            _value = _args[3]
        except (ValueError, IndexError):
            if _model is None or len(_model) == 0:
                print('** class name missing **')
                return
            if _id is None or len(_id) == 0:
                print('** instance id missing **')
                return
            if _attr is None or len(_attr) == 0:
                print('** attribute name missing **')
                return
            if _value is None or len(_value) == 0:
                print('** value missing **')
                return

        result = self.bnbService.update_model_attribute(_model, _id,
                                                        _attr, _value)

        if result is not None:
            print(result)
            return
        else:
            return

    def do_destroy(self, *args):
        """Remove a model by id"""
        _args = (str(args[0]).split(' '))
        _model = ''
        _id = ''
        try:
            _model = _args[0]
            _id = _args[1]
        except (ValueError, IndexError):
            if len(_model) == 0:
                print('** class name missing **')
                return
            if _id is None or len(_id) == 0:
                print('** instance id missing **')
                return

        return self.bnbService.delete_model_by_id(_model, _id)

    def do_all(self, *args):
        """Lists all models of a class"""
        _args = args[0].split(' ')
        result = self.bnbService.find_all(_args[0])
        if result is not None and len(result) > 0:
            [print(x) for x in result]

    def do_count(self, *args):
        """Prints the size of a model type"""
        _args = args[0].split(' ')
        if len(_args) < 1:
            print('** class name missing **')

        _count = self.bnbService.fetch_model_count(_args[0])
        if _count is not None:
            print(_count)

    def do_show(self, *args):
        """Prints a model instance"""
        _args = (str(args[0]).split(' '))
        _model = ''
        _id = ''
        try:
            _model = _args[0]
            _id = _args[1]
        except (ValueError, IndexError):
            if len(_model) == 0:
                print('** class name missing **')
                return
            if _id is None or len(_id) == 0:
                print('** instance id missing **')
                return

        result = self.bnbService.fetch_model_by_id(_model, _id)
        if result is not None:
            print(result)

    def parse_attr(self, args):
        """Parses class attributes and returns a dictionary representation"""
        arg_dict = {}
        for x in range(0, len(args)):
            tmp = args[x].split("=")
            arg_dict[tmp[0]] = tmp[1]
        new_dict = {}
        for key, value in arg_dict.items():
            if isinstance(value, str):
                new_dict[key] = value.replace("_", " ").replace('"', '')
            else:
                new_dict[key] = value
        return new_dict

    def cmdloop(self, intro=None):
        super().cmdloop(intro)

    def emptyline(self) -> bool:
        return False

    def preloop(self) -> None:
        if not os.isatty(0):
            self.prompt = ''
            self.onecmd('')

    def precmd(self, line: str):
        try:
            _fn = 'do_' + line.split(' ')[0]
            if getattr(self, _fn) is not None:
                return super().precmd(line)
        except (AttributeError):
            try:
                ln = self.preprocess_input(line)
                return super().precmd(ln)
            except (AttributeError, TypeError, ValueError, IndexError):
                return super().precmd(line)

        return super().precmd(line)

    def preprocess_input(self, line: str):
        args = [self.remove_quotes(x)
                for x in self.tokenize_string(line)]
        _entity = args[0]
        _method = args[1]
        _args = args[2:]
        if getattr(self, 'do_' + _method) is not None:
            return ' '.join([_method, _entity] + _args)

    def remove_quotes(self, input: str):
        if input.startswith(('"', "'")) and input.endswith(('"', "'")):
            return input[1:-1]
        else:
            return input

    def tokenize_string(self, input_string):
        if input_string is None or len(input_string) == 0:
            return ['']
        pattern = r'([A-Za-z_][A-Za-z0-9_]*(\.[A-Za-z_][A-Za-z0-9_]*)*)\.([A \
        -Za-z_][A-Za-z0-9_]*)\(([^)]*)\)'

        match = re.match(pattern, input_string)
        if match:
            class_name = match.group(1)
            method_name = match.group(3)
            args = [arg.strip() for arg in match.group(4).split(',')]
            return [class_name, method_name] + args

        return None


if __name__ == "__main__":
    HBNBCommand().cmdloop()


# class HBNBCommand(cmd.Cmd):
#     """ Contains the functionality for the HBNB console"""

#     # determines prompt for interactive/non-interactive modes
#     prompt = '(hbnb) ' if sys.__stdin__.isatty() else ''

#     classes = {
#         'BaseModel': BaseModel, 'User': User, 'Place': Place,
#         'State': State, 'City': City, 'Amenity': Amenity,
#         'Review': Review
#     }
#     dot_cmds = ['all', 'count', 'show', 'destroy', 'update']
#     types = {
#         'number_rooms': int, 'number_bathrooms': int,
#         'max_guest': int, 'price_by_night': int,
#         'latitude': float, 'longitude': float
#     }

#     def preloop(self):
#         """Prints if isatty is false"""
#         if not sys.__stdin__.isatty():
#             print('(hbnb)')

#     def precmd(self, line):
#         """Reformat command line for advanced command syntax.

#         Usage: <class name>.<command>([<id> [<*args> or <**kwargs>]])
#         (Brackets denote optional fields in usage example.)
#         """
#         _cmd = _cls = _id = _args = ''  # initialize line elements

#         # scan for general formating - i.e '.', '(', ')'
#         if not ('.' in line and '(' in line and ')' in line):
#             return line

#         try:  # parse line left to right
#             pline = line[:]  # parsed line

#             # isolate <class name>
#             _cls = pline[:pline.find('.')]

#             # isolate and validate <command>
#             _cmd = pline[pline.find('.') + 1:pline.find('(')]
#             if _cmd not in HBNBCommand.dot_cmds:
#                 raise Exception

#             # if parantheses contain arguments, parse them
#             pline = pline[pline.find('(') + 1:pline.find(')')]
#             if pline:
#                 # partition args: (<id>, [<delim>], [<*args>])
#                 pline = pline.partition(', ')  # pline convert to tuple

#                 # isolate _id, stripping quotes
#                 _id = pline[0].replace('\"', '')
#                 # possible bug here:
#                 # empty quotes register as empty _id when replaced

#                 # if arguments exist beyond _id
#                 pline = pline[2].strip()  # pline is now str
#                 if pline:
#                     # check for *args or **kwargs
#                     if pline[0] == '{' and pline[-1] == '}'\
#                             and type(eval(pline)) is dict:
#                         _args = pline
#                     else:
#                         _args = pline.replace(',', '')
#                         # _args = _args.replace('\"', '')
#             line = ' '.join([_cmd, _cls, _id, _args])

#         except Exception as mess:
#             pass
#         finally:
#             return line

#     def postcmd(self, stop, line):
#         """Prints if isatty is false"""
#         if not sys.__stdin__.isatty():
#             print('(hbnb) ', end='')
#         return stop

#     def do_quit(self, command):
#         """ Method to exit the HBNB console"""
#         exit()

#     def help_quit(self):
#         """ Prints the help documentation for quit  """
#         print("Exits the program with formatting\n")

#     def do_EOF(self, arg):
#         """ Handles EOF to exit program """
#         print()
#         exit()

#     def help_EOF(self):
#         """ Prints the help documentation for EOF """
#         print("Exits the program without formatting\n")

#     def emptyline(self):
#         """ Overrides the emptyline method of CMD """
#         pass

#     def parse_attr(self, args):
#         """Parses class attributes and returns a dictionary representation"""
#         arg_dict = {}
#         for x in range(1, len(args)):
#             tmp = args[x].split("=")
#             arg_dict[tmp[0]] = tmp[1]
#         return arg_dict

#     def do_create(self, args):
#         """ Create an object of any class"""
#         all_args = shlex.split(args)
#         cls_name = all_args[0]

#         if not cls_name:
#             print("** class name missing **")
#             return
#         elif cls_name not in HBNBCommand.classes:
#             print("** class doesn't exist **")
#             return

#         arg_dict = self.parse_attr(all_args)

#         new_instance = HBNBCommand.classes[cls_name]()
#         for y in arg_dict:
#             setattr(new_instance, y, arg_dict[y])
#         models.storage.save()
#         print(new_instance.id)
#         models.storage.save()

#     def help_create(self):
#         """ Help information for the create method """
#         print("Creates a class of any type")
#         print("[Usage]: create <className>\n")

#     def do_show(self, args):
#         """ Method to show an individual object """
#         new = args.partition(" ")
#         c_name = new[0]
#         c_id = new[2]

#         # guard against trailing args
#         if c_id and ' ' in c_id:
#             c_id = c_id.partition(' ')[0]

#         if not c_name:
#             print("** class name missing **")
#             return

#         if c_name not in HBNBCommand.classes:
#             print("** class doesn't exist **")
#             return

#         if not c_id:
#             print("** instance id missing **")
#             return

#         key = c_name + "." + c_id
#         try:
#             print(storage._FileStorage__objects[key])
#         except KeyError:
#             print("** no instance found **")

#     def help_show(self):
#         """ Help information for the show command """
#         print("Shows an individual instance of a class")
#         print("[Usage]: show <className> <objectId>\n")

#     def do_destroy(self, args):
#         """ Destroys a specified object """
#         new = args.partition(" ")
#         c_name = new[0]
#         c_id = new[2]
#         if c_id and ' ' in c_id:
#             c_id = c_id.partition(' ')[0]

#         if not c_name:
#             print("** class name missing **")
#             return

#         if c_name not in HBNBCommand.classes:
#             print("** class doesn't exist **")
#             return

#         if not c_id:
#             print("** instance id missing **")
#             return

#         key = c_name + "." + c_id

#         try:
#             del (storage.all()[key])
#             storage.save()
#         except KeyError:
#             print("** no instance found **")

#     def help_destroy(self):
#         """ Help information for the destroy command """
#         print("Destroys an individual instance of a class")
#         print("[Usage]: destroy <className> <objectId>\n")

#     def do_all(self, args):
#         """ Shows all objects, or all objects of a class"""
#         print_list = []

#         if args:
#             args = args.split(' ')[0]  # remove possible trailing args
#             if args not in HBNBCommand.classes:
#                 print("** class doesn't exist **")
#                 return
#             for k, v in storage._FileStorage__objects.items():
#                 if k.split('.')[0] == args:
#                     print_list.append(str(v))
#         else:
#             for k, v in storage._FileStorage__objects.items():
#                 print_list.append(str(v))

#         print(print_list)

#     def help_all(self):
#         """ Help information for the all command """
#         print("Shows all objects, or all of a class")
#         print("[Usage]: all <className>\n")

#     def do_count(self, args):
#         """Count current number of class instances"""
#         count = 0
#         for k, v in storage._FileStorage__objects.items():
#             if args == k.split('.')[0]:
#                 count += 1
#         print(count)

#     def help_count(self):
#         """ """
#         print("Usage: count <class_name>")

#     def do_update(self, args):
#         """ Updates a certain object with new info """
#         c_name = c_id = att_name = att_val = kwargs = ''

#         # isolate cls from id/args, ex: (<cls>, delim, <id/args>)
#         args = args.partition(" ")
#         if args[0]:
#             c_name = args[0]
#         else:  # class name not present
#             print("** class name missing **")
#             return
#         if c_name not in HBNBCommand.classes:  # class name invalid
#             print("** class doesn't exist **")
#             return

#         # isolate id from args
#         args = args[2].partition(" ")
#         if args[0]:
#             c_id = args[0]
#         else:  # id not present
#             print("** instance id missing **")
#             return

#         # generate key from class and id
#         key = c_name + "." + c_id

#         # determine if key is present
#         if key not in storage.all():
#             print("** no instance found **")
#             return

#         # first determine if kwargs or args
#         if '{' in args[2] and '}' in args[2] and type(eval(args[2])) is dict:
#             kwargs = eval(args[2])
#             args = []  # reformat kwargs into list, ex: [<name>, <value>, ...]
#             for k, v in kwargs.items():
#                 args.append(k)
#                 args.append(v)
#         else:  # isolate args
#             args = args[2]
#             if args and args[0] == '\"':  # check for quoted arg
#                 second_quote = args.find('\"', 1)
#                 att_name = args[1:second_quote]
#                 args = args[second_quote + 1:]

#             args = args.partition(' ')

#             # if att_name was not quoted arg
#             if not att_name and args[0] != ' ':
#                 att_name = args[0]
#             # check for quoted val arg
#             if args[2] and args[2][0] != '\"':
#                 att_val = args[2][1:args[2].find('\"', 1)]

#             # if att_val was not quoted arg
#             if not att_val and args[2]:
#                 att_val = args[2].partition(' ')[0]

#             args = [att_name, att_val]

#         # retrieve dictionary of current objects
#         new_dict = storage.all()[key]

#         # iterate through attr names and values
#         for i, att_name in enumerate(args):
#             # block only runs on even iterations
#             if (i % 2 == 0):
#                 att_val = args[i + 1]  # following item is value
#                 if not att_name:  # check for att_name
#                     print("** attribute name missing **")
#                     return
#                 if not att_val:  # check for att_value
#                     print("** value missing **")
#                     return
#                 # type cast as necessary
#                 if att_name in HBNBCommand.types:
#                     att_val = HBNBCommand.types[att_name](att_val)

#                 # update dictionary with name, value pair
#                 new_dict.__dict__.update({att_name: att_val})

#         new_dict.save()  # save updates to file

#     def help_update(self):
#         """ Help information for the update class """
#         print("Updates an object with new information")
#         print("Usage: update <className> <id> <attName> <attVal>\n")
