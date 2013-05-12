#!/usr/bin/python 
# -*- coding: utf-8 -*- 

import unittest
import re

from processor import *


class ProcessorModulesPool(unittest.TestCase):
    def testCreateBlock(self):
        code_block = KCodeBlock()

    def testProcessing(self):
        code_block = KCodeBlock()
        code_block.Converter(RuleValidator(["-ь"], "ин"))
        self.assertEqual(code_block.process("Лень"), "Ленин")


if __name__ == "__main__":
    unittest.main()