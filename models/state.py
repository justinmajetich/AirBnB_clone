#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
import uuid  # Import the uuid module

class State(BaseModel):
    """ State class """
    name = ""

    def __init__(self, *args, **kwargs):
        """ Initialize State class """
        super().__init__(*args, **kwargs)

        # Generate the 'id' attribute if it doesn't exist
        if not hasattr(self, 'id'):
            self.id = str(uuid.uuid4())