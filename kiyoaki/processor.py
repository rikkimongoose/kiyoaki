#!/usr/bin/python 
# -*- coding: utf-8 -*- 

import re

class BaseProcessor:
    LOGIC = 1
    PROCESSOR = 2
    BRANCH = 4
    LOOP = 8
    CONTAINER = 16
    BRANCH_CONTAINER = BRANCH + CONTAINER
    def __init__(self, add_notification=None):
        self.sub_items = []
        self.add_notification_command = add_notification
        self.processor_block_type = self.CONTAINER

    def get_type(self):
        return self.processor_block_type

    def is_ready_to_return(self):
        return False

    def get_value_to_return(self):
        return None

    def append(self, module):
        if module is not None:
            self.sub_items.append(module)
        return self

    def add_notification(self, title, message):
        if add_notification_command is not None:
            add_notification_command(title, message)

class ProcessorModulesPool(BaseProcessor):
    def __init__(self, add_notification = None):
        BaseProcessor.__init__(self, add_notification)

    def process(self, input_string, module_name):
        module_to_exec = None
        for module in self.sub_items:
            if hasattr(module, "title") and module.title == module_name:
                module_to_exec = module
                break
        if module_to_exec is not None:
            return module_to_exec.process(input_string)

class ProcessModule(BaseProcessor):
    def __init__(self, title, add_notification = None):
        BaseProcessor.__init__(self, add_notification)
        self.title = title

    def process(self, input_string):
        result = []
        for sub_item in self.sub_items:
            sub_item.process(input_string)
            if sub_item.is_ready_to_return():
                return sub_item.get_value_to_return()
            input_string = new_val
        return input_string

class ProcessBranchBlock(BaseProcessor):
    def __init__(self, add_notification = None):
        BaseProcessor.__init__(self, add_notification)
        self.ready_to_return = False
        self.value_to_return = None
        self.processor_block_type = self.BRANCH_CONTAINER
        self.finished = True

    def process(self, input_string):
        for sub_item in self.sub_items:
            if sub_item.get_type() in (self.BRANCH, self.BRANCH_CONTAINER) and sub_item.test(input_string):
                sub_item.process(input_string)
                if sub_item.is_ready_to_return():
                    self.value_to_return = sub_item.get_value_to_return()
                    self.ready_to_return = True
                    break

    def is_ready_to_return(self):
        return self.ready_to_return

    def get_value_to_return(self):
        return self.value_to_return

    def is_finished(self):
        return self.finished

class ProcessBranch(ProcessBranchBlock):
    def __init__(self, rule_validator, add_notification = None):
        ProcessBranchBlock.__init__(self, add_notification)
        self.processor_block_type = self.BRANCH
        self.rule_validator = rule_validator
    
    def test(self, input_string):
        return self.rule_validator is None or self.rule_validator.test(input_string)

class TextProcessor(ProcessBranch):
    def __init__(self, rule_validator, replacement, add_notification = None):
        ProcessBranch.__init__(self, rule_validator, add_notification)
        self.replacement = replacement

    def process(self, input_string):
        if self.rule_validator is None:
            return None
        replaced = self.rule_validator.replace(input_string, self.replacement)
        if replaced != input_string:
            self.value_to_return = replaced
            self.ready_to_return = True

class RuleValidator:
    CMD_COMPARE_EQ = 1
    CMD_COMPARE_NOTEQ = 2
    def __init__(self, compare_command, comparation_set):
        self.comparation_set = comparation_set
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