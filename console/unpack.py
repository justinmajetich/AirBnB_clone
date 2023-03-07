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
        
        return {
            key[key.index("d_") + 2:]: value for key, value in namespace.items()
                if object_name in key
        }

    @classmethod
    def activate(cls, namespace, object_name="HBNBCommand"):
        return {
            "prompt": '(hbnb) ',
            "models": namespace["models"],
            "classes": cls._retrieve_classes(namespace),
            **cls._retrieve_object_methods(namespace, object_name)
        }
