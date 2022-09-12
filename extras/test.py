#!/usr/bin/python3
from os import getenv
from print import printme
import sys
sys.path.insert(1, '/home/dennis/alx/AirBnB_clone_v2')
from console import HBNBCommand  # noqa

# HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
# HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
# HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
# HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
# HBNB_ENV = getenv('HBNB_ENV')
# HBNB_TYPE_STORAGE = getenv('HBNB_TYPE_STORAGE')


# env = [HBNB_MYSQL_USER, HBNB_MYSQL_PWD, HBNB_MYSQL_HOST, HBNB_MYSQL_HOST,
#        HBNB_MYSQL_DB, HBNB_ENV, HBNB_TYPE_STORAGE]

printme("enviroment variables", HBNBCommand.classes)
