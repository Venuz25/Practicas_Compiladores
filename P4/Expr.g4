grammar Expr;

root : expr EOF;  // define una expresion

expr : expr MAS expr         // Suma
     | expr MENOS expr       // Resta
     | expr MULT expr        // Multiplicacion
     | expr DIV expr         // Division
     | expr POW expr         // Potencia
     | expr MOD expr         // Modulo
     | PAREI expr PARED expr   // Multi implicita despues
     | expr PAREI expr PARED     // Multi implicita antes
     | PAREI expr PARED      // Parentesis normales
     | expr AND expr         // AND logico (booleano)
     | expr OR expr          // OR logico (booleano)
     | NUM                   // Numero normal o flotante
     | BOOL                  // Valor booleano
     ;

AND : '&&' ;     // Operador AND
OR  : '||' ;     // Operador OR

NUM  : [0-9]+ ('.' [0-9]+)? ;  // Define numeros enteros o flotantes
BOOL : '0' | '1' ; // Valores booleanos especificos (0 o 1)
MAS  : '+' ;
MENOS : '-' ;
MULT : '*' ;
DIV  : '/' ;
MOD : '%';
POW  : '^' ;
PAREI : '(' ;
PARED : ')' ;
EQ   : '=' ;
WS   : [ \n]+ -> skip ;


/*
expr: definición de la gramática para la suma y resta de números naturales
skip: indica al escáner que el token WS no debe de llegar al parser
root: para procesar el final del archivo
*/