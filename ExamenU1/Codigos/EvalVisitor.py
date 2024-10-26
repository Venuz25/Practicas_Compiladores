# Generated from Expr.g4 by ANTLR 4.13.2
from antlr4 import *

if __name__ is not None and "." in __name__:
    from .ExprParser import ExprParser
    from .ExprVisitor import ExprVisitor
else:
    from ExprParser import ExprParser
    from ExprVisitor import ExprVisitor

# Creando la clase EvalVisitor
class EvalVisitor(ExprVisitor):
    def visitRoot(self, ctx):
        # Evalua la expresion
        res = self.visit(ctx.expr())
        print(f"Resultado de la expresion: {res}")
        return res
    
    def visitExpr(self, ctx):
        # Lista de los hijos de la expresion
        cade = list(ctx.getChildren())
        if len(cade) == 1:
            if cade[0].getText().isdigit() or '.' in cade[0].getText():
                # Si es un numero, lo convierte flotante o entero
                num_text = cade[0].getText()
                if '.' in num_text:
                    return float(num_text)
                else:
                    return int(num_text)
            else:
                # Si es un valor booleano (0 o 1)
                return int(cade[0].getText())
        elif len(cade) == 3 and cade[0].getText() == '(':
            # Caso de parentesis, se evalua la expresion entre ellos
            return self.visit(cade[1])
        elif len(cade) == 4:
            # Multiplicacion implicita antes o despues de los parentesis
            if cade[0].getText() == '(' and cade[2].getText() == ')':
                # Caso: (expr) expr -> Multiplicacion implicita despues del parentesis
                return self.visit(cade[1]) * self.visit(cade[3])
            elif cade[1].getText() == '(' and cade[3].getText() == ')':
                # Caso: expr (expr) -> Multiplicacion implicita antes del parentesis
                return self.visit(cade[0]) * self.visit(cade[2])
        else:
            # Detectar la operacion con el segundo hijo
            op = cade[1].getText()
            if op == '+':
                return self.visit(cade[0]) + self.visit(cade[2])
            elif op == '-':
                return self.visit(cade[0]) - self.visit(cade[2])
            elif op == '*':
                return self.visit(cade[0]) * self.visit(cade[2])
            elif op == '/':
                # Division, verifica no dividir por cero
                divisor = self.visit(cade[2])
                if divisor == 0:
                    raise ZeroDivisionError("Division por cero.")
                return self.visit(cade[0]) / divisor
            elif op == '%':
                #modulo
                return self.visit(cade[0]) % self.visit(cade[2])
            elif op == '^':
                # Potencia
                return self.visit(cade[0]) ** self.visit(cade[2])
            elif op == '&&':
                # Evaluacion AND, solo booleanos
                left = self.visit(cade[0])
                right = self.visit(cade[2])
                if left in [0, 1] and right in [0, 1]:
                    return 1 if left and right else 0
                else:
                    raise ValueError("Operacion logica solo permitida con 0 y 1.")
            elif op == '||':
                # Evaluacion OR, solo booleanos
                left = self.visit(cade[0])
                right = self.visit(cade[2])
                if left in [0, 1] and right in [0, 1]:
                    return 1 if left or right else 0
                else:
                    raise ValueError("Operacion logica solo permitida con 0 y 1.")