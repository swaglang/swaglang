import argparse
from antlr4 import FileStream, CommonTokenStream
from compiler.ast.printer import print_ast
from compiler.lexer.SwagLangLexer import SwagLangLexer
from compiler.lexer.SwagLangParser import SwagLangParser

from compiler.ast.builder import ASTBuilder

def parse(source: str):
    stream = FileStream(source)

    lexer = SwagLangLexer(stream)
    # TODO syntax error handler
    # lexer.removeErrorListeners()

    tokens = CommonTokenStream(lexer)
    parser = SwagLangParser(tokens)

    tree = parser.prog()
    return tree

def main():
    ap = argparse.ArgumentParser(description="Parses a SwagLang file and prints the resulting AST.")
    ap.add_argument("file", help=".swag source file")
    args = ap.parse_args()

    tree = parse(args.file)
    ast = ASTBuilder().visit(tree)

    print_ast(ast)

if __name__ == "__main__":
    main()
