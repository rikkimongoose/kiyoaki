class BaseParser:
    def __init__(self, root, command, parser_type):
        self.root = root
        self.regExRoot = re.compile("(\\s*)%s" % root, re.IGNORECASE)
        self.command = command
        self.type = parser_type