# Generated from grammar/SwagLangParser.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,55,372,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,1,0,1,0,1,0,1,
        1,1,1,5,1,70,8,1,10,1,12,1,73,9,1,1,2,1,2,1,3,1,3,3,3,79,8,3,1,4,
        1,4,1,4,1,4,5,4,85,8,4,10,4,12,4,88,9,4,1,4,1,4,1,5,3,5,93,8,5,1,
        6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,105,8,6,1,7,1,7,1,7,1,
        8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,120,8,9,1,10,1,10,1,10,
        1,10,1,10,1,10,5,10,128,8,10,10,10,12,10,131,9,10,3,10,133,8,10,
        1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,11,3,11,144,8,11,1,12,
        1,12,1,12,1,12,1,12,1,12,3,12,152,8,12,1,13,1,13,1,13,1,13,5,13,
        158,8,13,10,13,12,13,161,9,13,3,13,163,8,13,1,13,1,13,1,14,1,14,
        5,14,169,8,14,10,14,12,14,172,9,14,1,14,1,14,1,14,5,14,177,8,14,
        10,14,12,14,180,9,14,1,14,5,14,183,8,14,10,14,12,14,186,9,14,3,14,
        188,8,14,1,14,5,14,191,8,14,10,14,12,14,194,9,14,1,14,1,14,1,15,
        1,15,1,15,3,15,201,8,15,1,15,1,15,1,15,1,16,1,16,1,16,3,16,209,8,
        16,1,16,1,16,1,16,5,16,214,8,16,10,16,12,16,217,9,16,1,17,1,17,1,
        17,1,17,3,17,223,8,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,3,
        17,233,8,17,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,3,
        18,245,8,18,1,19,1,19,1,20,1,20,1,21,1,21,1,21,3,21,254,8,21,1,22,
        1,22,1,22,1,22,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,24,1,24,3,24,
        269,8,24,1,24,1,24,3,24,273,8,24,1,24,1,24,3,24,277,8,24,1,24,3,
        24,280,8,24,1,24,1,24,1,25,1,25,1,25,1,25,1,25,3,25,289,8,25,1,26,
        1,26,1,26,1,26,1,26,1,26,1,26,5,26,298,8,26,10,26,12,26,301,9,26,
        1,26,1,26,3,26,305,8,26,1,27,1,27,1,28,1,28,1,28,1,28,1,28,1,28,
        1,28,1,28,1,28,1,28,1,28,1,28,1,28,3,28,322,8,28,1,28,1,28,1,28,
        1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,
        1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,5,28,348,8,28,10,28,12,28,
        351,9,28,1,29,1,29,1,29,1,29,1,29,1,30,1,30,1,30,1,30,1,31,1,31,
        1,31,5,31,365,8,31,10,31,12,31,368,9,31,3,31,370,8,31,1,31,0,1,56,
        32,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,
        44,46,48,50,52,54,56,58,60,62,0,6,1,0,49,50,1,0,26,31,1,0,39,40,
        1,0,36,38,1,0,47,48,1,0,41,46,400,0,64,1,0,0,0,2,71,1,0,0,0,4,74,
        1,0,0,0,6,78,1,0,0,0,8,80,1,0,0,0,10,92,1,0,0,0,12,104,1,0,0,0,14,
        106,1,0,0,0,16,109,1,0,0,0,18,119,1,0,0,0,20,121,1,0,0,0,22,143,
        1,0,0,0,24,151,1,0,0,0,26,153,1,0,0,0,28,166,1,0,0,0,30,197,1,0,
        0,0,32,205,1,0,0,0,34,232,1,0,0,0,36,244,1,0,0,0,38,246,1,0,0,0,
        40,248,1,0,0,0,42,253,1,0,0,0,44,255,1,0,0,0,46,259,1,0,0,0,48,279,
        1,0,0,0,50,283,1,0,0,0,52,290,1,0,0,0,54,306,1,0,0,0,56,321,1,0,
        0,0,58,352,1,0,0,0,60,357,1,0,0,0,62,369,1,0,0,0,64,65,3,2,1,0,65,
        66,5,0,0,1,66,1,1,0,0,0,67,70,3,4,2,0,68,70,5,52,0,0,69,67,1,0,0,
        0,69,68,1,0,0,0,70,73,1,0,0,0,71,69,1,0,0,0,71,72,1,0,0,0,72,3,1,
        0,0,0,73,71,1,0,0,0,74,75,3,6,3,0,75,5,1,0,0,0,76,79,3,20,10,0,77,
        79,3,34,17,0,78,76,1,0,0,0,78,77,1,0,0,0,79,7,1,0,0,0,80,86,5,19,
        0,0,81,82,3,10,5,0,82,83,5,52,0,0,83,85,1,0,0,0,84,81,1,0,0,0,85,
        88,1,0,0,0,86,84,1,0,0,0,86,87,1,0,0,0,87,89,1,0,0,0,88,86,1,0,0,
        0,89,90,5,20,0,0,90,9,1,0,0,0,91,93,3,12,6,0,92,91,1,0,0,0,92,93,
        1,0,0,0,93,11,1,0,0,0,94,105,3,20,10,0,95,105,3,36,18,0,96,105,3,
        58,29,0,97,105,3,34,17,0,98,105,3,42,21,0,99,105,3,52,26,0,100,105,
        3,16,8,0,101,105,3,18,9,0,102,105,3,14,7,0,103,105,3,56,28,0,104,
        94,1,0,0,0,104,95,1,0,0,0,104,96,1,0,0,0,104,97,1,0,0,0,104,98,1,
        0,0,0,104,99,1,0,0,0,104,100,1,0,0,0,104,101,1,0,0,0,104,102,1,0,
        0,0,104,103,1,0,0,0,105,13,1,0,0,0,106,107,5,11,0,0,107,108,3,56,
        28,0,108,15,1,0,0,0,109,110,5,9,0,0,110,17,1,0,0,0,111,120,5,10,
        0,0,112,113,5,10,0,0,113,120,3,56,28,0,114,115,5,10,0,0,115,116,
        3,56,28,0,116,117,5,24,0,0,117,118,3,56,28,0,118,120,1,0,0,0,119,
        111,1,0,0,0,119,112,1,0,0,0,119,114,1,0,0,0,120,19,1,0,0,0,121,122,
        3,22,11,0,122,123,5,14,0,0,123,132,5,17,0,0,124,129,3,60,30,0,125,
        126,5,24,0,0,126,128,3,60,30,0,127,125,1,0,0,0,128,131,1,0,0,0,129,
        127,1,0,0,0,129,130,1,0,0,0,130,133,1,0,0,0,131,129,1,0,0,0,132,
        124,1,0,0,0,132,133,1,0,0,0,133,134,1,0,0,0,134,135,5,18,0,0,135,
        136,3,8,4,0,136,21,1,0,0,0,137,144,5,1,0,0,138,139,5,17,0,0,139,
        140,5,14,0,0,140,141,5,24,0,0,141,142,5,1,0,0,142,144,5,18,0,0,143,
        137,1,0,0,0,143,138,1,0,0,0,144,23,1,0,0,0,145,152,5,50,0,0,146,
        152,5,49,0,0,147,152,5,51,0,0,148,152,5,13,0,0,149,152,3,26,13,0,
        150,152,3,28,14,0,151,145,1,0,0,0,151,146,1,0,0,0,151,147,1,0,0,
        0,151,148,1,0,0,0,151,149,1,0,0,0,151,150,1,0,0,0,152,25,1,0,0,0,
        153,162,5,21,0,0,154,159,3,24,12,0,155,156,5,24,0,0,156,158,3,24,
        12,0,157,155,1,0,0,0,158,161,1,0,0,0,159,157,1,0,0,0,159,160,1,0,
        0,0,160,163,1,0,0,0,161,159,1,0,0,0,162,154,1,0,0,0,162,163,1,0,
        0,0,163,164,1,0,0,0,164,165,5,22,0,0,165,27,1,0,0,0,166,170,5,19,
        0,0,167,169,5,52,0,0,168,167,1,0,0,0,169,172,1,0,0,0,170,168,1,0,
        0,0,170,171,1,0,0,0,171,187,1,0,0,0,172,170,1,0,0,0,173,184,3,30,
        15,0,174,178,5,24,0,0,175,177,5,52,0,0,176,175,1,0,0,0,177,180,1,
        0,0,0,178,176,1,0,0,0,178,179,1,0,0,0,179,181,1,0,0,0,180,178,1,
        0,0,0,181,183,3,30,15,0,182,174,1,0,0,0,183,186,1,0,0,0,184,182,
        1,0,0,0,184,185,1,0,0,0,185,188,1,0,0,0,186,184,1,0,0,0,187,173,
        1,0,0,0,187,188,1,0,0,0,188,192,1,0,0,0,189,191,5,52,0,0,190,189,
        1,0,0,0,191,194,1,0,0,0,192,190,1,0,0,0,192,193,1,0,0,0,193,195,
        1,0,0,0,194,192,1,0,0,0,195,196,5,20,0,0,196,29,1,0,0,0,197,200,
        5,14,0,0,198,199,5,15,0,0,199,201,5,1,0,0,200,198,1,0,0,0,200,201,
        1,0,0,0,201,202,1,0,0,0,202,203,5,26,0,0,203,204,3,56,28,0,204,31,
        1,0,0,0,205,215,5,14,0,0,206,208,5,21,0,0,207,209,7,0,0,0,208,207,
        1,0,0,0,208,209,1,0,0,0,209,210,1,0,0,0,210,214,5,22,0,0,211,212,
        5,25,0,0,212,214,3,32,16,0,213,206,1,0,0,0,213,211,1,0,0,0,214,217,
        1,0,0,0,215,213,1,0,0,0,215,216,1,0,0,0,216,33,1,0,0,0,217,215,1,
        0,0,0,218,219,5,12,0,0,219,222,5,14,0,0,220,221,5,15,0,0,221,223,
        5,1,0,0,222,220,1,0,0,0,222,223,1,0,0,0,223,224,1,0,0,0,224,225,
        5,26,0,0,225,233,3,56,28,0,226,227,5,12,0,0,227,228,5,14,0,0,228,
        229,5,24,0,0,229,230,5,14,0,0,230,231,5,26,0,0,231,233,3,58,29,0,
        232,218,1,0,0,0,232,226,1,0,0,0,233,35,1,0,0,0,234,235,3,32,16,0,
        235,236,7,1,0,0,236,237,3,56,28,0,237,245,1,0,0,0,238,239,3,32,16,
        0,239,240,5,24,0,0,240,241,3,32,16,0,241,242,5,26,0,0,242,243,3,
        58,29,0,243,245,1,0,0,0,244,234,1,0,0,0,244,238,1,0,0,0,245,37,1,
        0,0,0,246,247,3,8,4,0,247,39,1,0,0,0,248,249,3,8,4,0,249,41,1,0,
        0,0,250,254,3,48,24,0,251,254,3,44,22,0,252,254,3,46,23,0,253,250,
        1,0,0,0,253,251,1,0,0,0,253,252,1,0,0,0,254,43,1,0,0,0,255,256,5,
        7,0,0,256,257,3,54,27,0,257,258,3,40,20,0,258,45,1,0,0,0,259,260,
        5,8,0,0,260,261,3,40,20,0,261,262,5,7,0,0,262,263,5,17,0,0,263,264,
        3,54,27,0,264,265,5,18,0,0,265,47,1,0,0,0,266,268,5,5,0,0,267,269,
        3,30,15,0,268,267,1,0,0,0,268,269,1,0,0,0,269,270,1,0,0,0,270,272,
        5,16,0,0,271,273,3,54,27,0,272,271,1,0,0,0,272,273,1,0,0,0,273,274,
        1,0,0,0,274,276,5,16,0,0,275,277,3,56,28,0,276,275,1,0,0,0,276,277,
        1,0,0,0,277,280,1,0,0,0,278,280,3,50,25,0,279,266,1,0,0,0,279,278,
        1,0,0,0,280,281,1,0,0,0,281,282,3,40,20,0,282,49,1,0,0,0,283,284,
        5,5,0,0,284,285,5,14,0,0,285,288,5,6,0,0,286,289,3,58,29,0,287,289,
        3,32,16,0,288,286,1,0,0,0,288,287,1,0,0,0,289,51,1,0,0,0,290,291,
        5,2,0,0,291,292,3,54,27,0,292,299,3,38,19,0,293,294,5,3,0,0,294,
        295,3,54,27,0,295,296,3,38,19,0,296,298,1,0,0,0,297,293,1,0,0,0,
        298,301,1,0,0,0,299,297,1,0,0,0,299,300,1,0,0,0,300,304,1,0,0,0,
        301,299,1,0,0,0,302,303,5,4,0,0,303,305,3,38,19,0,304,302,1,0,0,
        0,304,305,1,0,0,0,305,53,1,0,0,0,306,307,3,56,28,0,307,55,1,0,0,
        0,308,309,6,28,-1,0,309,310,5,17,0,0,310,311,3,56,28,0,311,312,5,
        18,0,0,312,322,1,0,0,0,313,322,3,24,12,0,314,322,3,58,29,0,315,322,
        3,32,16,0,316,317,3,32,16,0,317,318,7,2,0,0,318,322,1,0,0,0,319,
        320,5,34,0,0,320,322,3,56,28,8,321,308,1,0,0,0,321,313,1,0,0,0,321,
        314,1,0,0,0,321,315,1,0,0,0,321,316,1,0,0,0,321,319,1,0,0,0,322,
        349,1,0,0,0,323,324,10,7,0,0,324,325,5,35,0,0,325,348,3,56,28,7,
        326,327,10,6,0,0,327,328,7,3,0,0,328,348,3,56,28,7,329,330,10,5,
        0,0,330,331,7,4,0,0,331,348,3,56,28,6,332,333,10,4,0,0,333,334,7,
        5,0,0,334,348,3,56,28,5,335,336,10,3,0,0,336,337,5,32,0,0,337,348,
        3,56,28,4,338,339,10,2,0,0,339,340,5,33,0,0,340,348,3,56,28,3,341,
        342,10,1,0,0,342,343,5,23,0,0,343,344,3,56,28,0,344,345,5,15,0,0,
        345,346,3,56,28,2,346,348,1,0,0,0,347,323,1,0,0,0,347,326,1,0,0,
        0,347,329,1,0,0,0,347,332,1,0,0,0,347,335,1,0,0,0,347,338,1,0,0,
        0,347,341,1,0,0,0,348,351,1,0,0,0,349,347,1,0,0,0,349,350,1,0,0,
        0,350,57,1,0,0,0,351,349,1,0,0,0,352,353,5,14,0,0,353,354,5,17,0,
        0,354,355,3,62,31,0,355,356,5,18,0,0,356,59,1,0,0,0,357,358,5,14,
        0,0,358,359,5,15,0,0,359,360,5,1,0,0,360,61,1,0,0,0,361,366,3,56,
        28,0,362,363,5,24,0,0,363,365,3,56,28,0,364,362,1,0,0,0,365,368,
        1,0,0,0,366,364,1,0,0,0,366,367,1,0,0,0,367,370,1,0,0,0,368,366,
        1,0,0,0,369,361,1,0,0,0,369,370,1,0,0,0,370,63,1,0,0,0,38,69,71,
        78,86,92,104,119,129,132,143,151,159,162,170,178,184,187,192,200,
        208,213,215,222,232,244,253,268,272,276,279,288,299,304,321,347,
        349,366,369
    ]

class SwagLangParser ( Parser ):

    grammarFileName = "SwagLangParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'if'", "<INVALID>", "'else'", 
                     "'for'", "'in'", "'while'", "'do'", "'break'", "'return'", 
                     "'defer'", "<INVALID>", "<INVALID>", "<INVALID>", "':'", 
                     "';'", "'('", "')'", "'{'", "'}'", "'['", "']'", "'?'", 
                     "','", "'.'", "'='", "'+='", "'-='", "'*='", "'/='", 
                     "'%='", "'&&'", "'||'", "'!'", "'**'", "'*'", "'/'", 
                     "'%'", "'++'", "'--'", "'>'", "'<'", "'=='", "'!='", 
                     "'>='", "'<='", "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>", "TYPE", "IF", "ELSE_IF", "ELSE", "FOR", 
                      "IN", "WHILE", "DO", "BREAK", "RETURN", "DEFER", "ACCESS_MOD", 
                      "BOOL", "IDENT", "COLUMN", "SEMICOL", "L_PAREN", "R_PAREN", 
                      "L_CURLY", "R_CURLY", "L_BRACKET", "R_BRACKET", "QUESTION", 
                      "COMMA", "DOT", "ASSIGN", "ADD_ASSIGN", "SUB_ASSIGN", 
                      "MUL_ASSIGN", "DIV_ASSIGN", "MOD_ASSIGN", "AND", "OR", 
                      "NOT", "EXP", "MUL", "DIV", "MOD", "INC", "DEC", "GT", 
                      "LT", "EQ", "NEQ", "GTE", "LTE", "PLUS", "MINUS", 
                      "STRING", "INT", "FLOAT", "NWLN", "SPACE", "COMMENT", 
                      "INLINE_COMMENT" ]

    RULE_prog = 0
    RULE_stmts = 1
    RULE_stmt = 2
    RULE_pure_stmt = 3
    RULE_code_block = 4
    RULE_func_stmt = 5
    RULE_pure_func_stmt = 6
    RULE_defer = 7
    RULE_break = 8
    RULE_return = 9
    RULE_func_decl = 10
    RULE_return_type = 11
    RULE_data = 12
    RULE_list = 13
    RULE_dict = 14
    RULE_no_acs_mode_var_decl = 15
    RULE_var_ref = 16
    RULE_var_decl = 17
    RULE_var_assign = 18
    RULE_conditional_body = 19
    RULE_loop_body = 20
    RULE_loop = 21
    RULE_while_loop = 22
    RULE_do_while_loop = 23
    RULE_for_loop = 24
    RULE_forin = 25
    RULE_conditional = 26
    RULE_condition = 27
    RULE_expr = 28
    RULE_func_call = 29
    RULE_param_decl = 30
    RULE_params = 31

    ruleNames =  [ "prog", "stmts", "stmt", "pure_stmt", "code_block", "func_stmt", 
                   "pure_func_stmt", "defer", "break", "return", "func_decl", 
                   "return_type", "data", "list", "dict", "no_acs_mode_var_decl", 
                   "var_ref", "var_decl", "var_assign", "conditional_body", 
                   "loop_body", "loop", "while_loop", "do_while_loop", "for_loop", 
                   "forin", "conditional", "condition", "expr", "func_call", 
                   "param_decl", "params" ]

    EOF = Token.EOF
    TYPE=1
    IF=2
    ELSE_IF=3
    ELSE=4
    FOR=5
    IN=6
    WHILE=7
    DO=8
    BREAK=9
    RETURN=10
    DEFER=11
    ACCESS_MOD=12
    BOOL=13
    IDENT=14
    COLUMN=15
    SEMICOL=16
    L_PAREN=17
    R_PAREN=18
    L_CURLY=19
    R_CURLY=20
    L_BRACKET=21
    R_BRACKET=22
    QUESTION=23
    COMMA=24
    DOT=25
    ASSIGN=26
    ADD_ASSIGN=27
    SUB_ASSIGN=28
    MUL_ASSIGN=29
    DIV_ASSIGN=30
    MOD_ASSIGN=31
    AND=32
    OR=33
    NOT=34
    EXP=35
    MUL=36
    DIV=37
    MOD=38
    INC=39
    DEC=40
    GT=41
    LT=42
    EQ=43
    NEQ=44
    GTE=45
    LTE=46
    PLUS=47
    MINUS=48
    STRING=49
    INT=50
    FLOAT=51
    NWLN=52
    SPACE=53
    COMMENT=54
    INLINE_COMMENT=55

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmts(self):
            return self.getTypedRuleContext(SwagLangParser.StmtsContext,0)


        def EOF(self):
            return self.getToken(SwagLangParser.EOF, 0)

        def getRuleIndex(self):
            return SwagLangParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = SwagLangParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.stmts()
            self.state = 65
            self.match(SwagLangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SwagLangParser.StmtContext)
            else:
                return self.getTypedRuleContext(SwagLangParser.StmtContext,i)


        def NWLN(self, i:int=None):
            if i is None:
                return self.getTokens(SwagLangParser.NWLN)
            else:
                return self.getToken(SwagLangParser.NWLN, i)

        def getRuleIndex(self):
            return SwagLangParser.RULE_stmts

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmts" ):
                listener.enterStmts(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmts" ):
                listener.exitStmts(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmts" ):
                return visitor.visitStmts(self)
            else:
                return visitor.visitChildren(self)




    def stmts(self):

        localctx = SwagLangParser.StmtsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stmts)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4503599627505666) != 0):
                self.state = 69
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1, 12, 17]:
                    self.state = 67
                    self.stmt()
                    pass
                elif token in [52]:
                    self.state = 68
                    self.match(SwagLangParser.NWLN)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 73
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pure_stmt(self):
            return self.getTypedRuleContext(SwagLangParser.Pure_stmtContext,0)


        def getRuleIndex(self):
            return SwagLangParser.RULE_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmt" ):
                listener.enterStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmt" ):
                listener.exitStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = SwagLangParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.pure_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Pure_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def func_decl(self):
            return self.getTypedRuleContext(SwagLangParser.Func_declContext,0)


        def var_decl(self):
            return self.getTypedRuleContext(SwagLangParser.Var_declContext,0)


        def getRuleIndex(self):
            return SwagLangParser.RULE_pure_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPure_stmt" ):
                listener.enterPure_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPure_stmt" ):
                listener.exitPure_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPure_stmt" ):
                return visitor.visitPure_stmt(self)
            else:
                return visitor.visitChildren(self)




    def pure_stmt(self):

        localctx = SwagLangParser.Pure_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_pure_stmt)
        try:
            self.state = 78
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 17]:
                self.enterOuterAlt(localctx, 1)
                self.state = 76
                self.func_decl()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 2)
                self.state = 77
                self.var_decl()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Code_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L_CURLY(self):
            return self.getToken(SwagLangParser.L_CURLY, 0)

        def R_CURLY(self):
            return self.getToken(SwagLangParser.R_CURLY, 0)

        def func_stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SwagLangParser.Func_stmtContext)
            else:
                return self.getTypedRuleContext(SwagLangParser.Func_stmtContext,i)


        def NWLN(self, i:int=None):
            if i is None:
                return self.getTokens(SwagLangParser.NWLN)
            else:
                return self.getToken(SwagLangParser.NWLN, i)

        def getRuleIndex(self):
            return SwagLangParser.RULE_code_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCode_block" ):
                listener.enterCode_block(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCode_block" ):
                listener.exitCode_block(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCode_block" ):
                return visitor.visitCode_block(self)
            else:
                return visitor.visitChildren(self)




    def code_block(self):

        localctx = SwagLangParser.Code_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_code_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(SwagLangParser.L_CURLY)
            self.state = 86
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8444266483974054) != 0):
                self.state = 81
                self.func_stmt()
                self.state = 82
                self.match(SwagLangParser.NWLN)
                self.state = 88
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 89
            self.match(SwagLangParser.R_CURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pure_func_stmt(self):
            return self.getTypedRuleContext(SwagLangParser.Pure_func_stmtContext,0)


        def getRuleIndex(self):
            return SwagLangParser.RULE_func_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc_stmt" ):
                listener.enterFunc_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc_stmt" ):
                listener.exitFunc_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_stmt" ):
                return visitor.visitFunc_stmt(self)
            else:
                return visitor.visitChildren(self)




    def func_stmt(self):

        localctx = SwagLangParser.Func_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_func_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 3940666856603558) != 0):
                self.state = 91
                self.pure_func_stmt()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Pure_func_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def func_decl(self):
            return self.getTypedRuleContext(SwagLangParser.Func_declContext,0)


        def var_assign(self):
            return self.getTypedRuleContext(SwagLangParser.Var_assignContext,0)


        def func_call(self):
            return self.getTypedRuleContext(SwagLangParser.Func_callContext,0)


        def var_decl(self):
            return self.getTypedRuleContext(SwagLangParser.Var_declContext,0)


        def loop(self):
            return self.getTypedRuleContext(SwagLangParser.LoopContext,0)


        def conditional(self):
            return self.getTypedRuleContext(SwagLangParser.ConditionalContext,0)


        def break_(self):
            return self.getTypedRuleContext(SwagLangParser.BreakContext,0)


        def return_(self):
            return self.getTypedRuleContext(SwagLangParser.ReturnContext,0)


        def defer(self):
            return self.getTypedRuleContext(SwagLangParser.DeferContext,0)


        def expr(self):
            return self.getTypedRuleContext(SwagLangParser.ExprContext,0)


        def getRuleIndex(self):
            return SwagLangParser.RULE_pure_func_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPure_func_stmt" ):
                listener.enterPure_func_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPure_func_stmt" ):
                listener.exitPure_func_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPure_func_stmt" ):
                return visitor.visitPure_func_stmt(self)
            else:
                return visitor.visitChildren(self)




    def pure_func_stmt(self):

        localctx = SwagLangParser.Pure_func_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_pure_func_stmt)
        try:
            self.state = 104
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 94
                self.func_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 95
                self.var_assign()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 96
                self.func_call()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 97
                self.var_decl()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 98
                self.loop()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 99
                self.conditional()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 100
                self.break_()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 101
                self.return_()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 102
                self.defer()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 103
                self.expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeferContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEFER(self):
            return self.getToken(SwagLangParser.DEFER, 0)

        def expr(self):
            return self.getTypedRuleContext(SwagLangParser.ExprContext,0)


        def getRuleIndex(self):
            return SwagLangParser.RULE_defer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefer" ):
                listener.enterDefer(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefer" ):
                listener.exitDefer(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefer" ):
                return visitor.visitDefer(self)
            else:
                return visitor.visitChildren(self)




    def defer(self):

        localctx = SwagLangParser.DeferContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_defer)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.match(SwagLangParser.DEFER)
            self.state = 107
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(SwagLangParser.BREAK, 0)

        def getRuleIndex(self):
            return SwagLangParser.RULE_break

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBreak" ):
                listener.enterBreak(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBreak" ):
                listener.exitBreak(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak" ):
                return visitor.visitBreak(self)
            else:
                return visitor.visitChildren(self)




    def break_(self):

        localctx = SwagLangParser.BreakContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_break)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.match(SwagLangParser.BREAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(SwagLangParser.RETURN, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SwagLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(SwagLangParser.ExprContext,i)


        def COMMA(self):
            return self.getToken(SwagLangParser.COMMA, 0)

        def getRuleIndex(self):
            return SwagLangParser.RULE_return

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturn" ):
                listener.enterReturn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturn" ):
                listener.exitReturn(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn" ):
                return visitor.visitReturn(self)
            else:
                return visitor.visitChildren(self)




    def return_(self):

        localctx = SwagLangParser.ReturnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_return)
        try:
            self.state = 119
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 111
                self.match(SwagLangParser.RETURN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 112
                self.match(SwagLangParser.RETURN)
                self.state = 113
                self.expr(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 114
                self.match(SwagLangParser.RETURN)
                self.state = 115
                self.expr(0)
                self.state = 116
                self.match(SwagLangParser.COMMA)
                self.state = 117
                self.expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def return_type(self):
            return self.getTypedRuleContext(SwagLangParser.Return_typeContext,0)


        def IDENT(self):
            return self.getToken(SwagLangParser.IDENT, 0)

        def L_PAREN(self):
            return self.getToken(SwagLangParser.L_PAREN, 0)

        def R_PAREN(self):
            return self.getToken(SwagLangParser.R_PAREN, 0)

        def code_block(self):
            return self.getTypedRuleContext(SwagLangParser.Code_blockContext,0)


        def param_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SwagLangParser.Param_declContext)
            else:
                return self.getTypedRuleContext(SwagLangParser.Param_declContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(SwagLangParser.COMMA)
            else:
                return self.getToken(SwagLangParser.COMMA, i)

        def getRuleIndex(self):
            return SwagLangParser.RULE_func_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc_decl" ):
                listener.enterFunc_decl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc_decl" ):
                listener.exitFunc_decl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_decl" ):
                return visitor.visitFunc_decl(self)
            else:
                return visitor.visitChildren(self)




    def func_decl(self):

        localctx = SwagLangParser.Func_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_func_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self.return_type()
            self.state = 122
            self.match(SwagLangParser.IDENT)
            self.state = 123
            self.match(SwagLangParser.L_PAREN)
            self.state = 132
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 124
                self.param_decl()
                self.state = 129
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==24:
                    self.state = 125
                    self.match(SwagLangParser.COMMA)
                    self.state = 126
                    self.param_decl()
                    self.state = 131
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 134
            self.match(SwagLangParser.R_PAREN)
            self.state = 135
            self.code_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(SwagLangParser.TYPE, 0)

        def L_PAREN(self):
            return self.getToken(SwagLangParser.L_PAREN, 0)

        def IDENT(self):
            return self.getToken(SwagLangParser.IDENT, 0)

        def COMMA(self):
            return self.getToken(SwagLangParser.COMMA, 0)

        def R_PAREN(self):
            return self.getToken(SwagLangParser.R_PAREN, 0)

        def getRuleIndex(self):
            return SwagLangParser.RULE_return_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturn_type" ):
                listener.enterReturn_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturn_type" ):
                listener.exitReturn_type(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_type" ):
                return visitor.visitReturn_type(self)
            else:
                return visitor.visitChildren(self)




    def return_type(self):

        localctx = SwagLangParser.Return_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_return_type)
        try:
            self.state = 143
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 137
                self.match(SwagLangParser.TYPE)
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 2)
                self.state = 138
                self.match(SwagLangParser.L_PAREN)
                self.state = 139
                self.match(SwagLangParser.IDENT)
                self.state = 140
                self.match(SwagLangParser.COMMA)
                self.state = 141
                self.match(SwagLangParser.TYPE)
                self.state = 142
                self.match(SwagLangParser.R_PAREN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DataContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(SwagLangParser.INT, 0)

        def STRING(self):
            return self.getToken(SwagLangParser.STRING, 0)

        def FLOAT(self):
            return self.getToken(SwagLangParser.FLOAT, 0)

        def BOOL(self):
            return self.getToken(SwagLangParser.BOOL, 0)

        def list_(self):
            return self.getTypedRuleContext(SwagLangParser.ListContext,0)


        def dict_(self):
            return self.getTypedRuleContext(SwagLangParser.DictContext,0)


        def getRuleIndex(self):
            return SwagLangParser.RULE_data

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterData" ):
                listener.enterData(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitData" ):
                listener.exitData(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitData" ):
                return visitor.visitData(self)
            else:
                return visitor.visitChildren(self)




    def data(self):

        localctx = SwagLangParser.DataContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_data)
        try:
            self.state = 151
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [50]:
                self.enterOuterAlt(localctx, 1)
                self.state = 145
                self.match(SwagLangParser.INT)
                pass
            elif token in [49]:
                self.enterOuterAlt(localctx, 2)
                self.state = 146
                self.match(SwagLangParser.STRING)
                pass
            elif token in [51]:
                self.enterOuterAlt(localctx, 3)
                self.state = 147
                self.match(SwagLangParser.FLOAT)
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 4)
                self.state = 148
                self.match(SwagLangParser.BOOL)
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 5)
                self.state = 149
                self.list_()
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 6)
                self.state = 150
                self.dict_()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L_BRACKET(self):
            return self.getToken(SwagLangParser.L_BRACKET, 0)

        def R_BRACKET(self):
            return self.getToken(SwagLangParser.R_BRACKET, 0)

        def data(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SwagLangParser.DataContext)
            else:
                return self.getTypedRuleContext(SwagLangParser.DataContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(SwagLangParser.COMMA)
            else:
                return self.getToken(SwagLangParser.COMMA, i)

        def getRuleIndex(self):
            return SwagLangParser.RULE_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterList" ):
                listener.enterList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitList" ):
                listener.exitList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList" ):
                return visitor.visitList(self)
            else:
                return visitor.visitChildren(self)




    def list_(self):

        localctx = SwagLangParser.ListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.match(SwagLangParser.L_BRACKET)
            self.state = 162
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 3940649676578816) != 0):
                self.state = 154
                self.data()
                self.state = 159
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==24:
                    self.state = 155
                    self.match(SwagLangParser.COMMA)
                    self.state = 156
                    self.data()
                    self.state = 161
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 164
            self.match(SwagLangParser.R_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DictContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L_CURLY(self):
            return self.getToken(SwagLangParser.L_CURLY, 0)

        def R_CURLY(self):
            return self.getToken(SwagLangParser.R_CURLY, 0)

        def NWLN(self, i:int=None):
            if i is None:
                return self.getTokens(SwagLangParser.NWLN)
            else:
                return self.getToken(SwagLangParser.NWLN, i)

        def no_acs_mode_var_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SwagLangParser.No_acs_mode_var_declContext)
            else:
                return self.getTypedRuleContext(SwagLangParser.No_acs_mode_var_declContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(SwagLangParser.COMMA)
            else:
                return self.getToken(SwagLangParser.COMMA, i)

        def getRuleIndex(self):
            return SwagLangParser.RULE_dict

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDict" ):
                listener.enterDict(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDict" ):
                listener.exitDict(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDict" ):
                return visitor.visitDict(self)
            else:
                return visitor.visitChildren(self)




    def dict_(self):

        localctx = SwagLangParser.DictContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_dict)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self.match(SwagLangParser.L_CURLY)
            self.state = 170
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 167
                    self.match(SwagLangParser.NWLN) 
                self.state = 172
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

            self.state = 187
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 173
                self.no_acs_mode_var_decl()
                self.state = 184
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==24:
                    self.state = 174
                    self.match(SwagLangParser.COMMA)
                    self.state = 178
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==52:
                        self.state = 175
                        self.match(SwagLangParser.NWLN)
                        self.state = 180
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 181
                    self.no_acs_mode_var_decl()
                    self.state = 186
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 192
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==52:
                self.state = 189
                self.match(SwagLangParser.NWLN)
                self.state = 194
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 195
            self.match(SwagLangParser.R_CURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class No_acs_mode_var_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(SwagLangParser.IDENT, 0)

        def ASSIGN(self):
            return self.getToken(SwagLangParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(SwagLangParser.ExprContext,0)


        def COLUMN(self):
            return self.getToken(SwagLangParser.COLUMN, 0)

        def TYPE(self):
            return self.getToken(SwagLangParser.TYPE, 0)

        def getRuleIndex(self):
            return SwagLangParser.RULE_no_acs_mode_var_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNo_acs_mode_var_decl" ):
                listener.enterNo_acs_mode_var_decl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNo_acs_mode_var_decl" ):
                listener.exitNo_acs_mode_var_decl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNo_acs_mode_var_decl" ):
                return visitor.visitNo_acs_mode_var_decl(self)
            else:
                return visitor.visitChildren(self)




    def no_acs_mode_var_decl(self):

        localctx = SwagLangParser.No_acs_mode_var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_no_acs_mode_var_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
            self.match(SwagLangParser.IDENT)
            self.state = 200
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==15:
                self.state = 198
                self.match(SwagLangParser.COLUMN)
                self.state = 199
                self.match(SwagLangParser.TYPE)


            self.state = 202
            self.match(SwagLangParser.ASSIGN)
            self.state = 203
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_refContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(SwagLangParser.IDENT, 0)

        def L_BRACKET(self, i:int=None):
            if i is None:
                return self.getTokens(SwagLangParser.L_BRACKET)
            else:
                return self.getToken(SwagLangParser.L_BRACKET, i)

        def R_BRACKET(self, i:int=None):
            if i is None:
                return self.getTokens(SwagLangParser.R_BRACKET)
            else:
                return self.getToken(SwagLangParser.R_BRACKET, i)

        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(SwagLangParser.DOT)
            else:
                return self.getToken(SwagLangParser.DOT, i)

        def var_ref(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SwagLangParser.Var_refContext)
            else:
                return self.getTypedRuleContext(SwagLangParser.Var_refContext,i)


        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(SwagLangParser.INT)
            else:
                return self.getToken(SwagLangParser.INT, i)

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(SwagLangParser.STRING)
            else:
                return self.getToken(SwagLangParser.STRING, i)

        def getRuleIndex(self):
            return SwagLangParser.RULE_var_ref

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar_ref" ):
                listener.enterVar_ref(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar_ref" ):
                listener.exitVar_ref(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_ref" ):
                return visitor.visitVar_ref(self)
            else:
                return visitor.visitChildren(self)




    def var_ref(self):

        localctx = SwagLangParser.Var_refContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_var_ref)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 205
            self.match(SwagLangParser.IDENT)
            self.state = 215
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 213
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [21]:
                        self.state = 206
                        self.match(SwagLangParser.L_BRACKET)
                        self.state = 208
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==49 or _la==50:
                            self.state = 207
                            _la = self._input.LA(1)
                            if not(_la==49 or _la==50):
                                self._errHandler.recoverInline(self)
                            else:
                                self._errHandler.reportMatch(self)
                                self.consume()


                        self.state = 210
                        self.match(SwagLangParser.R_BRACKET)
                        pass
                    elif token in [25]:
                        self.state = 211
                        self.match(SwagLangParser.DOT)
                        self.state = 212
                        self.var_ref()
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 217
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ACCESS_MOD(self):
            return self.getToken(SwagLangParser.ACCESS_MOD, 0)

        def IDENT(self, i:int=None):
            if i is None:
                return self.getTokens(SwagLangParser.IDENT)
            else:
                return self.getToken(SwagLangParser.IDENT, i)

        def ASSIGN(self):
            return self.getToken(SwagLangParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(SwagLangParser.ExprContext,0)


        def COLUMN(self):
            return self.getToken(SwagLangParser.COLUMN, 0)

        def TYPE(self):
            return self.getToken(SwagLangParser.TYPE, 0)

        def COMMA(self):
            return self.getToken(SwagLangParser.COMMA, 0)

        def func_call(self):
            return self.getTypedRuleContext(SwagLangParser.Func_callContext,0)


        def getRuleIndex(self):
            return SwagLangParser.RULE_var_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar_decl" ):
                listener.enterVar_decl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar_decl" ):
                listener.exitVar_decl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_decl" ):
                return visitor.visitVar_decl(self)
            else:
                return visitor.visitChildren(self)




    def var_decl(self):

        localctx = SwagLangParser.Var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_var_decl)
        self._la = 0 # Token type
        try:
            self.state = 232
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 218
                self.match(SwagLangParser.ACCESS_MOD)
                self.state = 219
                self.match(SwagLangParser.IDENT)
                self.state = 222
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==15:
                    self.state = 220
                    self.match(SwagLangParser.COLUMN)
                    self.state = 221
                    self.match(SwagLangParser.TYPE)


                self.state = 224
                self.match(SwagLangParser.ASSIGN)
                self.state = 225
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 226
                self.match(SwagLangParser.ACCESS_MOD)
                self.state = 227
                self.match(SwagLangParser.IDENT)
                self.state = 228
                self.match(SwagLangParser.COMMA)
                self.state = 229
                self.match(SwagLangParser.IDENT)
                self.state = 230
                self.match(SwagLangParser.ASSIGN)
                self.state = 231
                self.func_call()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_assignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_ref(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SwagLangParser.Var_refContext)
            else:
                return self.getTypedRuleContext(SwagLangParser.Var_refContext,i)


        def expr(self):
            return self.getTypedRuleContext(SwagLangParser.ExprContext,0)


        def ASSIGN(self):
            return self.getToken(SwagLangParser.ASSIGN, 0)

        def ADD_ASSIGN(self):
            return self.getToken(SwagLangParser.ADD_ASSIGN, 0)

        def SUB_ASSIGN(self):
            return self.getToken(SwagLangParser.SUB_ASSIGN, 0)

        def MUL_ASSIGN(self):
            return self.getToken(SwagLangParser.MUL_ASSIGN, 0)

        def DIV_ASSIGN(self):
            return self.getToken(SwagLangParser.DIV_ASSIGN, 0)

        def MOD_ASSIGN(self):
            return self.getToken(SwagLangParser.MOD_ASSIGN, 0)

        def COMMA(self):
            return self.getToken(SwagLangParser.COMMA, 0)

        def func_call(self):
            return self.getTypedRuleContext(SwagLangParser.Func_callContext,0)


        def getRuleIndex(self):
            return SwagLangParser.RULE_var_assign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar_assign" ):
                listener.enterVar_assign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar_assign" ):
                listener.exitVar_assign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_assign" ):
                return visitor.visitVar_assign(self)
            else:
                return visitor.visitChildren(self)




    def var_assign(self):

        localctx = SwagLangParser.Var_assignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_var_assign)
        self._la = 0 # Token type
        try:
            self.state = 244
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 234
                self.var_ref()
                self.state = 235
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4227858432) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 236
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 238
                self.var_ref()
                self.state = 239
                self.match(SwagLangParser.COMMA)
                self.state = 240
                self.var_ref()
                self.state = 241
                self.match(SwagLangParser.ASSIGN)
                self.state = 242
                self.func_call()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Conditional_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def code_block(self):
            return self.getTypedRuleContext(SwagLangParser.Code_blockContext,0)


        def getRuleIndex(self):
            return SwagLangParser.RULE_conditional_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditional_body" ):
                listener.enterConditional_body(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditional_body" ):
                listener.exitConditional_body(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConditional_body" ):
                return visitor.visitConditional_body(self)
            else:
                return visitor.visitChildren(self)




    def conditional_body(self):

        localctx = SwagLangParser.Conditional_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_conditional_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 246
            self.code_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Loop_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def code_block(self):
            return self.getTypedRuleContext(SwagLangParser.Code_blockContext,0)


        def getRuleIndex(self):
            return SwagLangParser.RULE_loop_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoop_body" ):
                listener.enterLoop_body(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoop_body" ):
                listener.exitLoop_body(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoop_body" ):
                return visitor.visitLoop_body(self)
            else:
                return visitor.visitChildren(self)




    def loop_body(self):

        localctx = SwagLangParser.Loop_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_loop_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 248
            self.code_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LoopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def for_loop(self):
            return self.getTypedRuleContext(SwagLangParser.For_loopContext,0)


        def while_loop(self):
            return self.getTypedRuleContext(SwagLangParser.While_loopContext,0)


        def do_while_loop(self):
            return self.getTypedRuleContext(SwagLangParser.Do_while_loopContext,0)


        def getRuleIndex(self):
            return SwagLangParser.RULE_loop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoop" ):
                listener.enterLoop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoop" ):
                listener.exitLoop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoop" ):
                return visitor.visitLoop(self)
            else:
                return visitor.visitChildren(self)




    def loop(self):

        localctx = SwagLangParser.LoopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_loop)
        try:
            self.state = 253
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 250
                self.for_loop()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 251
                self.while_loop()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 3)
                self.state = 252
                self.do_while_loop()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_loopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(SwagLangParser.WHILE, 0)

        def condition(self):
            return self.getTypedRuleContext(SwagLangParser.ConditionContext,0)


        def loop_body(self):
            return self.getTypedRuleContext(SwagLangParser.Loop_bodyContext,0)


        def getRuleIndex(self):
            return SwagLangParser.RULE_while_loop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile_loop" ):
                listener.enterWhile_loop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile_loop" ):
                listener.exitWhile_loop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile_loop" ):
                return visitor.visitWhile_loop(self)
            else:
                return visitor.visitChildren(self)




    def while_loop(self):

        localctx = SwagLangParser.While_loopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_while_loop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 255
            self.match(SwagLangParser.WHILE)
            self.state = 256
            self.condition()
            self.state = 257
            self.loop_body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Do_while_loopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DO(self):
            return self.getToken(SwagLangParser.DO, 0)

        def loop_body(self):
            return self.getTypedRuleContext(SwagLangParser.Loop_bodyContext,0)


        def WHILE(self):
            return self.getToken(SwagLangParser.WHILE, 0)

        def L_PAREN(self):
            return self.getToken(SwagLangParser.L_PAREN, 0)

        def condition(self):
            return self.getTypedRuleContext(SwagLangParser.ConditionContext,0)


        def R_PAREN(self):
            return self.getToken(SwagLangParser.R_PAREN, 0)

        def getRuleIndex(self):
            return SwagLangParser.RULE_do_while_loop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDo_while_loop" ):
                listener.enterDo_while_loop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDo_while_loop" ):
                listener.exitDo_while_loop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDo_while_loop" ):
                return visitor.visitDo_while_loop(self)
            else:
                return visitor.visitChildren(self)




    def do_while_loop(self):

        localctx = SwagLangParser.Do_while_loopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_do_while_loop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 259
            self.match(SwagLangParser.DO)
            self.state = 260
            self.loop_body()
            self.state = 261
            self.match(SwagLangParser.WHILE)
            self.state = 262
            self.match(SwagLangParser.L_PAREN)
            self.state = 263
            self.condition()
            self.state = 264
            self.match(SwagLangParser.R_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_loopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def loop_body(self):
            return self.getTypedRuleContext(SwagLangParser.Loop_bodyContext,0)


        def FOR(self):
            return self.getToken(SwagLangParser.FOR, 0)

        def forin(self):
            return self.getTypedRuleContext(SwagLangParser.ForinContext,0)


        def SEMICOL(self, i:int=None):
            if i is None:
                return self.getTokens(SwagLangParser.SEMICOL)
            else:
                return self.getToken(SwagLangParser.SEMICOL, i)

        def no_acs_mode_var_decl(self):
            return self.getTypedRuleContext(SwagLangParser.No_acs_mode_var_declContext,0)


        def condition(self):
            return self.getTypedRuleContext(SwagLangParser.ConditionContext,0)


        def expr(self):
            return self.getTypedRuleContext(SwagLangParser.ExprContext,0)


        def getRuleIndex(self):
            return SwagLangParser.RULE_for_loop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor_loop" ):
                listener.enterFor_loop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor_loop" ):
                listener.exitFor_loop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_loop" ):
                return visitor.visitFor_loop(self)
            else:
                return visitor.visitChildren(self)




    def for_loop(self):

        localctx = SwagLangParser.For_loopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_for_loop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 279
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.state = 266
                self.match(SwagLangParser.FOR)

                self.state = 268
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==14:
                    self.state = 267
                    self.no_acs_mode_var_decl()


                self.state = 270
                self.match(SwagLangParser.SEMICOL)
                self.state = 272
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 3940666856595456) != 0):
                    self.state = 271
                    self.condition()


                self.state = 274
                self.match(SwagLangParser.SEMICOL)
                self.state = 276
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
                if la_ == 1:
                    self.state = 275
                    self.expr(0)


                pass

            elif la_ == 2:
                self.state = 278
                self.forin()
                pass


            self.state = 281
            self.loop_body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForinContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(SwagLangParser.FOR, 0)

        def IDENT(self):
            return self.getToken(SwagLangParser.IDENT, 0)

        def IN(self):
            return self.getToken(SwagLangParser.IN, 0)

        def func_call(self):
            return self.getTypedRuleContext(SwagLangParser.Func_callContext,0)


        def var_ref(self):
            return self.getTypedRuleContext(SwagLangParser.Var_refContext,0)


        def getRuleIndex(self):
            return SwagLangParser.RULE_forin

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForin" ):
                listener.enterForin(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForin" ):
                listener.exitForin(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForin" ):
                return visitor.visitForin(self)
            else:
                return visitor.visitChildren(self)




    def forin(self):

        localctx = SwagLangParser.ForinContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_forin)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 283
            self.match(SwagLangParser.FOR)
            self.state = 284
            self.match(SwagLangParser.IDENT)
            self.state = 285
            self.match(SwagLangParser.IN)
            self.state = 288
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.state = 286
                self.func_call()
                pass

            elif la_ == 2:
                self.state = 287
                self.var_ref()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(SwagLangParser.IF, 0)

        def condition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SwagLangParser.ConditionContext)
            else:
                return self.getTypedRuleContext(SwagLangParser.ConditionContext,i)


        def conditional_body(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SwagLangParser.Conditional_bodyContext)
            else:
                return self.getTypedRuleContext(SwagLangParser.Conditional_bodyContext,i)


        def ELSE_IF(self, i:int=None):
            if i is None:
                return self.getTokens(SwagLangParser.ELSE_IF)
            else:
                return self.getToken(SwagLangParser.ELSE_IF, i)

        def ELSE(self):
            return self.getToken(SwagLangParser.ELSE, 0)

        def getRuleIndex(self):
            return SwagLangParser.RULE_conditional

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditional" ):
                listener.enterConditional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditional" ):
                listener.exitConditional(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConditional" ):
                return visitor.visitConditional(self)
            else:
                return visitor.visitChildren(self)




    def conditional(self):

        localctx = SwagLangParser.ConditionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_conditional)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 290
            self.match(SwagLangParser.IF)
            self.state = 291
            self.condition()
            self.state = 292
            self.conditional_body()
            self.state = 299
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 293
                self.match(SwagLangParser.ELSE_IF)
                self.state = 294
                self.condition()
                self.state = 295
                self.conditional_body()
                self.state = 301
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 304
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 302
                self.match(SwagLangParser.ELSE)
                self.state = 303
                self.conditional_body()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(SwagLangParser.ExprContext,0)


        def getRuleIndex(self):
            return SwagLangParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition" ):
                return visitor.visitCondition(self)
            else:
                return visitor.visitChildren(self)




    def condition(self):

        localctx = SwagLangParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 306
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L_PAREN(self):
            return self.getToken(SwagLangParser.L_PAREN, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SwagLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(SwagLangParser.ExprContext,i)


        def R_PAREN(self):
            return self.getToken(SwagLangParser.R_PAREN, 0)

        def data(self):
            return self.getTypedRuleContext(SwagLangParser.DataContext,0)


        def func_call(self):
            return self.getTypedRuleContext(SwagLangParser.Func_callContext,0)


        def var_ref(self):
            return self.getTypedRuleContext(SwagLangParser.Var_refContext,0)


        def INC(self):
            return self.getToken(SwagLangParser.INC, 0)

        def DEC(self):
            return self.getToken(SwagLangParser.DEC, 0)

        def NOT(self):
            return self.getToken(SwagLangParser.NOT, 0)

        def EXP(self):
            return self.getToken(SwagLangParser.EXP, 0)

        def MUL(self):
            return self.getToken(SwagLangParser.MUL, 0)

        def DIV(self):
            return self.getToken(SwagLangParser.DIV, 0)

        def MOD(self):
            return self.getToken(SwagLangParser.MOD, 0)

        def PLUS(self):
            return self.getToken(SwagLangParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(SwagLangParser.MINUS, 0)

        def GT(self):
            return self.getToken(SwagLangParser.GT, 0)

        def LT(self):
            return self.getToken(SwagLangParser.LT, 0)

        def EQ(self):
            return self.getToken(SwagLangParser.EQ, 0)

        def GTE(self):
            return self.getToken(SwagLangParser.GTE, 0)

        def LTE(self):
            return self.getToken(SwagLangParser.LTE, 0)

        def NEQ(self):
            return self.getToken(SwagLangParser.NEQ, 0)

        def AND(self):
            return self.getToken(SwagLangParser.AND, 0)

        def OR(self):
            return self.getToken(SwagLangParser.OR, 0)

        def QUESTION(self):
            return self.getToken(SwagLangParser.QUESTION, 0)

        def COLUMN(self):
            return self.getToken(SwagLangParser.COLUMN, 0)

        def getRuleIndex(self):
            return SwagLangParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SwagLangParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 56
        self.enterRecursionRule(localctx, 56, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 321
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.state = 309
                self.match(SwagLangParser.L_PAREN)
                self.state = 310
                self.expr(0)
                self.state = 311
                self.match(SwagLangParser.R_PAREN)
                pass

            elif la_ == 2:
                self.state = 313
                self.data()
                pass

            elif la_ == 3:
                self.state = 314
                self.func_call()
                pass

            elif la_ == 4:
                self.state = 315
                self.var_ref()
                pass

            elif la_ == 5:
                self.state = 316
                self.var_ref()
                self.state = 317
                _la = self._input.LA(1)
                if not(_la==39 or _la==40):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 6:
                self.state = 319
                self.match(SwagLangParser.NOT)
                self.state = 320
                self.expr(8)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 349
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,35,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 347
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
                    if la_ == 1:
                        localctx = SwagLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 323
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 324
                        self.match(SwagLangParser.EXP)
                        self.state = 325
                        self.expr(7)
                        pass

                    elif la_ == 2:
                        localctx = SwagLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 326
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 327
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 481036337152) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 328
                        self.expr(7)
                        pass

                    elif la_ == 3:
                        localctx = SwagLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 329
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 330
                        _la = self._input.LA(1)
                        if not(_la==47 or _la==48):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 331
                        self.expr(6)
                        pass

                    elif la_ == 4:
                        localctx = SwagLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 332
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 333
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 138538465099776) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 334
                        self.expr(5)
                        pass

                    elif la_ == 5:
                        localctx = SwagLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 335
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 336
                        self.match(SwagLangParser.AND)
                        self.state = 337
                        self.expr(4)
                        pass

                    elif la_ == 6:
                        localctx = SwagLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 338
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 339
                        self.match(SwagLangParser.OR)
                        self.state = 340
                        self.expr(3)
                        pass

                    elif la_ == 7:
                        localctx = SwagLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 341
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 342
                        self.match(SwagLangParser.QUESTION)
                        self.state = 343
                        self.expr(0)
                        self.state = 344
                        self.match(SwagLangParser.COLUMN)
                        self.state = 345
                        self.expr(2)
                        pass

             
                self.state = 351
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,35,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Func_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(SwagLangParser.IDENT, 0)

        def L_PAREN(self):
            return self.getToken(SwagLangParser.L_PAREN, 0)

        def params(self):
            return self.getTypedRuleContext(SwagLangParser.ParamsContext,0)


        def R_PAREN(self):
            return self.getToken(SwagLangParser.R_PAREN, 0)

        def getRuleIndex(self):
            return SwagLangParser.RULE_func_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc_call" ):
                listener.enterFunc_call(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc_call" ):
                listener.exitFunc_call(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_call" ):
                return visitor.visitFunc_call(self)
            else:
                return visitor.visitChildren(self)




    def func_call(self):

        localctx = SwagLangParser.Func_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_func_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 352
            self.match(SwagLangParser.IDENT)
            self.state = 353
            self.match(SwagLangParser.L_PAREN)
            self.state = 354
            self.params()
            self.state = 355
            self.match(SwagLangParser.R_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(SwagLangParser.IDENT, 0)

        def COLUMN(self):
            return self.getToken(SwagLangParser.COLUMN, 0)

        def TYPE(self):
            return self.getToken(SwagLangParser.TYPE, 0)

        def getRuleIndex(self):
            return SwagLangParser.RULE_param_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParam_decl" ):
                listener.enterParam_decl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParam_decl" ):
                listener.exitParam_decl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_decl" ):
                return visitor.visitParam_decl(self)
            else:
                return visitor.visitChildren(self)




    def param_decl(self):

        localctx = SwagLangParser.Param_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_param_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 357
            self.match(SwagLangParser.IDENT)
            self.state = 358
            self.match(SwagLangParser.COLUMN)
            self.state = 359
            self.match(SwagLangParser.TYPE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SwagLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(SwagLangParser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(SwagLangParser.COMMA)
            else:
                return self.getToken(SwagLangParser.COMMA, i)

        def getRuleIndex(self):
            return SwagLangParser.RULE_params

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParams" ):
                listener.enterParams(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParams" ):
                listener.exitParams(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParams" ):
                return visitor.visitParams(self)
            else:
                return visitor.visitChildren(self)




    def params(self):

        localctx = SwagLangParser.ParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_params)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 369
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 3940666856595456) != 0):
                self.state = 361
                self.expr(0)
                self.state = 366
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==24:
                    self.state = 362
                    self.match(SwagLangParser.COMMA)
                    self.state = 363
                    self.expr(0)
                    self.state = 368
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[28] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 1)
         




