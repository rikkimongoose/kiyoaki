#!/usr/bin/python 
# -*- coding: utf-8 -*- 

import unittest
from processor import *
import re

validator = RuleValidator(RuleValidator.CMD_COMPARE_EQ, [re.compile(r"(.*)ь()")])
validatorL = RuleValidator(RuleValidator.CMD_COMPARE_EQ, [re.compile(r"()Л(.*)")])
validator_branch1 = RuleValidator(RuleValidator.CMD_COMPARE_EQ, [re.compile(r"()Л(.*)")])
validator_branch2 = RuleValidator(RuleValidator.CMD_COMPARE_EQ, [re.compile(r"()Н(.*)")])
processor = TextProcessor(validator, "ин")
processorN = TextProcessor(validatorL, "L", False)
processorL = TextProcessor(validator, "ин", False)
branch1 = ProcessBranch(validator_branch1)
branch1.append(processor)
branch2 = ProcessBranch(validator_branch2)
branch2.append(processor)
branch_block = ProcessBranchBlock()
branch_block.append(branch1).append(branch2)
process_module_line = ProcessModule("postfix_name_linear")
process_module_line.append(processorN).append(processorL)
process_module = ProcessModule("postfix_name")
process_module.append(branch_block)
processor_modules_pool = ProcessorModulesPool()
processor_modules_pool.append(process_module)

class ProcessorModulesPool(unittest.TestCase):
    def testProcessing(self):
        self.assertEqual(processor_modules_pool.process("Лень", "postfix_name"), "Ленин")

class ProcessBranchBlockTest(unittest.TestCase):
    def testProcessing(self):
        branch_block.process("Лень")
        self.assertTrue(branch_block.is_ready_to_return())
        self.assertEqual(branch_block.get_value_to_return(), "Ленин")
        branch_block.process("Нень")
        self.assertTrue(branch_block.is_ready_to_return())
        self.assertEqual(branch_block.get_value_to_return(), "Ненин")
    
    def testLineProcessing(self):
        self.assertEqual(process_module_line.process("Лень"), "Lенин")

class TextProcessor(unittest.TestCase):
    def testProcessing(self):
        processor.process("Лень")
        self.assertTrue(processor.is_ready_to_return())
        self.assertEqual(processor.get_value_to_return(), "Ленин")

class RuleValidatorTest(unittest.TestCase):
    def testTest(self):
        self.assertTrue(validator.test("Лень"))

    def testReplace(self):
        self.assertEqual(validator.replace("Лень", "ин"), "Ленин")

if __name__ == "__main__":
    unittest.main()