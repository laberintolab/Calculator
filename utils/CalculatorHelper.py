# CalculatorHelper.py
from calculator import Calculator

class CalculatorHelper:
    def __init__(self):
        self.calc = Calculator.Calculator()

    def process_expression(self, resultado: str):
        resultado = resultado.strip() # (strip) elimina los espacios
        # Unary square root prefix
        if resultado.startswith('√'):
            try:
                num_str = resultado[1:].strip()
                x = float(num_str)
                return self.calc.square_root(x)
            except ValueError:
                return "Invalid input for square root."

        # Trigonometric functions prefix
        for func in ['sin', 'cos', 'tan']:
            if resultado.startswith(func):
                try:
                    angle_str = resultado[len(func):].strip()
                    angle = float(angle_str)
                    return self.calc.trig_func(func, angle)
                except ValueError:
                    return f"Invalid input for {func}."

        # Binary operators (simple left-to-right parsing)
        for op in ['^', '+', '-', '*', '/']:
            if op in resultado:
                parts = resultado.split(op)
                if len(parts) != 2:
                    return "Invalid expression."
                try:
                    x = float(parts[0].strip())
                    y = float(parts[1].strip())
                except ValueError:
                    return "Invalid numbers."
                if op == '+':
                    return self.calc.add(x, y)
                elif op == '-':
                    return self.calc.subtract(x, y)
                elif op == '*':
                    return self.calc.multiply(x, y)
                elif op == '/':
                    return self.calc.divide(x, y)
                elif op == '^':
                    return self.calc.exponent(x, y)

        # If no operator, parse as float
        try:
            return float(resultado)
        except ValueError:
            return "Invalid input."
