# Generated from grammar/SwagLangParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .SwagLangParser import SwagLangParser
else:
    from SwagLangParser import SwagLangParser

# This class defines a complete generic visitor for a parse tree produced by SwagLangParser.

class SwagLangParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SwagLangParser#prog.
    def visitProg(self, ctx:SwagLangParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SwagLangParser#stmts.
    def visitStmts(self, ctx:SwagLangParser.StmtsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SwagLangParser#stmt.
    def visitStmt(self, ctx:SwagLangParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SwagLangParser#pure_stmt.
    def visitPure_stmt(self, ctx:SwagLangParser.Pure_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SwagLangParser#code_block.
    def visitCode_block(self, ctx:SwagLangParser.Code_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SwagLangParser#func_stmt.
    def visitFunc_stmt(self, ctx:SwagLangParser.Func_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SwagLangParser#pure_func_stmt.
    def visitPure_func_stmt(self, ctx:SwagLangParser.Pure_func_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SwagLangParser#defer.
    def visitDefer(self, ctx:SwagLangParser.DeferContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SwagLangParser#break.
    def visitBreak(self, ctx:SwagLangParser.BreakContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SwagLangParser#return.
    def visitReturn(self, ctx:SwagLangParser.ReturnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SwagLangParser#func_decl.
    def visitFunc_decl(self, ctx:SwagLangParser.Func_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SwagLangParser#return_type.
    def visitReturn_type(self, ctx:SwagLangParser.Return_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SwagLangParser#data.
    def visitData(self, ctx:SwagLangParser.DataContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SwagLangParser#list.
    def visitList(self, ctx:SwagLangParser.ListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SwagLangParser#dict.
    def visitDict(self, ctx:SwagLangParser.DictContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SwagLangParser#no_acs_mode_var_decl.
    def visitNo_acs_mode_var_decl(self, ctx:SwagLangParser.No_acs_mode_var_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SwagLangParser#var_ref.
    def visitVar_ref(self, ctx:SwagLangParser.Var_refContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SwagLangParser#var_decl.
    def visitVar_decl(self, ctx:SwagLangParser.Var_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SwagLangParser#var_assign.
    def visitVar_assign(self, ctx:SwagLangParser.Var_assignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SwagLangParser#conditional_body.
    def visitConditional_body(self, ctx:SwagLangParser.Conditional_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SwagLangParser#loop_body.
    def visitLoop_body(self, ctx:SwagLangParser.Loop_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SwagLangParser#loop.
    def visitLoop(self, ctx:SwagLangParser.LoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SwagLangParser#while_loop.
    def visitWhile_loop(self, ctx:SwagLangParser.While_loopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SwagLangParser#do_while_loop.
    def visitDo_while_loop(self, ctx:SwagLangParser.Do_while_loopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SwagLangParser#for_loop.
    def visitFor_loop(self, ctx:SwagLangParser.For_loopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SwagLangParser#forin.
    def visitForin(self, ctx:SwagLangParser.ForinContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SwagLangParser#conditional.
    def visitConditional(self, ctx:SwagLangParser.ConditionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SwagLangParser#condition.
    def visitCondition(self, ctx:SwagLangParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SwagLangParser#expr.
    def visitExpr(self, ctx:SwagLangParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SwagLangParser#func_call.
    def visitFunc_call(self, ctx:SwagLangParser.Func_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SwagLangParser#param_decl.
    def visitParam_decl(self, ctx:SwagLangParser.Param_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SwagLangParser#params.
    def visitParams(self, ctx:SwagLangParser.ParamsContext):
        return self.visitChildren(ctx)



del SwagLangParser