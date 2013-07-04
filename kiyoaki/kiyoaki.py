#!/usr/bin/python 
# -*- coding: utf-8 -*- 

from morphgen import *
from namegen import *
from secondnamegen import *

from bases.surnames import *
from bases.names import *
from bases.secondnames import *

class KiyoakiCore:
    VERSION = "0.1.1"
    """ Core class for Kiyoaki project. Generates Russian names with surnames.
    """
    @staticmethod
    def generate_surname(surnames_array = None, surnames_fixes = None):
        if surnames_array is None:
            surnames_array = DEFAULT_SURNAMES
        if surnames_fixes is None:
            surnames_fixes = DEFAULT_SURNAMES_FIXES
        
        generator = MorphemGenerator(surnames_array, surnames_fixes)
        return generator.generate()

    @staticmethod
    def generate_name(names_array = None):
        if names_array is None:
            names_array = DEFAULT_NAMES

        generator = NameGenerator(names_array)
        return generator.generate()

    @staticmethod
    def generate_secondname(secondnames_array = None):
        if secondnames_array is None:
            secondnames_array = DEFAULT_SECONDNAMES

        generator = SecondNameGenerator(secondnames_array)
        return generator.generate()

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
