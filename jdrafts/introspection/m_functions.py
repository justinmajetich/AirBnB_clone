#!/usr/bin/python3

import inspect

class MetaFunctionTools:
    """ COLLECTION OF TOOLS TO DYNAMICALLY MANIPULATE FUNCTIONS VIA INTROSPECTION """

    @staticmethod
    def find_code_attribute(code_obj, target_attribute="co_name"):
        """RETURNS THE SPECIFIED ATTRIBUTE OF FUNCTUON"""
        input_class = code_obj.__class__.__name__

        if input_class != "code":
            try:
                code_obj = {
                        "frame": (lambda x: x.f_code),
                        "function": (lambda x: x.__code__),
                    }[input_class](code_obj)
            except:
                raise AttributeError("Place holder")
        
        return (code_obj.__getattribute__(target_attribute))


    @classmethod
    def find_function_name(cls, code_obj):
        """RETURNS DEFAULT ATTRIBUTE FROM 'find_code_attribute' AS STRING"""
        return cls.find_code_attribute(code_obj)
    

    @classmethod
    def find_varaiable_names(cls, code_obj):
        """RETURNS TUPLE CONTAINING VARIABLE NAMES FROM GIVEN FUNCTION"""
        return cls.find_code_attribute(code_obj, "co_names")

    @classmethod
    def function_name(cls, func_obj):
        """WRAPPER FOR 'find_code_attribute' TO FIND FUNCTION NAME"""
        return cls.find_code_attribute(func_obj)