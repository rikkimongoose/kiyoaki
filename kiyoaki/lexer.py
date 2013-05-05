class Lexer:
    """ Lexer parser for the Kyoaki language
    """
    def __init__(self, parser_context):
        self.parser_context = parser_context

    def _get_line(self):
        """ Get line from the source_loader, ignoring comments
        """
        new_line = self.source_loader.get_line()
        is_line_empty = True
        while is_line_empty:
            if source_loader.is_end():
                return None
            new_line = self.source_loader.get_line()
            is_line_empty = not new_line or self.parser_context.is_comment(new_line)
        return new_line

    def get_lexems(self, source_loader):
        """ Get lexems from a source loader and return the list of strings ready to be parsed.
        """
        self.source_loader = source_loader
        lexems = []
        line_to_parse = self._get_line()
        while line_to_parse is not None:
            while not self.parser_context.is_finished(line_to_parse):
                new_line_to_parse = self._get_line()
                if new_line_to_parse is None:
                    self.parser_context.add_notification("Lexer Error", "Unable to parse final line: %s" % line_to_parse)
                    return None
                line_to_parse = line_to_parse + new_line_to_parse
            lexems.add(line_to_parse)
            line_to_parse = self._get_line()
        return lexems