#!/usr/bin/python
"""A class User that inherits from BaseModel"""

from models.base_model import BaseModel

class User(BaseModel):
    """Represents a class User
    """

    def __init__(self):
        """User Instantiation
        """

        email = ''
        password = ''
        first_name = ''
        last_name = ''
