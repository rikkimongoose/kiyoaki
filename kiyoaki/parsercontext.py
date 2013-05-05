import re

from lexer import *

class ParserContext:
    """ A context for parser to be executed
    """

    RegExComment = re.compile("\s*(#.*)?")
    ScopeSymbols = [("[", "]")]

    def __init__(self):
        self.lexer = Lexer(self)
        self.notifications = []

    def add_notification(self, title, descrition):
        """ Add the notification about an error during lexing or parsing.
        """
        self.notifications.add(ParserNotification(title, descrition))

    def is_comment(self, str_to_check):
        return ParserContext.RegExComment.match(str_to_check) is not None

    def is_finished(self, str_to_check):
        scope_count_list = {}

        for scope_symbol in ParserContext.ScopeSymbols:
            scope_count_list[scope_symbol[0]] = 0

        for s in str_to_check:
            for scope_symbol in ParserContext.ScopeSymbols:
                scope_symbol_0 = scope_symbol[0]
                if scope_symbol_0 == str(s):
                    scope_count_list[scope_symbol_0] = scope_count_list[scope_symbol_0] + 1
                elif scope_symbol[1] == str(s):
                    scope_count_list[scope_symbol_0] = scope_count_list[scope_symbol_0] - 1

                if scope_count_list[scope_symbol_0] < 0:
                    return False

        for scope_symbol in ParserContext.ScopeSymbols:
            if scope_count_list[scope_symbol[0]] != 0:
                return False

        return True

    def do_compile(self, source_loader):
        """ Compile a code provided in source_loader to a compiled text processor.
        """
        lexems = self.lexer.get_lexems(source_loader)
        if lexems is None:
            return None
        compiled_processor = self.parser.compile(lexems)
        if compiled_processor is None:
            return None
        return compiled_processor

class ParserNotification:
    def __init__(self, title, descrition):
        self.title = title
        self.descrition = descrition