#!/user/bin/python3
"""
this module is the Review module 

"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    this class is the Review class it inherite from BaseModel

    """
    place_id = ""
    user_id = ""
    text = ""
