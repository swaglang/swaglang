# Generated from grammar/SwagLangParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .SwagLangParser import SwagLangParser
else:
    from SwagLangParser import SwagLangParser

# This class defines a complete listener for a parse tree produced by SwagLangParser.
class SwagLangParserListener(ParseTreeListener):

    # Enter a parse tree produced by SwagLangParser#prog.
    def enterProg(self, ctx:SwagLangParser.ProgContext):
        pass

    # Exit a parse tree produced by SwagLangParser#prog.
    def exitProg(self, ctx:SwagLangParser.ProgContext):
        pass


    # Enter a parse tree produced by SwagLangParser#stmts.
    def enterStmts(self, ctx:SwagLangParser.StmtsContext):
        pass

    # Exit a parse tree produced by SwagLangParser#stmts.
    def exitStmts(self, ctx:SwagLangParser.StmtsContext):
        pass


    # Enter a parse tree produced by SwagLangParser#stmt.
    def enterStmt(self, ctx:SwagLangParser.StmtContext):
        pass

    # Exit a parse tree produced by SwagLangParser#stmt.
    def exitStmt(self, ctx:SwagLangParser.StmtContext):
        pass


    # Enter a parse tree produced by SwagLangParser#pure_stmt.
    def enterPure_stmt(self, ctx:SwagLangParser.Pure_stmtContext):
        pass

    # Exit a parse tree produced by SwagLangParser#pure_stmt.
    def exitPure_stmt(self, ctx:SwagLangParser.Pure_stmtContext):
        pass


    # Enter a parse tree produced by SwagLangParser#code_block.
    def enterCode_block(self, ctx:SwagLangParser.Code_blockContext):
        pass

    # Exit a parse tree produced by SwagLangParser#code_block.
    def exitCode_block(self, ctx:SwagLangParser.Code_blockContext):
        pass


    # Enter a parse tree produced by SwagLangParser#func_stmt.
    def enterFunc_stmt(self, ctx:SwagLangParser.Func_stmtContext):
        pass

    # Exit a parse tree produced by SwagLangParser#func_stmt.
    def exitFunc_stmt(self, ctx:SwagLangParser.Func_stmtContext):
        pass


    # Enter a parse tree produced by SwagLangParser#pure_func_stmt.
    def enterPure_func_stmt(self, ctx:SwagLangParser.Pure_func_stmtContext):
        pass

    # Exit a parse tree produced by SwagLangParser#pure_func_stmt.
    def exitPure_func_stmt(self, ctx:SwagLangParser.Pure_func_stmtContext):
        pass


    # Enter a parse tree produced by SwagLangParser#defer.
    def enterDefer(self, ctx:SwagLangParser.DeferContext):
        pass

    # Exit a parse tree produced by SwagLangParser#defer.
    def exitDefer(self, ctx:SwagLangParser.DeferContext):
        pass


    # Enter a parse tree produced by SwagLangParser#break.
    def enterBreak(self, ctx:SwagLangParser.BreakContext):
        pass

    # Exit a parse tree produced by SwagLangParser#break.
    def exitBreak(self, ctx:SwagLangParser.BreakContext):
        pass


    # Enter a parse tree produced by SwagLangParser#return.
    def enterReturn(self, ctx:SwagLangParser.ReturnContext):
        pass

    # Exit a parse tree produced by SwagLangParser#return.
    def exitReturn(self, ctx:SwagLangParser.ReturnContext):
        pass


    # Enter a parse tree produced by SwagLangParser#func_decl.
    def enterFunc_decl(self, ctx:SwagLangParser.Func_declContext):
        pass

    # Exit a parse tree produced by SwagLangParser#func_decl.
    def exitFunc_decl(self, ctx:SwagLangParser.Func_declContext):
        pass


    # Enter a parse tree produced by SwagLangParser#return_type.
    def enterReturn_type(self, ctx:SwagLangParser.Return_typeContext):
        pass

    # Exit a parse tree produced by SwagLangParser#return_type.
    def exitReturn_type(self, ctx:SwagLangParser.Return_typeContext):
        pass


    # Enter a parse tree produced by SwagLangParser#data.
    def enterData(self, ctx:SwagLangParser.DataContext):
        pass

    # Exit a parse tree produced by SwagLangParser#data.
    def exitData(self, ctx:SwagLangParser.DataContext):
        pass


    # Enter a parse tree produced by SwagLangParser#list.
    def enterList(self, ctx:SwagLangParser.ListContext):
        pass

    # Exit a parse tree produced by SwagLangParser#list.
    def exitList(self, ctx:SwagLangParser.ListContext):
        pass


    # Enter a parse tree produced by SwagLangParser#dict.
    def enterDict(self, ctx:SwagLangParser.DictContext):
        pass

    # Exit a parse tree produced by SwagLangParser#dict.
    def exitDict(self, ctx:SwagLangParser.DictContext):
        pass


    # Enter a parse tree produced by SwagLangParser#no_acs_mode_var_decl.
    def enterNo_acs_mode_var_decl(self, ctx:SwagLangParser.No_acs_mode_var_declContext):
        pass

    # Exit a parse tree produced by SwagLangParser#no_acs_mode_var_decl.
    def exitNo_acs_mode_var_decl(self, ctx:SwagLangParser.No_acs_mode_var_declContext):
        pass


    # Enter a parse tree produced by SwagLangParser#var_ref.
    def enterVar_ref(self, ctx:SwagLangParser.Var_refContext):
        pass

    # Exit a parse tree produced by SwagLangParser#var_ref.
    def exitVar_ref(self, ctx:SwagLangParser.Var_refContext):
        pass


    # Enter a parse tree produced by SwagLangParser#var_decl.
    def enterVar_decl(self, ctx:SwagLangParser.Var_declContext):
        pass

    # Exit a parse tree produced by SwagLangParser#var_decl.
    def exitVar_decl(self, ctx:SwagLangParser.Var_declContext):
        pass


    # Enter a parse tree produced by SwagLangParser#var_assign.
    def enterVar_assign(self, ctx:SwagLangParser.Var_assignContext):
        pass

    # Exit a parse tree produced by SwagLangParser#var_assign.
    def exitVar_assign(self, ctx:SwagLangParser.Var_assignContext):
        pass


    # Enter a parse tree produced by SwagLangParser#conditional_body.
    def enterConditional_body(self, ctx:SwagLangParser.Conditional_bodyContext):
        pass

    # Exit a parse tree produced by SwagLangParser#conditional_body.
    def exitConditional_body(self, ctx:SwagLangParser.Conditional_bodyContext):
        pass


    # Enter a parse tree produced by SwagLangParser#loop_body.
    def enterLoop_body(self, ctx:SwagLangParser.Loop_bodyContext):
        pass

    # Exit a parse tree produced by SwagLangParser#loop_body.
    def exitLoop_body(self, ctx:SwagLangParser.Loop_bodyContext):
        pass


    # Enter a parse tree produced by SwagLangParser#loop.
    def enterLoop(self, ctx:SwagLangParser.LoopContext):
        pass

    # Exit a parse tree produced by SwagLangParser#loop.
    def exitLoop(self, ctx:SwagLangParser.LoopContext):
        pass


    # Enter a parse tree produced by SwagLangParser#while_loop.
    def enterWhile_loop(self, ctx:SwagLangParser.While_loopContext):
        pass

    # Exit a parse tree produced by SwagLangParser#while_loop.
    def exitWhile_loop(self, ctx:SwagLangParser.While_loopContext):
        pass


    # Enter a parse tree produced by SwagLangParser#do_while_loop.
    def enterDo_while_loop(self, ctx:SwagLangParser.Do_while_loopContext):
        pass

    # Exit a parse tree produced by SwagLangParser#do_while_loop.
    def exitDo_while_loop(self, ctx:SwagLangParser.Do_while_loopContext):
        pass


    # Enter a parse tree produced by SwagLangParser#for_loop.
    def enterFor_loop(self, ctx:SwagLangParser.For_loopContext):
        pass

    # Exit a parse tree produced by SwagLangParser#for_loop.
    def exitFor_loop(self, ctx:SwagLangParser.For_loopContext):
        pass


    # Enter a parse tree produced by SwagLangParser#forin.
    def enterForin(self, ctx:SwagLangParser.ForinContext):
        pass

    # Exit a parse tree produced by SwagLangParser#forin.
    def exitForin(self, ctx:SwagLangParser.ForinContext):
        pass


    # Enter a parse tree produced by SwagLangParser#conditional.
    def enterConditional(self, ctx:SwagLangParser.ConditionalContext):
        pass

    # Exit a parse tree produced by SwagLangParser#conditional.
    def exitConditional(self, ctx:SwagLangParser.ConditionalContext):
        pass


    # Enter a parse tree produced by SwagLangParser#condition.
    def enterCondition(self, ctx:SwagLangParser.ConditionContext):
        pass

    # Exit a parse tree produced by SwagLangParser#condition.
    def exitCondition(self, ctx:SwagLangParser.ConditionContext):
        pass


    # Enter a parse tree produced by SwagLangParser#expr.
    def enterExpr(self, ctx:SwagLangParser.ExprContext):
        pass

    # Exit a parse tree produced by SwagLangParser#expr.
    def exitExpr(self, ctx:SwagLangParser.ExprContext):
        pass


    # Enter a parse tree produced by SwagLangParser#func_call.
    def enterFunc_call(self, ctx:SwagLangParser.Func_callContext):
        pass

    # Exit a parse tree produced by SwagLangParser#func_call.
    def exitFunc_call(self, ctx:SwagLangParser.Func_callContext):
        pass


    # Enter a parse tree produced by SwagLangParser#param_decl.
    def enterParam_decl(self, ctx:SwagLangParser.Param_declContext):
        pass

    # Exit a parse tree produced by SwagLangParser#param_decl.
    def exitParam_decl(self, ctx:SwagLangParser.Param_declContext):
        pass


    # Enter a parse tree produced by SwagLangParser#params.
    def enterParams(self, ctx:SwagLangParser.ParamsContext):
        pass

    # Exit a parse tree produced by SwagLangParser#params.
    def exitParams(self, ctx:SwagLangParser.ParamsContext):
        pass



del SwagLangParser