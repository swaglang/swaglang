grammar gr;		
prog:	stmts EOF ;
stmts: (stmt NWLN)* stmt? ;
stmt: pure_stmt? comment? ;

pure_stmt: func_decl 
         | var_decl 
         ;

func_body: func_stmt* ;
func_stmt: func_decl 
         | var_assign 
         | func_call 
         | var_decl 
         | loop 
         | conditional 
         | BREAK
         | RETURN expr
         ;

func_decl: return_type IDENT '(' (param_decl)* ')' 
'{' func_body NWLN? '}' ;
return_type: TYPE
           | '(' ERR_TYPE ',' TYPE ')' ;


comment: START_COMMENT . ;
code_block: '{' stmts '}' ;
var_decl: ACCESS_MOD IDENT COLUMN TYPE '=' expr ;
var_assign: IDENT '=' DATA;

conditional_body: code_block;
loop_body: code_block;

loop: for_loop
    | while_loop
    | do_while_loop
    ;

while_loop: WHILE condition loop_body ;
do_while_loop: DO  loop_body  WHILE '(' condition ')' ;
for_loop: (FOR (var_decl? ';' condition? ';' expr? )
        | forin) loop_body ;
forin: FOR IDENT IN (func_call | IDENT );

conditional: IF condition conditional_body 
            (ELSE_IF condition conditional_body)*
            (ELSE conditional_body)? ;
condition: expr;
expr: expr '**' expr
    | expr ('*'|'/') expr
    | expr ('+'|'-') expr
    | expr (AND | OR | NOT) expr
    | expr ('>' | '<' | '=' | '>=' | '<=') expr
    | func_call
    | DATA
    | IDENT
    |	'(' expr ')'
    ;	
func_call: IDENT '(' params ')' ;
param_decl: IDENT COLUMN TYPE ;
params: (expr (',' expr )*)? ;

START_COMMENT: '#' ; 
TYPE: 'int'
    | 'float'
    | 'string'
    ;
COLUMN: ':' ;
SEMICOL: ';' ;
FOR: 'for' ;
AND: 'and' ;
OR: 'or' ;
NOT: 'not' | '!';
IF: 'if' ;
ELSE_IF: 'else' 'if' ;
IN: 'in' ;
ELSE: 'else' ;
WHILE: 'while' ;
DO: 'do' ;
BREAK: 'break' ;
RETURN: 'return' ;
ACCESS_MOD: 'const' | 'let' ;
KEYWORD: FOR
       | ACCESS_MOD
       | IF
       | ELSE_IF
       | ELSE
       | TYPE
       | RETURN
       ;
DATA: INT
    | STRING
    | FLOAT
    | BOOL
    ;
STRING: '"' ( ~["\\\r\n] | '\\' . )* '"' ;
INT: [0-9]+ ;
FLOAT: [0-9]* '.' [0-9]+ ;
BOOL: 'true'
    | 'false'
    ;

IDENT : [a-zA-Z]+  ; 
ERR_TYPE: IDENT ;

NWLN : '\r'? '\n' ;
SPACE: (' '|'\r'|'\t'|'\u000C')+ -> skip ;
