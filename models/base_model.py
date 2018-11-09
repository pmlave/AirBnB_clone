#!/usr/bin/python3
'''
module 'base_model'
'''

import uuid
from datetime import datetime

class BaseModel:
    """
    BaseModel class used with all all other classes
    """

    id = str(uuid.uuid4())
    created_at = datetime.now()
    updated_at = datetime.now()


    def __str__(self):
        '''
        string representation of BaseModel instance
        '''
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def to_dict(self):
        '''
        dictionary representation of an instance
        '''
        new_dict = dict(self.__dict__)
        for key, value in self.__dict__.items():
            if key == 'created_at':
                new_dict['created_at'] = self.__dict__[key].isoformat()
            if key == 'updated_at':
                new_dict['updated_at'] = self.__dict__[key].isoformat()
        
