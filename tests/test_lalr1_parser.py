import unittest
from src.grammar import Grammar
from src.lalr1_parser import LALR1Parser

class TestLALR1Parser(unittest.TestCase):
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
        self.parser = LALR1Parser(self.grammar)

    def test_parse(self):
        tokens = ["id", "+", "id", "*", "id"]
        try:
            self.parser.parse(tokens)
            result = True
        except SyntaxError:
            result = False
        self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()
