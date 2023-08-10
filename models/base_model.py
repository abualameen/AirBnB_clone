#!/usr/bin/python3
"""
This module is the base class

"""
import uuid
from datetime import datetime


class BaseModel:
    """
    this is the class Basemodel that all other class in
    the project would inherite from

    """
    def __init__(self):
        """
        this method initializes a new instance of the BaseModel
        it assigns a unique ID and sets time for creation and updating of time

        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        this method returns a string representation of the BaseModel instance
        with this format [<class name>] (<self.id>) <self.__dict__>

        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        This method update the public instance attribute updated_at with
        the current datetime

        """
        self.updated_at = datetime.now()

    def to_dic(self):
        """
        this method converts the instance attributes to a dictionary

        Returns:
            dict: A dictionary containing all keys/values of __dict__.

        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
