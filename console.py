#!/usr/bin/python3
"""
Creating a console for the AirBnB_clone
"""

import cmd
import sys
import shlex    # Unix shell - like syntax analyzer
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
    # Some attributes that are not allowed to be modified manually
    not_updatable = ["id", "created_at", "updated_at"]

    def preloop(self):
        """
        Print if isatty is false
        """
        if not sys.__stdin__.isatty():
            print('(hbnb)')

    def precmd(self, line):
        """
        Reformat command line for advanced command syntax.

        Usage: <Class name>.<command>([<id> [<*args> or <**kwargs>]])
        (Brackets denote optional fields in usage example.)
        """
        _cmd = _cls = _id = _args = str()    # initialize line elements

        # scan for general formating - i.e '.', '(', ')'
        if not ('.' in line and '(' in line and ')' in line):
            return line

        try:  # parse line left to right
            pline = line[:]  # parsed line

            # isolate <Class name>
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
                    if (pline[0] == '{') and (pline[-1] == '}')\
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
        """
        Print if isatty is false
        """
        if not sys.__stdin__.isatty():
            print('(hbnb) ', end='')
        return stop

    def do_quit(self, command):
        """
        Quit command to exit the program
        Usage:
        ======
        quit

        Example:
        =======
            (hbnb) quit
        """
        return True

    def do_EOF(self, arg):
        """
        End of file marker for exit
        Usage:
        ======
        <CTRL + D>

        Example:
        ========
            (hbnb) <CTRL + D>
        """
        print()
        return True

    def emptyline(self):
        """
        Executed when an empty line is entered in response to the prompt
        """
        pass

    def do_create(self, args):
        """
        Create a new instance.

        Param syntax: <key name>="<value>"

        * Any double qoute inside the value must be escaped with a backslash
        * All underscores in the value are replaced by spaces.

        Usage:
        ======
        * create <Class name>
        * create <Class name> <param 1> <param 2> <param 3>...

        Example:
        ========
            (hbnb) create BaseModel
            1234-1234-1234
            (hbnb) create State name="Little_California" zip_location="103422"
            1235-1235-1235
            (hbnb) show State 1235-1235-1235
            [State] (1235-1235-1235) {'id': '1235-1235-1235', \
'created_at': datetime.datetime(2023, 6, 12, 18, 59, 0, 404960), \
'updated_at': datetime.datetime(2023, 6, 12, 18, 59, 0, 404960), \
'name': 'Little California', 'zip_location': 103422}
        """
        # Fetch all arguments
        try:
            args = shlex.split(args, posix=True, comments=False)
        except Exception as e:
            print("**Error: {}**".format(e))
            return

        """
        # Test to see actual arguments
        for pos in range(len(args)):
            print("\targ[{}]: '{}'".format(pos, args[pos]))
        """

        if not args:
            print("** class name missing **")
            return

        _class = args[0]
        if _class not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        # Create a dictonary of attributes of the instance
        attr = dict()
        for arg in args[1:]:
            # print("**arg: {}**".format(arg))
            if "=" not in arg:
                # If parameter is unrecognized, skip it
                continue

            key = arg.split("=")[0]
            value = arg.split("=")[-1]

            # Replace underscores in the value with by space
            value = value.replace(str('_'), str(' '))

            # convert the value to the required type
            try:
                value = float(value)
            except ValueError:
                pass
            else:
                if value == int(value):
                    value = int(value)

            # print("dict: '{}'".format({key: value}))    # test
            attr.update({key: value})

        # print("\nAttributes: '{}'\n".format(attr))      # test

        new_instance = HBNBCommand.classes[_class]()

        # Update the instance with the attributes
        for key, value in attr.items():
            setattr(new_instance, key, value)

        # Save the instance to storage
        storage.save()
        print(new_instance.id)
        storage.save()

    def do_show(self, args):
        """
        Print the string representation of an instance based on
        the class name and id.
        Usage:
        ======
        show <Class name> <id>

        Alternative use:
        ================
        <Class name>.show(<id>)

        Example:
        ========
            (hbnb) show BaseModel 1234-1234-1234
            ...
            (hbnb) BaseModel.show(1234-1234-1234)
            ...
        """
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
            print(storage.all()[key])
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, args):
        """
        Delete an instance based on the class name and id.
        Usage:
        ======
        destroy <Class name> <id>

        Alternative use:
        ================
        <Class name>.destroy(<id>)

        Example:
        ========
            (hbnb) destroy BaseModel 1234-1234-1234
            (hbnb) BaseModel.destroy(1234-1234-1234)
        """
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

        """
        try:
            del (storage.all()[key])
            storage.save()
        except KeyError:
            print("** no instance found **")
        """
        try:
            storage.delete(key)
            storage.save()
        except KeyError:
            print("** no instance found **")

    def do_all(self, args):
        """
        Print all string representation of all instances based on
        the class name or not.
        Usage:
        ======
        all [<Class name>]

        Alternative use:
        ================
        * <Class name>.all()
        * .all()

        Example:
        ========
            (hbnb) all
            ...
            (hbnb) .all()
            ...
            (hbnb) all BaseModel
            ...
            (hbnb) BaseModel.all()
            ...
        """
        print_list = []

        if args:
            args = args.split(' ')[0]  # remove possible trailing args
            if args not in HBNBCommand.classes:
                print("** class doesn't exist **")
                return
            for k, v in storage.all().items():
                if k.split('.')[0] == args:
                    print_list.append(str(v))
        else:
            for k, v in storage.all().items():
                print_list.append(str(v))

        print(print_list)

    def do_count(self, args):
        """
        Count the current number of instances based on / not on class name
        Usage:
        ======
        count [<Class name>]

        Alternative use:
        ================
        * <Class name>.count()
        * .count()

        Example:
        ========
            (hbnb) count
            5
            (hbnb) .count()
            5
            (hbnb) count User
            2
            (hbnb) User.count()
            2
            (hbnb) Amenity.count()
            3
        """

        if type(args) is str and len(args) == 0:   # args is an empty string
            pass
        elif args not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        count = 0
        for k, v in storage.all().items():
            # count all instances
            if type(args) is str and len(args) == 0:   # args is an empty str
                count += 1
            # count only instances of the specified class
            elif (args in HBNBCommand.classes) and (args == k.split('.')[0]):
                count += 1

        print(count)

    def do_update(self, args):
        """
        Update an instance based on class name and id.
        NOTE:
        *   only one attribute is updated at a time
        *   The attributes ``id``, ``created_at`` and ``updated_at`` are not
            allowed to be updated
        Usage:
        ======
        update <Class name> <id> <attribute name> "<attribute value>"

        Alternative use:
        ================
        * <Class name>.update(<id>, <attribute name>, <attribute value>)

        * <Class name>.update(<id>, <dictionary representation>)

        Example:
        ========
            (hbnb) update BaseModel 1234-1234-1234 email "airbnb@gmail.com"
            (hbnb) BaseModel.update(1234-1234-1234, email, "airbnb@gmail.com")
            (hbnb) BaseModel.update(1234-1234-1234, \
{"email": "airbnb@gmail.com"})
        """
        c_name = c_id = att_name = att_val = kwargs = str('')

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
            if (args) and (args[0] == '\"'):  # check for quoted arg
                second_quote = args.find('\"', 1)
                att_name = args[1:second_quote]
                args = args[second_quote + 1:]

            args = args.partition(' ')

            # if att_name was not quoted arg
            if (not att_name) and (args[0] != ' '):
                att_name = args[0]

            # check for quoted val arg
            if args[2] and (args[2][0] == '\"'):
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

                # Restrict updating of specific attributes
                if att_name in HBNBCommand.not_updatable:
                    info = "** The \"{}\" attribute is not allowed \
to be updated **"
                    print(info.format(att_name))
                    return

                # type cast as necessary
                if att_name in HBNBCommand.types:
                    att_val = HBNBCommand.types[att_name](att_val)

                # update dictionary with name, value pair
                new_dict.__dict__.update({att_name: att_val})

        new_dict.save()  # save updates to file

    # Auto-completion

    def complete_create(self, text, line, begidx, endix):
        """
        Auto completion
        """
        return [i for i in self.classes if i.startswith(text)]

    def complete_show(self, text, line, begidx, endix):
        """
        Auto completion
        """
        return [i for i in self.classes if i.startswith(text)]

    def complete_all(self, text, line, begidx, endix):
        """
        Auto completion
        """
        return [i for i in self.classes if i.startswith(text)]

    def complete_destroy(self, text, line, begidx, endix):
        """
        Auto completion
        """
        return [i for i in self.classes if i.startswith(text)]

    def complete_update(self, text, line, begidx, endix):
        """
        Auto completion
        """
        return [i for i in self.classes if i.startswith(text)]

    def complete_count(self, text, line, begidx, endix):
        """
        Auto completion
        """
        return [i for i in self.classes if i.startswith(text)]


# Don't execute console if imported
if __name__ == "__main__":
    # Ensure that codebase works properly by running tests
    # put the code here
    HBNBCommand().cmdloop()
