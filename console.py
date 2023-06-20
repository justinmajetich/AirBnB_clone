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
            print('(hbnb)', end=' ')

    def precmd(self, line):
        """Reformat command line for advanced command syntax.

        Usage: <class name>.<command>([<id> [<*args> or <**kwargs>]])
        (Brackets denote optional fields in usage example.)
        """
        _cmd = _cls = _id = _args = ''  # initialize line elements

        # scan for general formating - i.e '.', '(', ')', '='
        if not ('.' in line and '(' in line and ')' in line and '=' in line):
            return line

        try:  # parse line left to right
            pline = line[:]  # parsed line

            # [State.create()]
            # [State.all()].find('.') -> 5
            # _cls = pline[:5] -> State

            # check if plin contains '='
            if '=' in pline:
                first_space = pline.find(' ')
                second_space = pline.find(' ', first_space + 1)

                _cmd = pline[:first_space]
                _cls = pline[first_space + 1:second_space]
                _args = pline[second_space + 1:]

                line = ' '.join([_cmd, _cls, _args])
            # check if pline contains '.'
            elif '.' in pline:
                # isolate <class name>
                _cls = pline[:pline.find('.')]

                # isolate and validate <command>
                _cmd = pline[pline.find('.') + 1:pline.find('(')]
                if _cmd not in HBNBCommand.dot_cmds:
                    raise Exception

                # if parantheses contain arguments, parse them
                pline = pline[pline.find('(') + 1:pline.find(')')]
                if pline:
                    # partition args: (<id>, [<delim>], [<*args>])
                    pline = pline.partition(', ')  # pline convert to tuple

                    # isolate _id, stripping quotes
                    _id = pline[0].replace('\"', '')
                    # possible bug here:
                    # empty quotes register as empty _id when replaced

                    # if arguments exist beyond _id
                    pline = pline[2].strip()  # pline is now str
                    if pline:
                        # check for *args or **kwargs
                        if pline[0] == '{' and pline[-1] == '}' \
                                and type(eval(pline)) is dict:
                            _args = pline
                        else:
                            _args = pline.replace(',', '')
                            # _args = _args.replace('\"', '')
                line = ' '.join([_cmd, _cls, _id, _args])

        except Exception as mess:
            pass
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

    def parse_args(self, args):
        """Parse args into kwargs.
        args is a string of the form: <key>=<value> <key>=<value>
        <value> may contain spaces.
        """

        # create empty kwargs
        kwargs = {}

        # track whether we are in a quote or have found an equal sign
        equal = False
        quote = False

        # track key and value
        key = value = ''

        # iterate through args
        for char in args:
            # if not in quote and not equal sign, add to key and continue
            if not equal and not quote and char not in ' =':
                key += char
                continue

            # if equal sign, set equal to True and continue
            if char == '=':
                equal = True
                continue

            # if not in quote and character is a quote, set quote to True
            if char == '\"' and not quote:
                quote = True
                continue

            # if in quote and character is not a quote,
            # add to value and continue
            if quote and char != '\"':
                value += char
                continue

            # if in quote and character is a quote,
            # set quote to False and add to kwargs
            # reset key and value and continue
            # effectively skipping the space after the closing quote
            if char == '\"' and quote:
                quote = False
                equal = False
                kwargs[key] = value
                key = value = ''
                continue

        return kwargs

    def do_create(self, args):
        """ Create an object of any class"""
        if not args:
            print("** class name missing **")
            return

        # get class name from args
        _cls = args.partition(" ")[0]

        # check if class exists
        if _cls not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        # build kwargs from args
        # _args look like 'name="New York" state_id="0001"'
        # create **kwargs from _args
        _args = args.partition(" ")[2]
        _kwargs = self.parse_args(_args)

        # create new instance of class
        new_instance = HBNBCommand.classes[_cls](**_kwargs)
        print(new_instance.id)
        storage.new(new_instance)
        storage.save()

    def help_create(self):
        """ Help information for the create method """
        print("Creates a class of any type")
        print("[Usage]: create <className>\n")

    def do_show(self, args):
        """ Method to show an individual object """
        new = args.partition(" ")
        c_name = new[0]
        c_id = new[2]

        # guard against trailing args
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
            print(storage._FileStorage__objects[key])
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
        print("Destroys an individual instance of a class")
        print("[Usage]: destroy <className> <objectId>\n")
    '''
    def do_all(self, args):
        """ Shows all objects, or all objects of a class"""
        print_list = []

        if args:
            args = args.split(' ')[0]  # remove possible trailing args
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
    '''

    def do_all(self, args):
        """Shows all objects, or all objects of a class"""
        print_list = []

        if args:
            class_name = args.split(' ')[0]  # extract the class name
            if class_name not in HBNBCommand.classes:
                print("** class doesn't exist **")
                return
            for obj in storage.all().values():
                if type(obj).__name__ == class_name:
                    print_list.append(str(obj))
        else:
            print_list = [str(obj) for obj in storage.all().values()]

        print(print_list)


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
        """ Updates a certain object with new info """
        c_name = c_id = att_name = att_val = kwargs = ''

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
        else:  # id not present
            print("** instance id missing **")
            return

        # generate key from class and id
        key = c_name + "." + c_id

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
