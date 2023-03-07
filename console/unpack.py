#!/usr/bin/python3

class UnpackingTool:

    @classmethod
    def _retrieve_classes(cls, namespace):
        return {
            key: value for key, value in namespace.items()
                if isinstance(value, type)
        }
    
    @classmethod
    def _retrieve_object_methods(cls, namespace, object_name="HBNBCommand"):
        
        source_mods = {
            key: value for key, value in namespace.items()
                if object_name in key
        }
        return {
            method.__name__: method for method in
                [list(vars(x).items())[-1][1] for x in source_mods.values()]
        }

    @classmethod
    def activate(cls, namespace, object_name="HBNBCommand"):
        return {
            "prompt": '(hbnb) ',
            "models": globals()["models"],
            "classes": cls._retrieve_classes(namespace),
            **cls._retrieve_object_methods(namespace, object_name)
        }
