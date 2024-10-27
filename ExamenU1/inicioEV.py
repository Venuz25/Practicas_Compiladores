from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from EvalVisitor import EvalVisitor

def parse_tree_structure(tree_str):
    tree_str = tree_str.replace('(', ' ( ').replace(')', ' ) ')
    tokens = tree_str.split()
    
    def parse(tokens):
        token = tokens.pop(0)
        if token == '(':
            sub_tree = []
            while tokens[0] != ')':
                sub_tree.append(parse(tokens))
            tokens.pop(0)
            return sub_tree
        else:
            return token

    return parse(tokens)

def print_tree(tree, indent=0):
    if isinstance(tree, list):
        print(' ' * indent + str(tree[0]))
        for subtree in tree[1:]:
            print_tree(subtree, indent + 4) 
    else:
        print(' ' * indent + str(tree))

#main
input_stream = InputStream(input('? '))

lexer = ExprLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = ExprParser(token_stream)
tree = parser.root()

tree.toStringTree(recog=parser)
visitor = EvalVisitor()
visitor.visit(tree)

tree_str = tree.toStringTree(recog=parser)
parsed_tree = parse_tree_structure(tree_str)

print("\nArbol Sintactico:")
print_tree(parsed_tree)