#!/usr/bin/python3
""" Tests for Amenity class module """

import os
import unittest
import models

from models.base_model import BaseModel
from models.amenity import Amenity

class TestState(unittest.TestCase):
    """ Start off tests """

    def test_docstring(self):
        """ Test if funcions, methods, classes
        and modules have docstrin """

        msj = "Módulo does not has docstring"
        self.assertIsNotNone(models.amenity.__doc__, msj)  # Modules
        msj = "Clase does not has docstring"
        self.assertIsNotNone(Amenity.__doc__, msj)  # Classes

    def test_executable_file(self):
        """ Test if file has permissions u+x to execute """
        # Check for read access
        is_read_true = os.access("models/amenity.py", os.R_OK)
        self.assertTrue(is_read_true)
        # Check for write access
        is_write_true = os.access("models/amenity.py", os.W_OK)
        self.assertTrue(is_write_true)
        # Check for execution access
        is_exec_true = os.access("models/amenity.py", os.X_OK)
        self.assertTrue(is_exec_true)

    def test_is_an_instance(self):
        """ Check if my_model is an instance of BaseModel """
        my_amenity = Amenity()
        self.assertIsInstance(my_amenity, Amenity)
