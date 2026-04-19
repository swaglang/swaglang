import argparse
from antlr4 import FileStream, CommonTokenStream
from compiler.ast.printer import print_ast
from compiler.lexer.SwagLangLexer import SwagLangLexer
from compiler.lexer.SwagLangParser import SwagLangParser
from compiler.ast.builder import ASTBuilder
from compiler.errors.listener import SwagErrorListener
from compiler.llvm.llvm import LLVMCompiler
from compiler.semantic.analyzer import SemanticAnalyzer
from compiler.semantic.transformer import ASTTransformer


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

    if error_listener.errors:
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

    symbols, types, sem_errors = SemanticAnalyzer(args.file).analyze(ast)
    for e in sem_errors:
        print(e)

    ASTTransformer(types, symbols).transform(ast)

    # print_ast(ast, types)

    llvm_compiler = LLVMCompiler(ast, types, symbols)
    llvm_ir = llvm_compiler.compile()
    print(llvm_ir)



if __name__ == "__main__":
    main()
