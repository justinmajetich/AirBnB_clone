#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel


class State(BaseModel):
    """ State class """
    name = ""

    print("Hola estoy en el state")
    def __init__(self, *args, **kwargs):
        print("SOY EL KWARGS-> {}".format(kwargs))
        super().__init__()
        if kwargs is not None and kwargs != {}:
            for key in kwargs.keys():
                if hasattr(self, key) and key != '__class__':
                    setattr(self, key, kwargs[key])
