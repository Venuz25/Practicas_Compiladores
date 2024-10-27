from ExprParser import ExprParser
from ExprVisitor import ExprVisitor

# Creando la clase EvalVisitor
class EvalVisitor(ExprVisitor):
    def __init__(self):
        super().__init__()
        self.variables = {}  # Diccionario para almacenar valores de variables

    def visitRoot(self, ctx):
        # Evalúa la expresión y muestra el resultado
        res = self.visit(ctx.expr())
        print(f"\nResultado de la expresión: {res}\n")
        return res
    
    def visitExpr(self, ctx):
        # Lista de los hijos de la expresión
        cade = list(ctx.getChildren())
        
        if len(cade) == 1:
            # Si es un número, lo convierte a flotante o entero
            num_text = cade[0].getText()
            if num_text.isdigit() or '.' in num_text:
                return float(num_text) if '.' in num_text else int(num_text)
            # Si es un valor booleano (0 o 1)
            elif num_text in ['0', '1']:
                return bool(int(num_text))
            # Si es una variable, solicita el valor al usuario si no está en el diccionario
            elif num_text.isalpha():
                if num_text not in self.variables:
                    valor = input(f"Introduce el valor para la variable '{num_text}': ")
                    # Intentamos convertirlo a número, de lo contrario se considera bool (0 o 1)
                    try:
                        self.variables[num_text] = float(valor) if '.' in valor else int(valor)
                    except ValueError:
                        raise ValueError(f"Valor no válido para la variable '{num_text}'")
                return self.variables[num_text]

        elif len(cade) == 3 and cade[0].getText() == '(':
            # Caso de paréntesis, evalúa la expresión entre ellos
            return self.visit(cade[1])

        # Detectar la operación usando el segundo hijo
        op = cade[1].getText()
        
        if op == '+':
            return self.visit(cade[0]) + self.visit(cade[2])
        elif op == '-':
            return self.visit(cade[0]) - self.visit(cade[2])
        elif op == '*':
            return self.visit(cade[0]) * self.visit(cade[2])
        elif op == '/':
            divisor = self.visit(cade[2])
            if divisor == 0:
                raise ZeroDivisionError("División por cero.")
            return self.visit(cade[0]) / divisor
        elif op == '%':
            return self.visit(cade[0]) % self.visit(cade[2])
        elif op == '^':
            return self.visit(cade[0]) ** self.visit(cade[2])
        elif op == '&&':
            # Evaluación lógica AND, devuelve booleano
            left = self.visit(cade[0])
            right = self.visit(cade[2])
            return bool(left) and bool(right)
        elif op == '||':
            # Evaluación lógica OR, devuelve booleano
            left = self.visit(cade[0])
            right = self.visit(cade[2])
            return bool(left) or bool(right)
