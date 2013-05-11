#!/usr/bin/python 
# -*- coding: utf-8 -*- 

import re
from random import choice

class KBaseBlack:
    def __init__(self):
        self.sub_items = []
        self.parent = None

    def append(self, sub_item):
        if sub_item is not None:
            self.sub_items.append(sub_item)
            sub_item.parent = self
        return self

    def get_title(self):
        return None

    def get_parent(self):
        return self.parent

class KMethod(KCodeBlock):
    def __init__(self, title):
        KCodeBlock.__init__(self)
        self.title=title

    def get_title(self):
        return self.title

class KCommand():
    def __init__(self, rule = None, return_mode = True, random_key = 0):
        KCodeBlock.__init__(self, rule, return_mode, random_key)

    def process(self, input_string):
        if self.rule is None:
            return input_string

        return self.rule.apply(input_string)

class KCodeBlock(KBaseBlock, KCommand):
    def __init__(self, rule = None, return_mode = True, random_key = 0):
        KBaseBlock.__init__(self)
        self.rule = rule
        self.return_mode = return_mode
        self.random_key = random_key

    def can_be_used_for(self, input_string):
        return self.rule is None or self.rule.test(unput_string)

    def is_return_mode(self, return_mode):
        return self.return_mode

    def get_random_key(self, key):
        return self.random_key

    def is_random_select(self, key):
        return self.random_key is not None and self.random_key > 0

    def CreateBlock(self, rule, return_mode, random_key):
        new_block = KCodeBlock(rule, return_mode, random_key)
        self.append(new_block)
        return new_block

    def CreateCommand(self, rule, return_mode, random_key):
        new_block = KCodeBlock(rule, return_mode, random_key)
        self.append(new_block)
        return self

    def Block(self, rule = None, return_mode = True, random_key = 0):
        return self.CreateBlock(rule, return_mode, random_key)

    def Branch(self, rule = None, random_key = 0):
        return self.CreateBlock(rule, True, random_key)

    def Converter(self, rule):
        return self.CreateCommand(rule, False, 0)

    def Returner(self, rule):
        return self.CreateCommand(rule, True, 0)

    def End(self):
        return new_block.get_parent()

    def process(self, input_string):
        blocks_to_exec = []
        for sub_item in sub_items:
            if sub_item.can_be_used_for(input_string):
                if sub_item.is_random_select():
                    blocks_to_exec.append(sub_item)
                    continue
                input_string = sub_item.process(input_string)
                if sub_item.is_return_mode():
                    return input_string

        if len(blocks_to_exec):
            sub_item = choice(blocks_to_exec)
            input_string = sub_item.process(input_string)

        return input_string

class KProcessorModulesPool(KBaseBlock):
    def __init__(self):
        KBaseBlock.__init__(self)

    def process(self, input_string, module_name):
        module_to_exec = None
        for module in self.sub_items:
            if module.get_title() == module_name:
                return module_to_exec.process(input_string)
        return input_string

class RuleValidator:
    CMD_COMPARE_EQ = 1
    CMD_COMPARE_NOTEQ = 2
    def __init__(self, compare_command, comparation_set):
        self.comparation_set = None
        self.compare_command = compare_command

    def _get_compare_command(self):
        return self.compare_command

    def test(self, input_string):
        compare_command = self._get_compare_command()
        for comparation_item in self.comparation_set:
            if comparation_item.match(input_string):
                return compare_command == self.CMD_COMPARE_EQ
        return compare_command == self.CMD_COMPARE_NOTEQ

    def replace(self, input_string, replacement):
        if replacement is None:
            replacement = ""
        for comparation_item in self.comparation_set:
            if comparation_item.match(input_string):
                return re.sub(comparation_item,  "\\1%s\\2" % replacement, input_string)
        return None

    def load_comparation_set(self, comparation_set):
        self.comparation_set = []
        for comparation_item in comparation_set:
            new_comparation_item = comparation_item.replace("-", "(.*)")
            if comparation_item[0] != "-":
                new_comparation_item = "()"+new_comparation_item
            if comparation_item[-1] != "-":
                new_comparation_item = new_comparation_item + "()"
            self.comparation_set.append(re.compile(new_comparation_item))
        return self