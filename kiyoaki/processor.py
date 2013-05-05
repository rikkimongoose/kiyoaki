#!/usr/bin/python 
# -*- coding: utf-8 -*- 

import re
from random import choice

class KBaseBlack:
    def __init__(self):
        self.sub_items = []

    def append(self, module):
        if module is not None:
            self.sub_items.append(module)
        return self

    def get_title(self):
        return None

class KCodeBlock(KBaseBlock):
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

class KMethod(KCodeBlock):
    def __init__(self, title):
        KCodeBlock.__init__(self)
        self.title=title

    def get_title(self):
        return self.title

class KCommand(KCodeBlock):
    def __init__(self, rule = None, return_mode = True, random_key = 0):
        KCodeBlock.__init__(self, rule, return_mode, random_key)

    def process(self, input_string):
        if self.rule is None:
            return input_string

        return self.rule.apply(input_string)

class KProcessorModulesPool(KBaseBlock):
    def __init__(self):
        KBaseBlock.__init__(self)

    def process(self, input_string, module_name):
        module_to_exec = None
        for module in self.sub_items:
            if module.get_title() == module_name:
                return module_to_exec.process(input_string)
        return input_string