#!/usr/bin/python3

class Validator():
    def __init__(self, *args, **kwargs):
        print("SOY EL KWARGS-> {}".format(kwargs))
        super().__init__()
        if kwargs is not None and kwargs != {}:
            for key in kwargs.keys():
                if hasattr(self, key) and key != '__class__':
                    setattr(self, key, kwargs[key])
