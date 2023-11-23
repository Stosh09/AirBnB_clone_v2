#!/usr/bin/python3

""" Module for state class class """

from tests.test_models.test_base_model import test_basemodel
import os
from models.state import State


class test_state(test_basemodel):
    """
    test cases for state class
    """

    def __init__(self, *args, **kwargs):
        """
        state class innit method
        """

        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """
        testing state name attribute
        """

        new = self.value()
        self.assertEqual(type(new.name), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))
