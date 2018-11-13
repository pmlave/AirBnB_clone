#!/usr/bin/python3

import unittest
from models.amenity import Amenity


class amenityTest(unittest.TestCase):
    '''
    Test cases for base_model class
    '''
    def setUp(self):
        '''
        simple set up
        '''
        pass

    def test_id_is_string(self):
        '''
        testing to verify id is a string
        '''
        self.assertIsInstance(id, str)

if __name__ == '__main__':
    unittest.main()
