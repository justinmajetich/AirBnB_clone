#!/usr/bin/python3

import inspect

from introspection.m_functions import MetaFunctionTools


class MetaClassTools:
    """ COLLECTION OF TOOLS TO DYNAMICALLY MANIPULATE CLASSES VIA INTROSPECTION """

    @classmethod
    def dynamically_define_class(name, parent, **components):
        pass

    @staticmethod
    def type_name_string(any_object):
        """RETURNS A STRING CONTAINING THE NAME OF OBJECT DATATYPE"""
        return (type(any_object).__qualname__)

        
    @classmethod
    def find_instance_properties(cls, code_obj):
        """RETURNS LIST INSTANCE PROPERTIES BY EXAMINING CLASS INITALIZER CODE"""
        base_names = [item for item in object.__dict__.keys()]

        classes = {
                name: class_obj for name, class_obj in globals().items() if type(class_obj).__qualname__ == "type"
        }
        class_member_names = [
            name for name in sum([
                    list(vars(members).keys()) for members in classes.values()
                ], []
            ) if name not in base_names
        ]
        bad_names = [
            *class_member_names,
            *base_names,
            *[x for x in list(globals().keys())],
            *[x for x in list(classes.keys())]
        ]
        return [
            z for z in MetaFunctionTools.find_varaiable_names(code_obj) if z not in bad_names
        ]


class Spam:

    def __init__(self, *args):
        self.name = ""
        self.number = 0

        MetaClassTools.unpack_arguments(self.__class__, args)

    @classmethod
    def bar(cls):
        pass
