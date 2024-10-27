grammar Expr;

root : expr EOF;  // Punto de entrada principal

expr
    : expr POW expr              // Potencia
    | expr MULT expr             // Multiplicación
    | expr DIV expr              // División
    | expr MOD expr              // Módulo
    | expr MAS expr              // Suma
    | expr MENOS expr            // Resta
    | expr AND expr              // Operador lógico AND
    | expr OR expr               // Operador lógico OR
    | '(' expr ')'               // Paréntesis
    | NUM                        // Números enteros y decimales
    | BOOL                       // Valores booleanos (0 o 1)
    | VAR                        // Variables simples
    ;

// Tokens
AND   : '&&';         // Operador lógico AND
OR    : '||';         // Operador lógico OR
MAS   : '+';          // Suma
MENOS : '-';          // Resta
MULT  : '*';          // Multiplicación
DIV   : '/';          // División
MOD   : '%';          // Módulo
POW   : '^';          // Potencia
NUM   : [0-9]+ ('.' [0-9]+)?;  // Define números enteros y decimales
BOOL  : '0' | '1';             // Valores booleanos
VAR   : [a-zA-Z];              // Variables representadas por letras
WS    : [ \t\r\n]+ -> skip;    // Ignorar espacios en blanco y saltos de línea