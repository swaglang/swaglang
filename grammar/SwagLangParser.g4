parser grammar SwagLangParser;

options {
    tokenVocab = SwagLangLexer;
}

prog
    : stmts EOF
    ;

// TODO: deal with NWLN statement junk
stmts
    : (stmt | NWLN)*
    ;

stmt
    : pure_stmt
    ;

pure_stmt
    : func_decl
    | var_decl
    ;

code_block
    : L_CURLY (func_stmt NWLN)* R_CURLY
    ;

func_stmt
    : pure_func_stmt?
    ;

pure_func_stmt
    : func_decl
    | var_assign
    | func_call
    | var_decl
    | loop
    | conditional
    | break
    | return
    | defer
    | expr
    ;

defer
    : DEFER expr
    ;

break
    : BREAK
    ;

return
    : RETURN
    | RETURN expr
    | RETURN expr COMMA expr
    ;

func_decl
    : return_type IDENT L_PAREN (param_decl)* R_PAREN code_block
    ;

return_type
    : TYPE
    | L_PAREN IDENT COMMA TYPE R_PAREN
    ;

data
    : INT
    | STRING
    | FLOAT
    | BOOL
    | list
    | dict
    // TODO:
    // | set
    ;

list
    // TODO: multi-line lists
    : L_BRACKET (data (COMMA data)*)? R_BRACKET
    ;

dict
    : L_CURLY NWLN* (no_acs_mode_var_decl (COMMA NWLN* no_acs_mode_var_decl)*)? NWLN* R_CURLY
    ;

no_acs_mode_var_decl
    : IDENT (COLUMN TYPE)? ASSIGN expr
    ;

var_ref
    : IDENT ((L_BRACKET (INT | STRING)? R_BRACKET) | (DOT var_ref))*
    ;

var_decl
    : ACCESS_MOD IDENT (COLUMN TYPE)? ASSIGN expr
    | ACCESS_MOD IDENT COMMA IDENT ASSIGN func_call
    ;

var_assign
    : var_ref ( ASSIGN | ADD_ASSIGN | SUB_ASSIGN | MUL_ASSIGN | DIV_ASSIGN | MOD_ASSIGN ) expr
    |  var_ref COMMA var_ref ASSIGN func_call
    ;

conditional_body
    : code_block
    ;

loop_body
    : code_block
    ;

loop
    : for_loop
    | while_loop
    | do_while_loop
    ;

while_loop
    : WHILE condition loop_body
    ;

do_while_loop
    : DO  loop_body  WHILE L_PAREN condition R_PAREN
    ;

for_loop
    : (FOR (no_acs_mode_var_decl? SEMICOL condition? SEMICOL expr? ) | forin) loop_body
    ;

forin
    : FOR IDENT IN (func_call | var_ref )
    ;

conditional
    : IF condition conditional_body (ELSE_IF condition conditional_body)* (ELSE conditional_body)?
    ;

condition
    : expr
    ;

expr
    : L_PAREN expr R_PAREN
    | data
    | func_call
    | var_ref
    | var_ref (INC | DEC)
    | NOT expr
    | <assoc=right> expr EXP expr
    | expr (MUL | DIV | MOD) expr
    | expr (PLUS | MINUS) expr
    | expr (GT | LT | EQ | GTE | LTE | NEQ) expr
    | expr AND expr
    | expr OR expr
    | expr QUESTION expr COLUMN expr
    ;

func_call
    : IDENT L_PAREN params R_PAREN
    ;

param_decl
    : IDENT COLUMN TYPE
    ;

params
    : (expr (COMMA expr )*)?
    ;
