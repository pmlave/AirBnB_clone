#!/usr/bin/python3

import unittest
from models.place import Place
from models.base_model import BaseModel


class placeTest(unittest.TestCase):
    '''
    Test cases for base_model class
    '''
    def setUp(self):
        """
        simple set up
        """
        self.new_inst = Place()

    def tearDown(self):
        """
        tear down method
        """
        del self.new_inst

    def test_is_basemodel_instance(self):
        """
        checks if new_inst is an instance of BaseModel
        """
        self.assertIsInstance(self.new_inst, BaseModel)

    def test_city_id_is_string(self):
        """
        test to verify if the value passed to the city_id is a string
        """
        self.assertEqual(str(type(self.new_inst.city_id)), "<class 'str'>")

    def test_user_id(self):
        """
        test to verify if value passed to user_id is a string
        """
        self.assertEqual(str(type(self.new_inst.user_id)), "<class 'str'>")

    def test_name(self):
        """
        test to verify if value passed to name is a string
        """
        self.assertEqual(str(type(self.new_inst.name)), "<class 'str'>")

    def test_description(self):
        """
        test to verify if value passed to description is a string
        """
        self.assertEqual(str(type(self.new_inst.description)), "<class 'str'>")

    def test_number_rooms(self):
        """
        test to verify if value passed to number_rooms is an integer
        """
        self.assertEqual(str(type(self.new_inst.number_rooms)),
                         "<class 'int'>")

    def test_max_guest(self):
        """
        test to verify if value passed to max_guest is an integer
        """
        self.assertEqual(str(type(self.new_inst.max_guest)), "<class 'int'>")

    def test_price(self):
        """
        test to verify if value passed to price by night is an integer
        """
        self.assertEqual(str(type(self.new_inst.price_by_night)),
                         "<class 'int'>")

    def test_latitude(self):
        """
        test to verify if value passed to latitude is a float
        """
        self.assertEqual(str(type(self.new_inst.latitude)), "<class 'float'>")

    def test_longitude(self):
        """
        test to verify if value passed to longitude is a float number
        """
        self.assertEqual(str(type(self.new_inst.longitude)), "<class 'float'>")

    def test_amenity_ids(self):
        """
        test to verify if value passed to amenity_ids is a list
        """
        self.assertEqual(str(type(self.new_inst.amenity_ids)),
                         "<class 'list'>")
