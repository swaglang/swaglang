import argparse
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

from antlr4 import FileStream, CommonTokenStream
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


def _write_or_print(content: str, dest):
    """dest=True → stdout, dest=str → write to file."""
    if dest is True:
        print(content)
    else:
        Path(dest).write_text(content, encoding="utf-8")
        print(f"written to {dest}")


def _compile_to_exe(llvm_ir: str, exe_path: str):
    """Write IR to a temp .ll file, invoke clang, produce exe_path."""
    fd, ll_path = tempfile.mkstemp(suffix=".ll")
    try:
        os.write(fd, llvm_ir.encode("utf-8"))
        os.close(fd)
        result = subprocess.run(
            ["clang", "-O0", ll_path, "-o", exe_path],
            capture_output=True,
            text=True,
        )
        if result.returncode != 0:
            # strip triple-override warning
            stderr = "\n".join(
                l
                for l in result.stderr.splitlines()
                if "override-module" not in l and l.strip()
            )
            if stderr:
                print(stderr, file=sys.stderr)
            return False
        return True
    finally:
        os.unlink(ll_path)


def main():
    ap = argparse.ArgumentParser(
        prog="swag",
        description="SwagLang compiler",
    )
    ap.add_argument("file", help=".swag source file")
    ap.add_argument(
        "--tree",
        nargs="?",
        const=True,
        metavar="FILE",
        help="print AST to stdout, or write to FILE",
    )
    ap.add_argument(
        "--llvm",
        nargs="?",
        const=True,
        metavar="FILE",
        help="print LLVM IR to stdout, or write to FILE",
    )
    ap.add_argument(
        "--out",
        nargs="?",
        const=True,
        metavar="FILE",
        help="compile to executable; FILE defaults to input name without extension",
    )
    ap.add_argument(
        "--run",
        action="store_true",
        help="compile to a temp executable, run it, then delete it",
    )
    args = ap.parse_args()

    tree = parse(args.file)
    if tree is None:
        sys.exit(1)

    ast = ASTBuilder().visit(tree)

    if args.tree is not None:
        from compiler.ast.printer import print_ast  # lazy import

        _write_or_print(print_ast(ast), args.tree)

    symbols, types, sem_errors = SemanticAnalyzer(args.file).analyze(ast)
    for e in sem_errors:
        print(e, file=sys.stderr)
    if sem_errors:
        sys.exit(1)

    ASTTransformer(types, symbols).transform(ast)

    llvm_ir = LLVMCompiler(ast, types, symbols).compile()

    if args.llvm is not None:
        _write_or_print(llvm_ir, args.llvm)

    if args.out is not None:
        exe = str(Path(args.file).with_suffix(".exe")) if args.out is True else args.out
        if not _compile_to_exe(llvm_ir, exe):
            sys.exit(1)
        print(f"compiled: {exe}")

    if args.run:
        tmpdir = tempfile.mkdtemp()
        try:
            exe = os.path.join(tmpdir, "out.exe")
            if not _compile_to_exe(llvm_ir, exe):
                sys.exit(1)
            result = subprocess.run([exe])
            sys.exit(result.returncode)
        finally:
            shutil.rmtree(tmpdir, ignore_errors=True)

    if args.tree is None and args.llvm is None and args.out is None and not args.run:
        print(llvm_ir)


if __name__ == "__main__":
    main()
