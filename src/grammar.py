class Grammar:
    def __init__(self, productions):
        self.productions = productions
        self.non_terminals = set()
        self.terminals = set()
        self.start_symbol = None
        self._find_symbols()

    def _find_symbols(self):
        for head, body in self.productions:
            self.non_terminals.add(head)
            for symbol in body:
                if not symbol.isupper():
                    self.terminals.add(symbol)
        self.start_symbol = self.productions[0][0]
