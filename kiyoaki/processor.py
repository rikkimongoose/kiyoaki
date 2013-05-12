#!/usr/bin/python 
# -*- coding: utf-8 -*- 

import re
from random import choice

class KBaseBlock:
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

class KMethod(KBaseBlock):
    def __init__(self, title):
        KBaseBlock.__init__(self)
        self.title=title

    def get_title(self):
        return self.title

class KCodeBlock(KBaseBlock):
    def __init__(self, rule = None, return_mode = True, random_key = 0):
        KBaseBlock.__init__(self)
        self.rule = rule
        self.return_mode = return_mode
        self.random_key = random_key

    def can_be_used_for(self, input_string):
        return self.rule is None or self.rule.test(input_string)

    def is_return_mode(self):
        return self.return_mode

    def get_random_key(self, key):
        return self.random_key

    def is_random_select(self):
        return self.random_key is not None and self.random_key > 0

    def AddRule(self, rule):
        self.rule = rule
        return self

    def CreateBlock(self, rule, return_mode = False, random_key = True):
        new_block = KCodeBlock(rule, return_mode, random_key)
        self.append(new_block)
        return new_block

    def CreateCommand(self, rule, return_mode = True, random_key = 0):
        new_block = KCommand(rule, return_mode, random_key)
        self.append(new_block)
        return new_block

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
        for sub_item in self.sub_items:
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


class KCommand(KCodeBlock):
    def __init__(self, rule = None, return_mode = True, random_key = 0):
        KCodeBlock.__init__(self, rule, return_mode, random_key)

    def process(self, input_string):
        if self.rule is None:
            return input_string

        return self.rule.replace(input_string)

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
    def __init__(self, comparation_set, replacement):
        self.comparation_set = []
        if comparation_set is not None:
            self.load_set(comparation_set)
        self.replacement = replacement

    def test(self, input_string):
        for comparation_item in self.comparation_set:
            if comparation_item.match(input_string):
                return True
        return False

    def replace(self, input_string):
        for comparation_item in self.comparation_set:
            if comparation_item.match(input_string):
                return re.sub(comparation_item,  "\\1%s\\2" % self.replacement, input_string)
        return None

    def load_set(self, comparation_set):
        for comparation_item in comparation_set:
            self.comparation_set.append(re.compile(self.parse_comparation_item(comparation_item)))
        return self

    def parse_comparation_item(self, comparation_item):
        new_comparation_item = comparation_item.replace("-", "(.*)")
        if comparation_item[0] != "-":
            new_comparation_item = "()"+new_comparation_item
        if comparation_item[-1] != "-":
            new_comparation_item = new_comparation_item + "()"
        return new_comparation_item


if __name__ == "__main__":
    print "Base classes for Kiyoaki project"