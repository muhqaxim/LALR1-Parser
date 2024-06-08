import unittest
from src.grammar import Grammar

class TestGrammar(unittest.TestCase):
    def test_grammar_initialization(self):
        productions = [
            ("E", ["E", "+", "T"]),
            ("E", ["T"]),
            ("T", ["T", "*", "F"]),
            ("T", ["F"]),
            ("F", ["(", "E", ")"]),
            ("F", ["id"])
        ]
        grammar = Grammar(productions)
        self.assertEqual(grammar.start_symbol, "E")
        self.assertIn("E", grammar.non_terminals)
        self.assertIn("id", grammar.terminals)

if __name__ == "__main__":
    unittest.main()
