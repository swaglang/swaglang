from dataclasses import dataclass
from compiler.ast.nodes import (
    ASTNode, Prog, CodeBlock, FuncDecl, SetLiteral,
    SingleReturnType, MultiReturnType, VoidReturnType, ParamDecl,
    ArrayType, BaseType, UserType,
    InterfaceDecl, InterfaceField,
    IntLiteral, FloatLiteral, StringLiteral, BoolLiteral,
    ArrayLiteral, MapField, MapLiteral, StructLiteral, NoAcsModeVarDecl, StructField,
    IndexAccessor, FieldAccessor, VarRef,
    VarDecl, MultiVarDecl, VarAssign, MultiVarAssign,
    FuncCall, BinaryExpr, UnaryExpr, PostfixExpr, TernaryExpr,
    WhileLoop, DoWhileLoop, ForLoop, ForInLoop,
    IfElse, Break, Return, Defer, MapType, SetType,
)

@dataclass
class _Label(ASTNode):
    label: str
    child: ASTNode

def print_ast(node: ASTNode) -> None:
    _print(node, prefix="", is_last=True)

def _print(node: ASTNode, prefix: str, is_last: bool) -> None:
    connector = "└ " if is_last else "├ "
    print(prefix + connector + _label(node))
    children = _children(node)
    new_prefix = prefix + ("  " if is_last else "│ ")
    for i, child in enumerate(children):
        _print(child, new_prefix, i == len(children) - 1)

def _format_type(t) -> str:
    match t:
        case BaseType():
            return t.value
        case UserType(name=name):
            return name
        case ArrayType(element=element):
            return f"{_format_type(element)}[]"
        case MapType(key=k, value=v):
            return f"map<{_format_type(k)}, {_format_type(v)}>"
        case SetType(element=e):
            return f"set<{_format_type(e)}>"

        case _:
            return "?"

def _label(node: ASTNode) -> str:
    match node:
        case Prog():
            return "Prog"
        case CodeBlock():
            return "CodeBlock"
        case FuncDecl(name=name, return_type=rt):
            match rt:
                case VoidReturnType():
                    rt_str = "void"
                case SingleReturnType(type_ann=t):
                    rt_str = _format_type(t) if t else "void"
                case MultiReturnType(types=ts):
                    rt_str = f"({', '.join(_format_type(t) for t in ts)})"
            return f"FuncDecl: {name} -> {rt_str}"
        case ParamDecl(name=name, type_ann=t):
            return f"ParamDecl: {name}: {_format_type(t)}"
        case InterfaceDecl(name=name, extends=extends):
            ext_str = f" extends {', '.join(extends)}" if extends else ""
            return f"InterfaceDecl: {name}{ext_str}"
        case InterfaceField(name=name, type_ann=t, optional=opt):
            q = "?" if opt else ""
            return f"InterfaceField: {name}{q}: {_format_type(t)}"
        case VarDecl(access_mod=mod, name=name, type_ann=t, val=val):
            t_str = _format_type(t) if t else "inferred"
            return f"VarDecl: {mod.value} {name}: {t_str}"
        case MultiVarDecl(access_mod=mod, names=names, val=val):
            return f"MultiVarDecl: {mod.value} {', '.join(names)}"
        case NoAcsModeVarDecl(name=name, type_ann=t, val=val):
            t_str = _format_type(t) if t else "inferred"
            return f"Field: {name}: {t_str}"
        case StructField(name=name):
            return f"Field: {name}"
        case VarAssign(op=op):
            return f"VarAssign: {op.value}"
        case MultiVarAssign():
            return "MultiVarAssign"
        case IfElse():
            return "IfElse"
        case WhileLoop():
            return "WhileLoop"
        case DoWhileLoop():
            return "DoWhileLoop"
        case ForLoop():
            return "ForLoop"
        case ForInLoop(var=var):
            return f"ForInLoop: {var} in"
        case Break():
            return "Break"
        case Return():
            return "Return"
        case Defer():
            return "Defer"
        case BinaryExpr(op=op):
            return f"BinaryExpr: {op.value}"
        case UnaryExpr(op=op):
            return f"UnaryExpr: {op.value}"
        case PostfixExpr(op=op):
            return f"PostfixExpr: {op.value}"
        case TernaryExpr():
            return "TernaryExpr"
        case FuncCall(func=func):
            return f"FuncCall: {func}"
        case VarRef(name=name, accessors=accessors):
            acc_str = ""
            for a in accessors:
                match a:
                    case IndexAccessor(index=i):
                        match i:
                            case IntLiteral(val=v):
                                acc_str += f"[{v}]"
                            case StringLiteral(val=v):
                                acc_str += f'["{v}"]'
                            case None:
                                acc_str += "[]"
                            case _:
                                acc_str += "[...]"
                    case FieldAccessor(field=f):
                        acc_str += f".{f.name}"
            return f"VarRef: {name}{acc_str}"
        case ArrayLiteral():
            return "ArrayLiteral"
        case MapLiteral():
            return "MapLiteral"
        case MapField():
            return "MapField"
        case SetLiteral():
            return "SetLiteral"
        case StructLiteral():
            return "StructLiteral"
        case IntLiteral(val=val):
            return f"IntLiteral: {val}"
        case FloatLiteral(val=val):
            return f"FloatLiteral: {val}"
        case StringLiteral(val=val):
            return f"StringLiteral: {val}"
        case BoolLiteral(val=val):
            return f"BoolLiteral: {'true' if val else 'false'}"
        case _Label(label=label):
            return label
        case _:
            return f"~~~unknown: {type(node).__name__}~~~"

def _children(node: ASTNode) -> list[ASTNode]:
    match node:
        case Prog(stmts=stmts):
            return stmts
        case CodeBlock(func_stmts=stmts):
            return stmts
        case FuncDecl(params=params, body=body):
            return params + [body]
        case ParamDecl():
            return []
        case InterfaceDecl(fields=fields):
            return fields
        case InterfaceField():
            return []
        case VarDecl(val=val):
            return [val]
        case MultiVarDecl(val=val):
            return [val]
        case NoAcsModeVarDecl(val=val):
            return [val]
        case StructField(val=val):
            return [val]
        case VarAssign(var=var, val=val):
            return [var, val]
        case MultiVarAssign(vars=vars, val=val):
            return vars + [val]
        case IfElse(condition=cond, if_body=if_body, elif_clauses=elifs, else_body=eb):
            children = [
                _Label("Condition", cond),
                _Label("If Body", if_body),
            ]
            for clause in elifs:
                children += [
                    _Label("Elif Condition", clause.condition),
                    _Label("Elif Body", clause.body),
                ]
            if eb:
                children.append(_Label("Else Body", eb))
            return children
        case WhileLoop(condition=cond, body=body):
            return [_Label("Condition", cond), _Label("Body", body)]
        case DoWhileLoop(body=body, condition=cond):
            return [_Label("Body", body), _Label("Condition", cond)]
        case ForLoop(init=init, condition=cond, update=update, body=body):
            children = []
            if init:
                children.append(_Label("Init", init))
            if cond:
                children.append(_Label("Condition", cond))
            if update:
                children.append(_Label("Update", update))
            children.append(_Label("Body", body))
            return children
        case ForInLoop(iterable=iterable, body=body):
            return [iterable, body]
        case Break():
            return []
        case Return(vals=vs):
            return [_Label(f"Value {i}", v) for i, v in enumerate(vs)]
        case Defer(expr=e):
            return [e]
        case BinaryExpr(left=l, right=r):
            return [l, r]
        case UnaryExpr(operand=operand):
            return [operand]
        case PostfixExpr(operand=operand):
            return [operand]
        case TernaryExpr(condition=cond, true_expr=true, false_expr=false):
            return [
                _Label("Condition", cond),
                _Label("True", true),
                _Label("False", false),
            ]
        case FuncCall(args=args):
            return args
        case VarRef():
            return []
        case ArrayLiteral(elements=elements):
            return elements
        case MapLiteral(fields=fields):
            return fields
        case MapField(key=key, val=val):
            return [_Label("Key", key), _Label("Val", val)]
        case SetLiteral(elements=elements):
            return elements
        case StructLiteral(fields=fields):
            return fields
        case IntLiteral():
            return []
        case FloatLiteral():
            return []
        case StringLiteral():
            return []
        case BoolLiteral():
            return []
        case _Label(child=child):
            return [child]
        case _:
            return []
