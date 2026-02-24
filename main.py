import argparse
from antlr4 import FileStream, CommonTokenStream
from compiler.ast.printer import print_ast
from compiler.lexer.SwagLangLexer import SwagLangLexer
from compiler.lexer.SwagLangParser import SwagLangParser
from compiler.ast.builder import ASTBuilder
from compiler.errors.listener import SwagErrorListener


def parse(source: str):
    stream = FileStream(source, encoding="utf-8")

    lexer = SwagLangLexer(stream)
    error_listener = SwagErrorListener(source)

    lexer.removeErrorListeners()
    lexer.addErrorListener(error_listener)

    tokens = CommonTokenStream(lexer)
    parser = SwagLangParser(tokens)

    parser.removeErrorListeners()
    parser.addErrorListener(error_listener)

    tree = parser.prog()

    if error_listener.collected:
        return None

    return tree


def main():
    ap = argparse.ArgumentParser(description="Parses a SwagLang file and prints the resulting AST.")
    ap.add_argument("file", help=".swag source file")
    args = ap.parse_args()

    tree = parse(args.file)
    if tree is None:
        return
    ast = ASTBuilder().visit(tree)

    print_ast(ast)


if __name__ == "__main__":
    main()
