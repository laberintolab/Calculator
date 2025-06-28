# Calculator.py
import math

class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y != 0:
            return x / y
        else:
            return "Error! Division by zero."

    def exponent(self, x, y):
        return x ** y

    def square_root(self, x):
        if x >= 0:
            return math.sqrt(x)
        else:
            return "Error! Cannot take the square root of a negative number."

    def trig_func(self, func, angle):
        angle_radians = math.radians(angle)
        if func == 'sin':
            return math.sin(angle_radians)
        elif func == 'cos':
            return math.cos(angle_radians)
        elif func == 'tan':
            return math.tan(angle_radians)
        else:
            return "Invalid trigonometric function."
