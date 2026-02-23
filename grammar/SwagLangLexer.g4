lexer grammar SwagLangLexer;

// Keywords
TYPE       : ('int' | 'float' | 'string' | 'bool') ('[]')? | 'void';
IF         : 'if';
ELSE_IF    : 'else' SPACE+ 'if';
ELSE       : 'else';
FOR        : 'for';
IN         : 'in';
WHILE      : 'while';
DO         : 'do';
BREAK      : 'break';
RETURN     : 'return';
DEFER      : 'defer';
ACCESS_MOD : 'const' | 'let';
BOOL       : 'true' | 'false';

IDENT: [a-zA-Z]+;

// Punctuation
COLUMN    : ':';
SEMICOL   : ';';
L_PAREN   : '(';
R_PAREN   : ')';
L_CURLY   : '{';
R_CURLY   : '}';
L_BRACKET : '[';
R_BRACKET : ']';
QUESTION  : '?';
COMMA     : ',';
DOT       : '.';

// Operators
ASSIGN     : '=';
ADD_ASSIGN : '+=';
SUB_ASSIGN : '-=';
MUL_ASSIGN : '*=';
DIV_ASSIGN : '/=';
MOD_ASSIGN : '%=';
AND        : '&&';
OR         : '||';
NOT        : '!';
EXP        : '**';
MUL        : '*';
DIV        : '/';
MOD        : '%';
INC        : '++';
DEC        : '--';
GT         : '>';
LT         : '<';
EQ         : '==';
NEQ        : '!=';
GTE        : '>=';
LTE        : '<=';
PLUS       : '+';
MINUS      : '-';

// Literals
STRING : '"' ( ~["\\\r\n] | '\\' . )* '"';
INT    : '-'?[0-9]+;
FLOAT  : '-'?[0-9]* '.' [0-9]+;

// Hidden tokens
NWLN           : '\r'? '\n';
SPACE          : (' '|'\r'|'\t'|'\u000C')+ -> skip;
COMMENT        : '/*' .*? '*/' -> channel(HIDDEN);
INLINE_COMMENT : '//' ~[\r\n]* -> channel(HIDDEN);
