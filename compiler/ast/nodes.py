from __future__ import annotations
from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional

class AccessMod(Enum):
    """access modifier of a variable"""
    CONST = "const"
    """constant"""
    LET = "let"
    """mutable"""

class BaseType(Enum):
    INT = "int"
    """integer type"""
    FLOAT = "float"
    """floating point type"""
    STRING = "string"
    """string type"""
    BOOL = "bool"
    """boolean type"""

# TODO: arrays are bad, separate array declaration from types
class ArrayType(Enum):
    INT_ARRAY = "int[]"
    """array of integers"""
    FLOAT_ARRAY = "float[]"
    """array of floating point numbers"""
    STRING_ARRAY = "string[]"
    """array of strings"""
    BOOL_ARRAY = "bool[]"
    """array of booleans"""

class VoidType(Enum):
    VOID = "void"
    """no return fom function"""

Type = BaseType | ArrayType

class ASTNode:
    """base class for all AST nodes"""

class FuncStmt(ASTNode):
    """a statement inside a function body"""

class PureFuncStmt(FuncStmt):
    """base class for function statements"""

class Expr(PureFuncStmt):
    """base class for expressions"""

class Stmt(ASTNode):
    """base class for all statements"""

class PureStmt(Stmt):
    """base class for function and variable declaration"""

@dataclass
class Prog(ASTNode):
    """program node, root of the AST"""
    stmts: List[Stmt]

@dataclass
class CodeBlock(ASTNode):
    """code block, a list of statements"""
    func_stmts: List[FuncStmt]

@dataclass
class FuncDecl(PureStmt, PureFuncStmt):
    return_type: ReturnType
    name: str
    params: List[ParamDecl]
    body: CodeBlock

class ReturnType(ASTNode):
    """return type of a function"""

@dataclass
class SingleReturnType(ReturnType):
    """single return type"""
    type_ann: Optional[Type]

@dataclass
class MultiReturnType(ReturnType):
    """multiple return types"""
    err: str
    value_type: Type

@dataclass
class VoidReturnType(ReturnType):
    """void return type, no return value"""

@dataclass
class ParamDecl(ASTNode):
    """function parameters"""
    name: str
    type_ann: Type

class Data(Expr):
    """data literals"""

@dataclass
class IntLiteral(Data):
    """integer literal"""
    val: int

@dataclass
class FloatLiteral(Data):
    """floating point literal"""
    val: float

@dataclass
class StringLiteral(Data):
    """string literal"""
    val: str

@dataclass
class BoolLiteral(Data):
    """true / false"""
    val: bool

@dataclass
class ListLiteral(Data):
    """list literal"""
    elements: List[Data]

@dataclass
class DictLiteral(Data):
    """dictionary literal"""
    fields: List[NoAcsModeVarDecl]

@dataclass
class NoAcsModeVarDecl(ASTNode):
    """variable declaration without access modifier, used in dict literals"""
    name: str
    type_ann: Optional[Type]
    val: Expr

class Accessor(ASTNode):
    """base class for variable access"""

@dataclass
class IndexAccessor(Accessor):
    """accessing an element of an array"""
    var: str
    index: Optional[Expr]

@dataclass
class FieldAccessor(Accessor):
    """accessing a field of a dictionary"""
    var: str
    field: VarRef

@dataclass
class VarRef(Expr):
    """accessing a variable"""
    name: str
    accessors: List[Accessor] = field(default_factory=list)

@dataclass
class VarDecl(PureStmt, PureFuncStmt):
    """variable declaration statement"""
    access_mod: AccessMod
    name: str
    type_ann: Optional[Type]
    val: Expr

@dataclass
class FuncCall(Expr):
    """function call expression"""
    func: str
    args: List[Expr]

@dataclass
class MultiVarDecl(PureFuncStmt):
    access_mod: AccessMod
    names: List[str]
    val: FuncCall

class AssignOp(Enum):
    """assignment operators"""
    ASSIGN = "="
    """simple assignment"""
    ADD_ASSIGN = "+="
    """addition assignment"""
    SUB_ASSIGN = "-="
    """subtraction assignment"""
    MUL_ASSIGN = "*="
    """multiplication assignment"""
    DIV_ASSIGN = "/="
    """division assignment"""
    MOD_ASSIGN = "%="
    """modulo assignment"""

@dataclass
class VarAssign(PureFuncStmt):
    """variable assignment statement"""
    var: VarRef
    op: AssignOp
    val: Expr

@dataclass
class MultiVarAssign(PureFuncStmt):
    """multiple variable assignment statement"""
    vars: List[VarRef]
    val: FuncCall

class Loop(PureFuncStmt):
    """base class for loops"""
    pass

@dataclass
class WhileLoop(Loop):
    """while loop statement"""
    condition: Expr
    body: CodeBlock

@dataclass
class DoWhileLoop(Loop):
    """do-while loop statement"""
    body: CodeBlock
    condition: Expr

@dataclass
class ForLoop(Loop):
    """for loop statement"""
    init: Optional[NoAcsModeVarDecl]
    condition: Optional[Expr]
    update: Optional[Expr]
    body: CodeBlock

@dataclass
class ForInLoop(Loop):
    """for-in loop statement"""
    var: str
    iterable: FuncCall | VarRef
    body: CodeBlock

class Conditional(PureFuncStmt):
    """base class for if-else statements"""
    pass

@dataclass
class ElifClause(ASTNode):
    """elif clause in an if-else statement"""
    condition: Expr
    body: CodeBlock

@dataclass
class IfElse(Conditional):
    """if-else statement"""
    condition: Expr
    if_body: CodeBlock
    elif_clauses: List[ElifClause]
    else_body: Optional[CodeBlock]

@dataclass
class Break(PureFuncStmt):
    """break statement to exit loops"""

@dataclass
class Return(PureFuncStmt):
    val: Optional[Expr] = None
    error: Optional[Expr] = None

@dataclass
class Defer(PureFuncStmt):
    """defer statement to execute code at the end of the function"""
    expr: Expr

class BinaryOp(Enum):
    """binary operators"""
    ADD = "+"
    """addition"""
    SUB = "-"
    """subtraction"""
    MUL = "*"
    """multiplication"""
    DIV = "/"
    """division"""
    MOD = "%"
    """modulo"""
    EXP = "**"
    """exponentiation"""
    EQ = "=="
    """equality comparison"""
    NEQ = "!="
    """inequality comparison"""
    LT = "<"
    """less than comparison"""
    GT = ">"
    """greater than comparison"""
    LTE = "<="
    """less than or equal to comparison"""
    GTE = ">="
    """greater than or equal to comparison"""
    AND = "&&"
    """logical and"""
    OR = "||"
    """logical or"""

class UnaryOp(Enum):
    """unary operators"""
    NOT = "!"
    """logical not"""

class PostfixOp(Enum):
    """postfix operators"""
    INC = "++"
    """increment"""
    DEC = "--"
    """decrement"""

@dataclass
class BinaryExpr(Expr):
    """binary expression"""
    left: Expr
    op: BinaryOp
    right: Expr

@dataclass
class UnaryExpr(Expr):
    """unary expression"""
    op: UnaryOp
    operand: Expr

@dataclass
class PostfixExpr(Expr):
    """postfix expression"""
    operand: VarRef
    op: PostfixOp

@dataclass
class TernaryExpr(Expr):
    """ternary expression"""
    condition: Expr
    true_expr: Expr
    false_expr: Expr
