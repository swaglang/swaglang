grammar gr;		

// LEXER
TYPE: ('int' | 'float' | 'string' | 'bool' | 'var') ('[]')? | 'void';
COLUMN: ':' ;
SEMICOL: ';' ;
ASSIGN: '=' ;
ADD_ASSIGN: '+=' ;
SUB_ASSIGN: '-=' ;
MUL_ASSIGN: '*=' ;
DIV_ASSIGN: '/=' ;
MOD_ASSIGN: '%=' ;
// L_BR: '{' ;
// R_BR: '}' ;
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
DEFER: 'defer' ;
ACCESS_MOD: 'const' | 'let' ;
KEYWORD: FOR | ACCESS_MOD | IF | ELSE_IF | ELSE | TYPE | RETURN | DEFER ;
STRING: '"' ( ~["\\\r\n] | '\\' . )* '"' ;
INT: '-'?[0-9]+ ;
FLOAT: '-'?[0-9]* '.' [0-9]+ ;
BOOL: 'true' | 'false' ;
IDENT : [a-zA-Z]+  ; 
// ERR_TYPE: IDENT ;
NWLN : '\r'? '\n' ;
SPACE: (' '|'\r'|'\t'|'\u000C')+ -> skip ;
// TODO: move to parser?

COMMENT: '/*' .*? '*/' -> channel(HIDDEN) ;
INLINE_COMMENT: '//' ~[\r\n]* -> channel(HIDDEN) ; 

// PARSER
prog
:	stmts EOF 
;

// TODO: deal with NWLN statment junk
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
: '{' (func_stmt NWLN)* '}'
;
func_stmt: pure_func_stmt? ;

pure_func_stmt: func_decl 
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
: RETURN expr
| RETURN expr ',' expr
;

func_decl
: return_type IDENT '(' (param_decl)* ')' code_block
;

return_type
: TYPE
| '(' IDENT ',' TYPE ')' 
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
: '[' (data (',' data)*)? ']' 
;

dict
: '{' NWLN* (no_acs_mode_var_decl (',' NWLN* no_acs_mode_var_decl)*)? NWLN* '}' 
;

no_acs_mode_var_decl
: IDENT (COLUMN TYPE)? '=' expr
;

var_ref
: IDENT (('[' (INT | STRING)? ']') | ('.' var_ref))*
;

var_decl
: ACCESS_MOD IDENT (COLUMN TYPE)? '=' expr 
| ACCESS_MOD IDENT ',' IDENT '=' func_call
;

var_assign
: var_ref ( ASSIGN | ADD_ASSIGN | SUB_ASSIGN | MUL_ASSIGN | DIV_ASSIGN | MOD_ASSIGN ) expr
|  var_ref ',' var_ref '=' func_call
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
: DO  loop_body  WHILE '(' condition ')' 
;

for_loop
: (FOR (no_acs_mode_var_decl? ';' condition? ';' expr? ) | forin) loop_body 
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
: expr '**' expr
| expr ('*'|'/') expr
| expr ('+'|'-') expr
| expr (AND | OR | NOT) expr
| expr ('>' | '<' | '==' | '>=' | '<=') expr
| var_ref '++'
| var_ref '--'
| expr '%' expr
| expr '?' expr COLUMN expr
| func_call
| data
| var_ref
|	'(' expr ')'
;	

func_call
: IDENT '(' params ')' 
;

param_decl
: IDENT COLUMN TYPE 
;

params
: (expr (',' expr )*)? 
;
