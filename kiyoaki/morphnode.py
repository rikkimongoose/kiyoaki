#!/usr/bin/python 
# -*- coding: utf-8 -*-

class MorphemNode:
    """ A node with text of morphem and count if its usage in source array.
    """
    def __init__(self, text=None, can_be_single = False):
        object.__init__(self)
        self.text = text
        self.can_be_single = can_be_single
        self.count = 1

    def get_text(self):
        return self.text

    def inc(self):
        self.count += 1
        return self

    def get_count(self):
        return self.count

    def is_single(self):
        return self.can_be_single

    def __str__(self):
        return "%s (%s:%s)" % (self.get_text(), self.get_count(), self.is_single())

if __name__ == "__main__":
    print MorphemNode.__doc__