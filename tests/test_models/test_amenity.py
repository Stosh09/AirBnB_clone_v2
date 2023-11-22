#!/usr/bin/python3

""" Module for testing amenity class """

from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity
import os


class test_Amenity(test_basemodel):
    """
    Amenity testing class
    """

    def __init__(self, *args, **kwargs):
        """
        innit testing class
        """

        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """
        testing name types for db and the file storage
        """

        new = self.value()
        self.assertEqual(type(new.name), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))
