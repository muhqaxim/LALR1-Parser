class LR0Item:
    def __init__(self, production, dot_position=0, lookahead="$"):
        self.production = production
        self.dot_position = dot_position
        self.lookahead = lookahead

    def __repr__(self):
        head, body = self.production
        return f"{head} -> {' '.join(body[:self.dot_position] + ['.'] + body[self.dot_position:])}, {self.lookahead}"

class LR0Automaton:
    def __init__(self, grammar):
        self.grammar = grammar
        self.states = []
        self._construct_automaton()

    def _closure(self, items):
        closure_set = set(items)
        while True:
            new_items = set()
            for item in closure_set:
                head, body = item.production
                if item.dot_position < len(body):
                    symbol = body[item.dot_position]
                    if symbol in self.grammar.non_terminals:
                        for prod in self.grammar.productions:
                            if prod[0] == symbol:
                                new_items.add(LR0Item(prod))
            if new_items.issubset(closure_set):
                break
            closure_set.update(new_items)
        return closure_set

    def _goto(self, items, symbol):
        goto_set = set()
        for item in items:
            head, body = item.production
            if item.dot_position < len(body) and body[item.dot_position] == symbol:
                goto_set.add(LR0Item(item.production, item.dot_position + 1))
        return self._closure(goto_set)

    def _construct_automaton(self):
        initial_item = LR0Item(self.grammar.productions[0], 0)
        initial_state = self._closure({initial_item})
        self.states.append(initial_state)
        unmarked_states = [initial_state]
        while unmarked_states:
            current_state = unmarked_states.pop()
            for symbol in self.grammar.non_terminals.union(self.grammar.terminals):
                new_state = self._goto(current_state, symbol)
                if new_state and new_state not in self.states:
                    self.states.append(new_state)
                    unmarked_states.append(new_state)
