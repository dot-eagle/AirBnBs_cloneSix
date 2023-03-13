#!/usr/bin/python3
""" Module for User Class """

from models.base_model import BaseModel

class User(BaseModel):
    """ def Class that defines a User and inherits from BaseModel """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
