#!/usr/bin/python 
# -*- coding: utf-8 -*- 

from morphgen import *
from bases.surnames import *

class KiyoakiCore:
    VERSION = "0.1"
    """ Core class for Kiyoaki project. Generates Russian names with surnames.
    """
    @staticmethod
    def generate_surname(surnames_array = None):
        if surnames_array is None:
            surnames_array = DEFAULT_SURNAMES

        generator = MorphemGenerator(surnames_array)
        return generator.generate()

    @staticmethod
    def generate_name():
        return ""

    @staticmethod
    def generate_secondname():
        return ""

    @staticmethod
    def get_ver():
        return KiyoakiCore.VERSION

    @staticmethod
    def generate(surnames_array = None):
        return "%s %s %s" % (KiyoakiCore.generate_surname(), KiyoakiCore.generate_name(), KiyoakiCore.generate_secondname())

if __name__ == "__main__":
    print KiyoakiCore.__doc__
    print "A sample generated surname:\n"
    print KiyoakiCore.generate()