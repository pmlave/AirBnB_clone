#!/usr/bin/python3

import unittest
from models.base_model import BaseModel
import datetime

class TestBaseModel(unittest.TestCase):
    '''
    Test cases for base_model class
    '''

    def setUp(self):
        '''
        simple set up
        '''
        self.new_instance = BaseModel()

    def tearDown(self):
        '''
        tear down method
        '''
        del self.new_instance

    def test_id_is_string(self):
        '''
        testing to verify id is a string
        '''
        self.assertEqual(str(type(self.new_instance.id)), "<class 'str'>")

    def test_created_at_is_datetimeobj(self):
        '''
        tests if created_at is a datetime object
        '''
        self.assertEqual(str(type(self.new_instance.created_at)),
                         "<class 'datetime.datetime'>")

    def test_updated_at_is_datetimeobj(self):
        '''
        tests if updated_at is a datetime object
        '''
        self.assertEqual(str(type(self.new_instance.updated_at)),
                         "<class 'datetime.datetime'>")

    def test_to_dict_type(self):
        '''
        test type of to_dict method
        '''
        basemodel_dict = self.new_instance.to_dict()
        self.assertEqual(str(type(basemodel_dict)), "<class 'dict'>")
