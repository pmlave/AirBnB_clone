#!/usr/bin/python
"""A class review that inherits from BaseModel"""

from model.BaseModel import base_model

class Review(BaseModel):
    """Represents a class Review
    """
    place_id = ''
    user_id = ''
    text = ''
