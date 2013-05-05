from lexer import *

class ParserContext:
    """ A context for parser to be executed
    """
    def __init__(self, lexer, parser):
        self.parser = parser
        self.lexer = Lexer(self, parser)
        self.notifications = []

    def add_notification(self, title, descrition):
        """ Add the notification about an error during lexing or parsing.
        """
        self.notifications.add(ParserNotification(title, descrition))

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