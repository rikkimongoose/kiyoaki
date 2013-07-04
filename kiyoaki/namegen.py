#!/usr/bin/python 
# -*- coding: utf-8 -*-

import random

class NameGenerator:
    """ Generates a random name based on the array of existing ones.

        Usage:
            generator = NameGenerator(array_with_surnames)
            print generator.generate()
    """
    def __init__(self, source_array):
        object.__init__(self)
        self.source_array = source_array

    def generate(self):
        """ Generate a name based on the array of template surnames.
        """
        name_index = random.randint(0, len(self.source_array) - 1)
        return self.source_array[name_index]

if __name__ == "__main__":
    print NameGenerator.__doc__
