#!/usr/bin/python3
"""Console Module"""

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
    """Contains the functionality for the HBNB console"""

    # Determines prompt for interactive/non-interactive modes
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
        """Reformat command line for advanced command syntax."""
        # Remaining code for the precmd method...

    def postcmd(self, stop, line):
        """Prints if isatty is false"""
        if not sys.__stdin__.isatty():
            print('(hbnb) ', end='')
        return stop

    def do_quit(self, command):
        """Method to exit the HBNB console"""
        # Remaining code for the do_quit method...

    def help_quit(self):
        """Prints the help documentation for quit"""
        # Remaining code for the help_quit method...

    def do_EOF(self, arg):
        """Handles EOF to exit program"""
        # Remaining code for the do_EOF method...

    def help_EOF(self):
        """Prints the help documentation for EOF"""
        # Remaining code for the help_EOF method...

    def emptyline(self):
        """Overrides the emptyline method of CMD"""
        pass

    def do_create(self, args):
        """Create an object of any class"""
        # Remaining code for the do_create method...

    def help_create(self):
        """Help information for the create method"""
        # Remaining code for the help_create method...

    def do_show(self, args):
        """Method to show an individual object"""
        # Remaining code for the do_show method...

    def help_show(self):
        """Help information for the show command"""
        # Remaining code for the help_show method...

    def do_destroy(self, args):
        """Destroys a specified object"""
        # Remaining code for the do_destroy method...

    def help_destroy(self):
        """Help information for the destroy command"""
        # Remaining code for the help_destroy method...

    def do_all(self, args):
        """Shows all objects, or all objects of a class"""
        # Remaining code for the do_all method...

    def help_all(self):
        """Help information for the all command"""
        # Remaining code for the help_all method...

    def do_count(self, args):
        """Count current number of class instances"""
        # Remaining code for the do_count method...

    def help_count(self):
        """Help information for the count command"""
        # Remaining code for the help_count method...

    def do_update(self, args):
        """Updates a certain object with new info"""
        # Remaining code for the do_update method...

    def help_update(self):
        """Help information for the update command"""
        # Remaining code for the help_update method...


if __name__ == "__main__":
    HBNBCommand().cmdloop()
