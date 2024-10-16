#!/usr/bin/python3
'''
This module defines a class Student that retrieves a dictionary representation and reloads attributes from a JSON dictionary.
'''

class Student:
    '''
    Defines a student by first_name, last_name, and age.
    '''

    def __init__(self, first_name, last_name, age):
        '''
        Initializes a Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''
        Retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list): A list of attribute names to retrieve.

        Returns:
            dict: The dictionary representation of the Student instance.
        '''
        if attrs is None:
            return self.__dict__
        return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}

    def reload_from_json(self, json):
        '''
        Replaces all attributes of the Student instance with values from a JSON dictionary.

        Args:
            json (dict): A dictionary containing attribute-value pairs.
        '''
        for key, value in json.items():
            setattr(self, key, value)
