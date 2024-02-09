#!/usr/bin/python3
'''
Module that contain user class
'''
from models.base_model import BaseModel


class User(BaseModel):
    '''
    Classs that represents a user

    Attributes:
    email(str): the email of the user
    password(str): the password of the user
    first_name(str): the first name of the user
    last_name(str): the second name of the user
    '''
    email = ''
    password = ''
    first_name = ''
    last_name = ''
