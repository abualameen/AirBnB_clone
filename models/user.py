#!/usr/bin/python3
"""
this is the user model

"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    this is the user class that inherite from the basemodel
 
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
