from compiler.lexer.SwagLangParser import SwagLangParser
from compiler.lexer.SwagLangParserVisitor import SwagLangParserVisitor
from compiler.ast.nodes import (
    AccessMod, ArrayType, AssignOp, BaseType, BinaryExpr, BinaryOp, BoolLiteral,
    Break, CodeBlock, Data, Defer, DictLiteral, DoWhileLoop, ElifClause, Expr,
    FieldAccessor, FloatLiteral, ForInLoop, ForLoop, FuncCall, FuncDecl, IfElse,
    IndexAccessor, IntLiteral, ListLiteral, MultiReturnType, MultiVarAssign,
    MultiVarDecl, NoAcsModeVarDecl, ParamDecl, PostfixExpr, PostfixOp, Prog,
    Return, ReturnType, SingleReturnType, StringLiteral, TernaryExpr, Type,
    UnaryExpr, UnaryOp, VarAssign, VarDecl, VarRef, VoidReturnType, WhileLoop
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
        if ctx.L_PAREN():
            return MultiReturnType(
                err=ctx.IDENT().getText(),
                value_type=self._parse_type(ctx.TYPE().getText())
            )
        raw = ctx.TYPE().getText()
        if raw == "void":
            return VoidReturnType()
        return SingleReturnType(type_ann=self._parse_type(raw))


    def visitParam_decl(self, ctx) -> ParamDecl:
        return ParamDecl(
            name=ctx.IDENT().getText(),
            type_ann=self._parse_type(ctx.TYPE().getText())
        )

    def visitVar_decl(self, ctx) -> VarDecl | MultiVarDecl:
        mod = AccessMod(ctx.ACCESS_MOD().getText())
        idents = ctx.IDENT()
        if len(idents) == 2:
            return MultiVarDecl(
                access_mod=mod,
                names=[idents[0].getText(), idents[1].getText()],
                val=self.visit(ctx.func_call()),
            )

        return VarDecl(
            access_mod=mod,
            name=idents[0].getText(),
            type_ann=self._parse_type(ctx.TYPE().getText()) if ctx.TYPE() else None,
            val=self.visit(ctx.expr())
        )

    def visitNo_acs_mode_var_decl(self, ctx) -> NoAcsModeVarDecl:
        return NoAcsModeVarDecl(
            name=ctx.IDENT().getText(),
            type_ann=self._parse_type(ctx.TYPE().getText()) if ctx.TYPE() else None,
            val=self.visit(ctx.expr())
        )

    def visitVar_assign(self, ctx) -> VarAssign | MultiVarAssign:
        var_refs = ctx.var_ref()

        if len(var_refs) == 2:
            return MultiVarAssign(
                vars=[self.visit(var_refs[0]), self.visit(var_refs[1])],
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
        children = list(ctx.getChildren())
        i = 1
        while i < len(children):
            text = children[i].getText()
            if text == "[":
                i += 1
                if children[i].getText() == "]":
                    accessors.append(IndexAccessor(var=name, index = None))
                else:
                    index = self._parse_scalar_literal(children[i].getText())
                    accessors.append(IndexAccessor(var=name, index=index))
                    i += 1
            elif text == ".":
                i += 1
                accessors.append(FieldAccessor(var=name, field=self.visit(children[i])))
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
        if ctx.list_():
            return self.visit(ctx.list_())
        if ctx.dict_():
            return self.visit(ctx.dict_())

    def visitList(self, ctx) -> ListLiteral:
        return ListLiteral(elements = [self.visit(f) for f in ctx.data()])

    def visitDict(self, ctx) -> DictLiteral:
        return DictLiteral(fields = [self.visit(f) for f in ctx.no_acs_mode_var_decl()])

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

    def visitReturn(self, ctx) -> Return:
        exprs = ctx.expr()
        if not exprs:
            return Return()
        if len(exprs) == 2:
            return Return(
                error=self.visit(exprs[0]),
                val=self.visit(exprs[1])
            )
        return Return(val=self.visit(exprs[0]))

    def visitDefer(self, ctx) -> Defer:
        return Defer(expr=self.visit(ctx.expr()))

    def _parse_type(self, text: str) -> Type:
        try:
            return ArrayType(text)
        except ValueError:
            return BaseType(text)

    def _parse_scalar_literal(self, text: str) -> IntLiteral | StringLiteral:
        if text.startswith('"'):
            return StringLiteral(val=text[1:-1])
        return IntLiteral(val=int(text))

    def _is_nwln(self, ctx: SwagLangParser) -> bool:
        return hasattr(ctx, 'symbol')
