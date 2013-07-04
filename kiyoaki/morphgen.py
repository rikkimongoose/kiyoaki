#!/usr/bin/python 
# -*- coding: utf-8 -*-

IS_UTF8 = 1
# the unicode indexes in Python 2.x are 
ITERATOR = 1 << IS_UTF8

import random
import re
from morphnode import *

class MorphemGenerator:
    """ Generates a fake surname based on the array of existing ones.

        Usage:
            generator = MorphemGenerator(array_with_surnames)
            print generator.generate()
    """
    DEFAULT_START_INDEX = 3

    def __init__(self, source_array, fixes_array = None, start_index = DEFAULT_START_INDEX):
        self.start_index = start_index * ITERATOR
        self.source_array = source_array
        self.fixes_array = fixes_array
        self.do_fix = fixes_array is not None

        self.sources = []
        self.prefixes = []
        self.postfixes = []

    def _get_morphem(self, morphem_array, text):
        for morphem in morphem_array:
            if morphem.get_text() == text:
                return morphem
        return None

    def _append_morphem(self, morphem_array, text, can_be_single = False):
        morphem_node = self._get_morphem(morphem_array, text)
        if morphem_node is not None:
            morphem_node.inc()
        else:
            morphem_node = MorphemNode(text, can_be_single)
            morphem_array.append(morphem_node)
        return morphem_node

    def _load_source(self):
        for source_item in self.source_array:
            self._append_source_str(source_item)
        return self

    def _append_source_str(self, text):
        if text not in self.sources:
            self.sources.append(text.lower())

    def _compile(self):
        while len(self.sources):
            self._compile_item(self.sources.pop())
        return self

    def _compile_item(self, text):
        index = len(text) - self.start_index
        was_parsed_head, was_parsed_tail = False, False

        # Prefix is built from the end
        while not was_parsed_tail and index > self.start_index:
            text_head = text[:index]
            text_tail = text[index:]
            index -= ITERATOR

            ready_morphem = self._get_morphem(self.postfixes, text_tail)
            if ready_morphem is not None:
                ready_morphem.inc()
                was_parsed_tail = True

            ready_morphem = self._get_morphem(self.prefixes, text_head)
            if ready_morphem is not None:
                ready_morphem.inc()
                was_parsed_head = True

            for source_item_text in self.sources:
                if not was_parsed_head:
                    if source_item_text == text_head:
                        self._append_morphem(self.prefixes, text_head, True)
                        was_parsed_head = True
                    elif source_item_text.find(text_head) == 0:
                        self._append_morphem(self.prefixes, text_head)
                        was_parsed_head = True

        # Postfix is built from the beginning
        index = self.start_index
        while not was_parsed_tail and index < len(text):
            text_tail = text[index:]
            index += ITERATOR

            ready_morphem = self._get_morphem(self.postfixes, text_tail)
            if ready_morphem is not None:
                ready_morphem.inc()
                was_parsed_tail = True

            for source_item_text in self.sources:
                if not was_parsed_tail:
                    tail_pos = source_item_text.find(text_tail)
                    if tail_pos > -1 and tail_pos == len(source_item_text) - len(text_tail):
                        self._append_morphem(self.postfixes, text_tail)
                        was_parsed_tail = True

        if not was_parsed_head and not was_parsed_tail:
            self._append_morphem(self.prefixes, text, True)

    def _clear(self):
        lambda_filter_applied = lambda item: item.is_single() or (item.get_count() > 1)
        self.prefixes = filter(lambda_filter_applied, self.prefixes)
        self.postfixes = filter(lambda_filter_applied, self.postfixes)
        return self

    def fix_mixes(self, word):
        if self.fixes_array is None or not self.do_fix:
            return word
        for fix_item in self.fixes_array:
            word = word.decode("utf-8").replace(fix_item[0], fix_item[1]).encode("utf-8")
        return word
        
    def _do_generate(self):
        node_head = MorphemGenerator.get_markov_node(self.prefixes)
        if node_head.is_single() and random.randint(0, 1):
            return node_head.get_text()
        node_head_text = node_head.get_text()

        node_tail = MorphemGenerator.get_markov_node(self.postfixes)
        node_tail_text = node_tail.get_text()

        if node_head_text[-ITERATOR:] == node_tail_text[:ITERATOR]:
            text_line = "%s%s" % (node_head_text, node_tail_text[ITERATOR:])
        text_line = "%s%s" % (node_head_text, node_tail_text)

        return text_line.title()

    def generate(self):
        """ Generate a surname based on the array of template surnames.
        """
        return self.fix_mixes(self._load_source()._compile()._clear()._do_generate())

    @staticmethod
    def get_markov_node(nodes_array):
        """ Get the next node in Markov chain according to its value.
        """
        markov_sum = 0
        for node in nodes_array:
            markov_sum += node.get_count()

        rand_sum_elem = random.randint(1, markov_sum)

        markov_sum = 0
        for node in nodes_array:
            markov_sum += node.get_count()
            if markov_sum >= rand_sum_elem:
                return node
        return None

    def __str__(self):
        output_str = "Prefixes\n=======\n"
        for morphem in self.prefixes:
            output_str += "%s\n" % str(morphem)
        output_srt += "\nPostfixes\n=======\n"
        for morphem in self.postfixes:
            output_str += "%s\n" % str(morphem)
        return output_str

if __name__ == "__main__":
    print MorphemGenerator.__doc__
