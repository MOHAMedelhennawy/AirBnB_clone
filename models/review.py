#!/usr/bin/python3
"""
This Model contains review class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    class that defines the review

    Attributes:
    place_id (str): it will be the Place.id
    user_id (str): it will be the User.id
    text (str): empty text
    """
    place_id = ''
    user_id = ''
    text = ''
