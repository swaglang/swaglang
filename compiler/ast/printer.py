from compiler.ast.nodes import (
    ASTNode, Prog, CodeBlock, FuncDecl,
    SingleReturnType, MultiReturnType, VoidReturnType, ParamDecl,
    IntLiteral, FloatLiteral, StringLiteral, BoolLiteral,
    ListLiteral, DictLiteral, NoAcsModeVarDecl,
    IndexAccessor, FieldAccessor, VarRef,
    VarDecl, MultiVarDecl, VarAssign, MultiVarAssign,
    FuncCall, BinaryExpr, UnaryExpr, PostfixExpr, TernaryExpr,
    WhileLoop, DoWhileLoop, ForLoop, ForInLoop,
    IfElse, Break, Return, Defer,
)

def print_ast(node: ASTNode, indent: int = 0) -> None:
    p = " " * indent

    match node:
        case Prog(stmts=stmts):
            print(f"{p}Prog")
            for s in stmts:
                print_ast(s, indent + 1)

        case CodeBlock(func_stmts=stmts):
            print(f"{p}CodeBlock")
            for s in stmts:
                print_ast(s, indent + 1)

        case FuncDecl(return_type=rt, name=name, params=params, body=body):
            match rt:
                case VoidReturnType():
                    rt_str = "void"
                case SingleReturnType(type_ann=t):
                    rt_str = t.value if t else "void"
                case MultiReturnType(err=e, value_type=t):
                    rt_str = f"({e}, {t.value})"
            print(f"{p}FuncDecl: {name} -> {rt_str}")
            for param in params:
                print_ast(param, indent + 1)
            print_ast(body, indent + 1)

        case ParamDecl(name=name, type_ann=t):
            print(f"{p}ParamDecl: {name}: {t.value}")

        case VarDecl(access_mod=mod, name=name, type_ann=t, val=val):
            t_str = f"{t.value}" if t else "inferred"
            print(f"{p}VarDecl: {mod.value} {name}: {t_str}")
            print_ast(val, indent + 1)

        case MultiVarDecl(access_mod=mod, names=names, val=val):
            print(f"{p}MultiVarDecl: {mod.value} {', '.join(names)}")
            print_ast(val, indent + 1)

        case NoAcsModeVarDecl(name=name, type_ann=t, val=val):
            t_str = f"{t.value}" if t else "inferred"
            print(f"{p}Field: {name}: {t_str}")
            print_ast(val, indent + 1)

        case VarAssign(var=var, op=op, val=val):
            print(f"{p}VarAssign: {op.value}")
            print_ast(var, indent + 1)
            print_ast(val, indent + 1)

        case MultiVarAssign(vars=vars, val=val):
            print(f"{p}MultiVarAssign")
            for v in vars:
                print_ast(v, indent + 1)
            print_ast(val, indent + 1)

        case IfElse(condition=cond, if_body=if_body, elif_clauses=elifs, else_body=eb):
            print(f"{p}IfElse")
            print(f"{p} Condition:")
            print_ast(cond, indent + 2)
            print(f"{p} If Body:")
            print_ast(if_body, indent + 2)
            for clause  in elifs:
                print(f"{p} Elif Clause:")
                print_ast(clause.condition, indent + 2)
                print_ast(clause.body, indent + 2)
            if eb:
                print(f"{p} Else Body:")
                print_ast(eb, indent + 2)

        case WhileLoop(condition=cond, body=body):
            print(f"{p}WhileLoop")
            print(f"{p} Condition:")
            print_ast(cond, indent + 2)
            print_ast(body, indent + 1)

        case DoWhileLoop(body=body, condition=cond):
            print(f"{p}DoWhileLoop")
            print_ast(body, indent + 1)
            print(f"{p} Condition:")
            print_ast(cond, indent + 2)

        case ForLoop(init=init, condition=cond, update=update, body=body):
            print(f"{p}ForLoop")
            if init:
                print(f"{p} Init:")
                print_ast(init, indent + 2)
            if cond:
                print(f"{p} Condition:")
                print_ast(cond, indent + 2)
            if update:
                print(f"{p} Update:")
                print_ast(update, indent + 2)
            print_ast(body, indent + 1)

        case ForInLoop(var=var, iterable=iterable, body=body):
            print(f"{p}ForInLoop: {var} in")
            print_ast(iterable, indent + 1)
            print_ast(body, indent + 1)

        case Break():
            print(f"{p}Break")

        case Return(error=e, val=v):
            print(f"{p}Return")
            if e:
                print(f"{p} Error:")
                print_ast(e, indent + 2)
            if v:
                print_ast(v, indent + 1)

        case Defer(expr=e):
            print(f"{p}Defer")
            print_ast(e, indent + 1)

        case BinaryExpr(left=l, op=op, right=r):
            print(f"{p}BinaryExpr: {op.value}")
            print_ast(l, indent + 1)
            print_ast(r, indent + 1)

        case UnaryExpr(op=op, operand=operand):
            print(f"{p}UnaryExpr: {op.value}")
            print_ast(operand, indent + 1)

        case PostfixExpr(operand=operand, op=op):
            print(f"{p}PostfixExpr: {op.value}")
            print_ast(operand, indent + 1)

        case TernaryExpr(condition=cond, true_expr=true, false_expr=false):
            print(f"{p}TernaryExpr")
            print(f"{p} Condition:")
            print_ast(cond, indent + 2)
            print(f"{p} True Expr:")
            print_ast(true, indent + 2)
            print(f"{p} False Expr:")
            print_ast(false, indent + 2)

        case FuncCall(func=func, args=args):
            print(f"{p}FuncCall: {func}")
            for a in args:
                print_ast(a, indent + 1)

        case VarRef(name=name, accessors=accessors):
            acc_str = ""
            for a in accessors:
                match a:
                    case IndexAccessor(index=i):
                        acc_str += f"[{i.val if i else ''}]"
                    case FieldAccessor(field=f):
                        acc_str += f".{f.name}"
            print(f"{p}VarRef: {name}{acc_str}")

        case ListLiteral(elements=elements):
            print(f"{p}ListLiteral")
            for e in elements:
                print_ast(e, indent + 1)

        case DictLiteral(fields=fields):
            print(f"{p}DictLiteral")
            for f in fields:
                print_ast(f, indent + 1)

        case IntLiteral(val=val):
            print(f"{p}IntLiteral: {val}")

        case FloatLiteral(val=val):
            print(f"{p}FloatLiteral: {val}")

        case StringLiteral(val=val):
            print(f"{p}StringLiteral: {val}")

        case BoolLiteral(val=val):
            print(f"{p}BoolLiteral: {'true' if val else 'false'}")

        case _:
            print(f"{p}~~~unknown: {type(node).__name__}~~~")
