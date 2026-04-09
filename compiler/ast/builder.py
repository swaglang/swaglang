from compiler.lexer.SwagLangParser import SwagLangParser
from compiler.lexer.SwagLangParserVisitor import SwagLangParserVisitor
from compiler.ast.nodes import (
    AccessMod, ArrayLiteral, ArrayType, AssignOp, BaseType, BinaryExpr,
    BinaryOp, BoolLiteral, Break, CodeBlock, Continue, Data, Defer,
    DoWhileLoop, ElifClause, Expr, FieldAccessor, FloatLiteral,
    ForInLoop, ForLoop, FuncCall, FuncDecl, IfElse, IndexAccessor,
    IntLiteral, InterfaceDecl, InterfaceField, MapField, MapLiteral,
    MapType, MultiReturnType, MultiVarAssign, MultiVarDecl,
    NoAcsModeVarDecl, NullLiteral, ParamDecl, PostfixExpr, PostfixOp,
    Prog, Return, ReturnType, SetLiteral, SetType, SingleReturnType,
    StringLiteral, StructField, StructLiteral, TernaryExpr, Type,
    UnaryExpr, UnaryOp, UserType, VarAssign, VarDecl, VarRef,
    VoidReturnType, WhileLoop,
)

class ASTBuilder(SwagLangParserVisitor):
    def visitProg(self, ctx) -> Prog:
        stmts_ctx = ctx.stmts()
        stmts = [
            self.visit(s) for s in stmts_ctx.stmt()
            if not self._is_nwln(s)
        ]
        return Prog(stmts=[s for s in stmts if s is not None])

    def visitStmt(self, ctx) -> None:
        return self.visit(ctx.pure_stmt())

    def visitPure_stmt(self, ctx) -> None:
        return self.visitChildren(ctx)

    def visitFunc_stmt(self, ctx) -> None:
        if ctx.pure_func_stmt():
            return self.visit(ctx.pure_func_stmt())
        return None

    def visitPure_func_stmt(self, ctx) -> None:
        return self.visitChildren(ctx)

    def visitCode_block(self, ctx):
        stmts = [self.visit(s) for s in ctx.func_stmt()]
        return CodeBlock(func_stmts=[s for s in stmts if s is not None])

    def visitFunc_decl(self, ctx) -> FuncDecl:
        return FuncDecl(
            return_type=self.visit(ctx.return_type()),
            name=ctx.IDENT().getText(),
            params=[self.visit(p) for p in ctx.param_decl()],
            body=self.visit(ctx.code_block())
        )

    def visitReturn_type(self, ctx) -> ReturnType:
        if ctx.VOID():
            return VoidReturnType()
        if ctx.L_PAREN():
            return MultiReturnType(
                types=[self.visit(t) for t in ctx.type_ann()]
            )
        return SingleReturnType(type_ann=self.visit(ctx.type_ann(0)))

    def visitType_ann(self, ctx) -> Type:
        if ctx.TYPE():
            base: Type = BaseType(ctx.TYPE().getText())
        elif ctx.map_type():
            base = self.visit(ctx.map_type())
        elif ctx.set_type():
            base = self.visit(ctx.set_type())
        else:
            base = UserType(name=ctx.IDENT().getText())

        depth = len(ctx.L_BRACKET())
        for _ in range(depth):
            base = ArrayType(element=base)
        return base

    def visitMap_type(self, ctx) -> MapType:
        return MapType(
            key=self.visit(ctx.type_ann(0)),
            value=self.visit(ctx.type_ann(1))
        )

    def visitSet_type(self, ctx) -> SetType:
        return SetType(element=self.visit(ctx.type_ann()))

    def visitInterface_decl(self, ctx) -> InterfaceDecl:
        idents = ctx.IDENT()
        name = idents[0].getText()
        parents: list[str] = []
        if ctx.EXTENDS():
            parents = [i.getText() for i in idents[1:]]
        fields = [self.visit(f) for f in ctx.interface_field()]
        return InterfaceDecl(name=name, extends=parents, fields=fields)

    def visitInterface_field(self, ctx) -> InterfaceField:
        return InterfaceField(
            name=ctx.IDENT().getText(),
            type_ann=self.visit(ctx.type_ann()),
            optional=ctx.QUESTION() is not None,
        )

    def visitParam_decl(self, ctx) -> ParamDecl:
        return ParamDecl(
            name=ctx.IDENT().getText(),
            type_ann=self.visit(ctx.type_ann())
        )

    def visitVar_decl(self, ctx) -> VarDecl | MultiVarDecl:
        mod = AccessMod(ctx.ACCESS_MOD().getText())
        idents = ctx.IDENT()
        if len(idents) >= 2:
            return MultiVarDecl(
                access_mod=mod,
                names=[i.getText() for i in idents],
                val=self.visit(ctx.func_call()),
            )

        return VarDecl(
            access_mod=mod,
            name=idents[0].getText(),
            type_ann=self.visit(ctx.type_ann()) if ctx.type_ann() else None,
            val=self.visit(ctx.expr())
        )

    def visitNo_acs_mode_var_decl(self, ctx) -> NoAcsModeVarDecl:
        return NoAcsModeVarDecl(
            name=ctx.IDENT().getText(),
            type_ann=self.visit(ctx.type_ann()) if ctx.type_ann() else None,
            val=self.visit(ctx.expr())
        )

    def visitVar_assign(self, ctx) -> VarAssign | MultiVarAssign:
        var_refs = ctx.var_ref()

        if len(var_refs) >= 2:
            return MultiVarAssign(
                vars=[self.visit(v) for v in var_refs],
                val=self.visit(ctx.func_call())
            )

        op_text = None
        for tok in [ctx.ASSIGN(), ctx.ADD_ASSIGN(), ctx.SUB_ASSIGN(), ctx.MUL_ASSIGN(), ctx.DIV_ASSIGN(), ctx.MOD_ASSIGN()]:
            if tok:
                op_text = tok.getText()
                break

        return VarAssign(
            var=self.visit(var_refs[0]),
            op=AssignOp(op_text),
            val=self.visit(ctx.expr())
        )

    def visitVar_ref(self, ctx) -> VarRef:
        name = ctx.IDENT().getText()
        accessors = []
        i = 1
        while i < len(ctx.children):
            child = ctx.children[i]
            if child.getText() == "[":
                expr_node = ctx.children[i + 1]
                accessors.append(IndexAccessor(
                    var=name,
                    index=self.visit(expr_node)
                ))
                i += 3
            elif child.getText() == ".":
                field_node = ctx.children[i + 1]
                accessors.append(FieldAccessor(
                    var=name,
                    field=self.visit(field_node)
                ))
                i += 2

            else:
                i += 1

        return VarRef(name=name, accessors=accessors)

    def visitData(self, ctx) -> Data:
        if ctx.INT():
            return IntLiteral(val=int(ctx.INT().getText()))
        if ctx.STRING():
            return StringLiteral(val=ctx.STRING().getText()[1:-1])
        if ctx.FLOAT():
            return FloatLiteral(val=float(ctx.FLOAT().getText()))
        if ctx.BOOL():
            return BoolLiteral(val=ctx.BOOL().getText() == "true")
        if ctx.NULL():
            return NullLiteral()
        if ctx.array():
            return self.visit(ctx.array())
        if ctx.map_():
            return self.visit(ctx.map_())
        if ctx.set_():
            return self.visit(ctx.set_())
        if ctx.struct():
            return self.visit(ctx.struct())

    def visitArray(self, ctx) -> ArrayLiteral:
        return ArrayLiteral(elements=[self.visit(e) for e in ctx.expr()])

    def visitMap(self, ctx) -> MapLiteral:
        return MapLiteral(fields=[self.visit(f) for f in ctx.map_field()])

    def visitMap_field(self, ctx) -> MapField:
        return MapField(
            key=self.visit(ctx.expr(0)),
            val=self.visit(ctx.expr(1))
        )

    def visitSet(self, ctx) -> SetLiteral:
        return SetLiteral(elements=[self.visit(e) for e in ctx.expr()])

    def visitStruct(self, ctx) -> StructLiteral:
        return StructLiteral(fields=[self.visit(f) for f in ctx.struct_field()])

    def visitStruct_field(self, ctx) -> StructField:
        return StructField(
            name=ctx.IDENT().getText(),
            val=self.visit(ctx.expr())
        )

    def visitExpr(self, ctx) -> Expr:
        n = ctx.getChildCount()

        # parentheses
        if n == 3 and ctx.getChild(0).getText() == "(":
            return self.visit(ctx.expr(0))

        if ctx.data():
            return self.visit(ctx.data())

        if ctx.func_call():
            return self.visit(ctx.func_call())

        # var ref
        if ctx.var_ref() and n == 1:
            return self.visit(ctx.var_ref())

        # ++ / --
        if ctx.var_ref() and n == 2:
            return PostfixExpr(
                operand=self.visit(ctx.var_ref()),
                op=PostfixOp(ctx.getChild(1).getText())
            )

        # unary: !
        if n == 2:
            return UnaryExpr(
                op=UnaryOp(ctx.getChild(0).getText()),
                operand=self.visit(ctx.expr(0))
            )

        # ternary: expr ? expr : expr
        if n == 5 and ctx.getChild(1).getText() == "?":
            return TernaryExpr(
                condition=self.visit(ctx.expr(0)),
                true_expr=self.visit(ctx.expr(1)),
                false_expr=self.visit(ctx.expr(2))
            )

        # binary
        if n == 3 and ctx.expr(0) and ctx.expr(1):
            return BinaryExpr(
                left=self.visit(ctx.expr(0)),
                op=BinaryOp(ctx.getChild(1).getText()),
                right=self.visit(ctx.expr(1))
            )

        return self.visitChildren(ctx)

    def visitFunc_call(self, ctx) -> FuncCall:
        return FuncCall(
            func=ctx.IDENT().getText(),
            args=[self.visit(e) for e in ctx.params().expr()] if ctx.params() else [],
        )

    def visitCondition(self, ctx) -> None:
        return self.visit(ctx.expr())

    def visitConditional(self, ctx) -> IfElse:
        conditions = ctx.condition()
        bodies = ctx.conditional_body()

        elif_clauses = [
            ElifClause(
                condition=self.visit(cond.expr()),
                body=self.visit(body.code_block())
            )
            for cond, body in zip(conditions[1:], bodies[1:])
        ]

        return IfElse(
            condition=self.visit(conditions[0].expr()),
            if_body=self.visit(bodies[0].code_block()),
            elif_clauses=elif_clauses,
            else_body=self.visit(bodies[-1].code_block()) if ctx.ELSE() else None
        )

    def visitWhile_loop(self, ctx):
        return WhileLoop(
            condition=self.visit(ctx.condition().expr()),
            body=self.visit(ctx.loop_body().code_block())
        )

    def visitDo_while_loop(self, ctx) -> WhileLoop:
        return DoWhileLoop(
            body=self.visit(ctx.loop_body().code_block()),
            condition=self.visit(ctx.condition().expr())
        )

    def visitFor_loop(self, ctx) -> ForLoop | ForInLoop:
        if ctx.forin():
            forin = ctx.forin()
            return ForInLoop(
                var=forin.IDENT().getText(),
                iterable=self.visit(forin.func_call()) if forin.func_call() else self.visit(forin.var_ref()),
                body=self.visit(ctx.loop_body().code_block())
            )

        return ForLoop(
            init=self.visit(ctx.no_acs_mode_var_decl()) if ctx.no_acs_mode_var_decl() else None,
            condition=self.visit(ctx.condition().expr()) if ctx.condition() else None,
            update=self.visit(ctx.expr()) if ctx.expr() else None,
            body=self.visit(ctx.loop_body().code_block())
        )

    def visitBreak(self, _) -> Break:
        return Break()

    def visitContinue(self, _) -> Continue:
        return Continue()

    def visitReturn(self, ctx) -> Return:
        return Return(vals=[self.visit(e) for e in ctx.expr()])

    def visitDefer(self, ctx) -> Defer:
        return Defer(expr=self.visit(ctx.expr()))

    def _parse_scalar_literal(self, text: str) -> IntLiteral | StringLiteral:
        if text.startswith('"'):
            return StringLiteral(val=text[1:-1])
        return IntLiteral(val=int(text))

    def _is_nwln(self, ctx: SwagLangParser) -> bool:
        return hasattr(ctx, 'symbol')
