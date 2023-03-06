#!/usr/bin/python3


from console_behaviour import *

from introspection.m_classes import MetaClassTools
from introspection.m_functions import MetaFunctionTools

def search_dict_values(
    dictionary,
    criteria1=(lambda x: x == x),
    criteria2=(lambda x: x == x)
):
        return [
                z for z in [
                        x for x in dictionary.values()
                ] 
                if criteria1(z) and criteria2(z)
        ]

def get_modules(mamespace, criteria=(lambda x: x == x)):
    return [
            z for z in
            search_dict_values(
                mamespace,
                (lambda x: MetaClassTools.type_name_string(x) == "module"),
                (lambda x: "builtins" not in str(x))
        ) if criteria(z)
    ]

def find_functions_in_mod(mod_dict):
      return [x for x in mod_dict.values() if callable(x)]

def build_command_list(namespace):

    command_functions = sum([find_functions_in_mod(vars(x)) for x in get_modules(namespace)], [])
    global_name_table = [
          x for x in globals().keys()
            if "__" not in x
    ]
    command_list = {}
    for func in command_functions:
          command_list.update()

print(build_command_list(vars()))