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

    def testMaleName(self):
        code_block = KCodeBlock()
        code_block.Converter(RuleValidator(["-а", "-я"], "ич")).Converter(RuleValidator(["Ираклий"], "Ираклиевич")) \
                  .Converter(RuleValidator(["-ий", "-ь"], "ьевич")).Converter(RuleValidator(["-ай"], "аевич")) \
                  .Converter(RuleValidator([""], "ович"))
        self.assertEqual(code_block.process("Илья"), "Ильич")
        self.assertEqual(code_block.process("Лука"), "Лукич")
        self.assertEqual(code_block.process("Ираклий"), "Ираклиевич")
        self.assertEqual(code_block.process("Жюль"), "Жюльевич")
        self.assertEqual(code_block.process("Мазай"), "Мазаевич")

        print code_block.process("Александр")

if __name__ == "__main__":
    unittest.main()