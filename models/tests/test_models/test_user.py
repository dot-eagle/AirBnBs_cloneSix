#!/usr/bin/python3
""" Tests for User class module """

import models
from models.base_model import BaseModel
from models.user import User

import os
import unittest


class TestUser(unittest.TestCase):
    """ Start off tests """

    def test_docstring(self):
        """ Test if funcions, methods, classes
        and modules have docstrin """
        msj = "Módulo does not has docstring"
        self.assertIsNotNone(models.user.__doc__, msj)  # Modules
        msj = "Clase does not has docstring"
        self.assertIsNotNone(User.__doc__, msj)  # Classes

    def test_executable_file(self):
        """ Test if file has permissions u+x to execute """
        # Check for read access
        is_read_true = os.access('models/user.py', os.R_OK)
        self.assertTrue(is_read_true)
        # Check for write access
        is_write_true = os.access('models/user.py', os.W_OK)
        self.assertTrue(is_write_true)
        # Check for execution access
        is_exec_true = os.access('models/user.py', os.X_OK)
        self.assertTrue(is_exec_true)

    def test_is_an_instance(self):
        """ check if my_model is an instance of BaseModel """
        my_user = User()
        self.assertIsInstance(my_user, User)
