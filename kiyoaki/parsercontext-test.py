#!/usr/bin/python 
# -*- coding: utf-8 -*- 

import unittest
from parsercontext import *

parser_context = ParserContext()

class ParserContext(unittest.TestCase):
    def test_is_comment(self):
        self.assertTrue(parser_context.is_comment("# comment"))
        self.assertTrue(parser_context.is_comment("   # comment"))
        self.assertFalse(parser_context.is_comment("not a comment"))

    def test_is_finished(self):
        self.assertTrue(parser_context.is_finished("ooo[boo[bbbb[booo]booo]booo]ooof"))
        self.assertFalse(parser_context.is_finished("ooo[boo[bbbb[booo]booo]booo"))
        self.assertFalse(parser_context.is_finished("ooo[boo[bbbb[booo]booo]booo]]oof"))
        self.assertFalse(parser_context.is_finished("ooo[boo[bbbbbooo]booo]booo]ooof["))

if __name__ == "__main__":
    unittest.main()