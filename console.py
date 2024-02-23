#!/usr/bin/python3
""" Console Module """
import cmd
import sys
import shlex
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
        (Brackets denote optional fields in usage example.)
        """
        _cmd = _cls = _id = _args = ''  # initialize line elements

        # scan for general formating - i.e '.', '(', ')'
        if not ('.' in line and '(' in line and ')' in line):
            return line

        try:  # parse line left to right
            pline = line[:]  # parsed line

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
                    if pline[0] is '{' and pline[-1] is'}'\
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

    def do_create(self, args):
        """ Create an object of any class"""
        args = shlex.split(args)
        if not args:
            print("** class name missing **")
            return
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        
        param_dict = {}
        for arg in args[1:]:
            if '=' not in arg:
                print("** invalid parameter format, use key=value **")
                return
            key, value = arg.split('=')
            key = key.replace('_', ' ')
            if value.startswith('"') and value.endswith('"'):
                value = value[1:-1]
                value = value.replace('\\"', '"')
            try:
                if '.' in value:
                    value = float(value)
                else:
                    value = int(value)
            except ValueError:
                pass
            param_dict[key] = value

        new_instance = HBNBCommand.classes[args[0]](**param_dict)
        storage.save()
        print(new_instance.id)  # Print the new ID

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

        all_objs = storage.all()
        for k, v in all_objs.items():
            if c_id == v.id and v.__class__.__name__ == c_name:
                print(v)
                return
        print("** no instance found **")

    def help_show(self):
        """ Prints the help documentation for the show method """
        print("Prints the string representation of an instance based on the class name and id\n")

    def do_destroy(self, args):
        """ Method to delete an object """
        new = args.partition(" ")
        c_name = new[0]
        c_id = new[2]

        if not c_name:
            print("** class name missing **")
            return

        if c_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if not c_id:
            print("** instance id missing **")
            return

        all_objs = storage.all()
        for k, v in all_objs.items():
            if c_id == v.id and v.__class__.__name__ == c_name:
                del all_objs[k]
                storage.save()
                return
        print("** no instance found **")

    def help_destroy(self):
        """ Prints the help documentation for the destroy method """
        print("Deletes an instance based on the class name and id\n")

    def do_all(self, args):
        """ Method to display all objects """
        all_objs = storage.all()
        obj_list = []

        if not args:
            for k, v in all_objs.items():
                obj_list.append(v.__str__())
            print(obj_list)
            return

        if args not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        for k, v in all_objs.items():
            if args == v.__class__.__name__:
                obj_list.append(v.__str__())
        print(obj_list)

    def help_all(self):
        """ Prints the help documentation for the all method """
        print("Prints all string representation of all instances based or not on the class name\n")

    def do_update(self, args):
        """ Method to update an instance by adding or updating attribute """
        new = args.partition(" ")
        c_name = new[0]
        new = new[2].partition(" ")
        c_id = new[0]
        new = new[2].partition(" ")
        c_att = new[0]
        c_val = new[2]

        if not c_name:
            print("** class name missing **")
            return

        if c_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if not c_id:
            print("** instance id missing **")
            return

        if not c_att:
            print("** attribute name missing **")
            return

        if not c_val:
            print("** value missing **")
            return

        if '.' in c_val:
            c_val = float(c_val)
        else:
            try:
                c_val = int(c_val)
            except ValueError:
                pass

        all_objs = storage.all()
        for k, v in all_objs.items():
            if c_id == v.id and v.__class__.__name__ == c_name:
                setattr(v, c_att, c_val)
                storage.save()
                return
        print("** no instance found **")

    def help_update(self):
        """ Prints the help documentation for the update method """
        print("Updates an instance based on the class name and id by adding or updating attribute\n")

    def default(self, line):
        """ Method to handle method calls without explicitly defined command """
        args = line.split(".")
        if len(args) < 2:
            print("*** Unknown syntax:", line)
            return

        if args[1] == "all()":
            self.do_all(args[0])
        elif args[1] == "count()":
            print(sum(1 for obj in storage.all().values()
                      if obj.__class__.__name__ == args[0]))
        elif args[1].startswith("show"):
            arg = args[1].split("(")[1].split(")")[0]
            self.do_show(args[0] + " " + arg)
        elif args[1].startswith("destroy"):
            arg = args[1].split("(")[1].split(")")[0]
            self.do_destroy(args[0] + " " + arg)
        elif args[1].startswith("update"):
            args_list = args[1].split("(")[1].split(")")[0].split(", ")
            if len(args_list) < 3:
                print("*** Unknown syntax:", line)
                return
            args_list[1] = args_list[1].replace('"', '')
            args_list[2] = args_list[2].replace('"', '')
            args_list[2] = args_list[2].replace(',', '')
            args_list[2] = args_list[2].replace('"', '')
            self.do_update(args[0] + " " + " ".join(args_list))
        else:
            print("*** Unknown syntax:", line)

    def emptyline(self):
        """ Method to handle an empty line entered """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
