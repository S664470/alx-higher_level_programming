#!/usr/bin/python3
"""Defines a base model class."""
import json


class Base:
    """Represent the base model.
    Represents the "base" for all other classes in project 0x0C*.
    Attributes:
        __nb_objects (int): The number of instantiated Bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base.
        Args:
            id (int): The identity of the new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

            """
            JSON REPRESNTATION OF STRING
            """
    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
    """
    Class to write the string represintation of list_objs
    """

    @staticmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__ + ".json"
        list_objs = [list_dictionaries]

        with open(filename, 'w'):
            if list_objs is None:
                filename.write("[]")
            else:
                ls_dic = [o.to_dictionary() for o in list_objs]
                filename.write(Base.to_json_string(list_dicts))
