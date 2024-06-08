from grammar import Grammar
from lalr1_parser import LALR1Parser

def main():
    productions = [
        ("E", ["E", "+", "T"]),
        ("E", ["T"]),
        ("T", ["T", "*", "F"]),
        ("T", ["F"]),
        ("F", ["(", "E", ")"]),
        ("F", ["id"])
    ]
    grammar = Grammar(productions)
    parser = LALR1Parser(grammar)
    tokens = ["id", "+", "id", "*", "id"]
    parser.parse(tokens)

if __name__ == "__main__":
    main()
