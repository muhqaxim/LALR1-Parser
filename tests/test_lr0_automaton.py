import unittest
from src.grammar import Grammar
from src.lr0_automaton import LR0Item, LR0Automaton

class TestLR0Automaton(unittest.TestCase):
    def setUp(self):
        productions = [
            ("E", ["E", "+", "T"]),
            ("E", ["T"]),
            ("T", ["T", "*", "F"]),
            ("T", ["F"]),
            ("F", ["(", "E", ")"]),
            ("F", ["id"])
        ]
        self.grammar = Grammar(productions)
        self.automaton = LR0Automaton(self.grammar)

    def test_closure(self):
        item = LR0Item(self.grammar.productions[0])
        closure = self.automaton._closure({item})
        self.assertIn(item, closure)

    def test_goto(self):
        item = LR0Item(self.grammar.productions[0])
        closure = self.automaton._closure({item})
        goto_result = self.automaton._goto(closure, 'E')
        self.assertIsNotNone(goto_result)

if __name__ == "__main__":
    unittest.main()
