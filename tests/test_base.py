#!/usr/bin/python3
"""Unittest base.
Test cases for BaseModel class.
"""


import unittest
from datetime import datetime

from models.base_model import BaseModel

class TestBase(unittest.TestCase):
    """Test class for BaseModel class."""

    def test_base(self):
        """
        Testing for BaseModel attributes
        """

        # Check that object working well and the same type of class
        my_model = BaseModel()
        current_date = datetime.now()
        self.assertTrue(type(my_model), BaseModel)

        # Check that name attribute is added and type of string
        my_model.name = "My First Model"
        self.assertEqual(my_model.name, "My First Model")
        self.assertTrue(type(my_model.name), str)

        # Checking for time is correct for created_at attribute,
        # but checked in year, month, day, hours, minute, second.
        # not contain nanoSeconds
        current_date = current_date.strftime("%Y-%m-%dT%H:%M:%S")
        excepted_ouput = my_model.created_at.strftime("%Y-%m-%dT%H:%M:%S")
        self.assertEqual(excepted_ouput, current_date)

        # Checking for time is correct for updated_at attribute.
        excepted_ouput = my_model.updated_at.strftime("%Y-%m-%dT%H:%M:%S")
        self.assertEqual(excepted_ouput, current_date)

        # Check that updated_at and created_at have the same value
        self.assertTrue(my_model.updated_at, my_model.created_at)

        # Checking that two id of two objects are uniqe
        my_model2 = BaseModel()
        self.assertNotEqual(my_model.id, my_model2.id)

        # Check that id is of type string
        self.assertIsInstance(my_model.id, str)
        self.assertIsInstance(my_model2.id, str)

if __name__ == '__main__':
    unittest.main()