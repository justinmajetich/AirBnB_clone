"""
Implementation of custom exceptions
"""


class GetClassException(Exception):
    """Raised when a class is not found"""

    def __init__(self, model="BaseModel"):
        super().__init__(f"<{model}> is not found")


class GetInstanceException(Exception):
    """Raised when an instance is not found"""

    def __init__(self, id, model="BaseModel"):
        super().__init__(f"<{id}> is not associated with <{model}>")