#!/usr/bin/python 
# -*- coding: utf-8 -*-

from namegen import *

class SecondNameGenerator(NameGenerator):
    """ Generates a random second name based on the array of existing ones.

        Usage:
            generator = SecondNameGenerator(array_with_surnames)
            print generator.generate()
    """
    def __init__(self, source_array):
        NameGenerator.__init__(self, source_array)

if __name__ == "__main__":
    print SecondNameGenerator.__doc__