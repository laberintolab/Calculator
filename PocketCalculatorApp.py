# PocketCalculatorApp.py
import tkinter as tk
from tkinter import font
from utils import CalculatorHelper

class PocketCalculatorApp:
    def __init__(self, root):
        self.root = root
        root.title("Pocket calculator app")
        root.resizable(False, False)
        self.helper = CalculatorHelper.CalculatorHelper()

        # Set font similar to Windows Calculator
        self.btn_font = font.Font(family='Segoe UI', size=14)
        self.display_font = font.Font(family='Segoe UI', size=24, weight='bold')

        # Display Entry
        self.display = tk.Entry(root, font=self.display_font, bd=0, relief=tk.FLAT, justify='right', bg='#1E1E1E', fg='white', insertbackground='white')
        self.display.grid(row=0, column=0, columnspan=4, sticky='nsew', padx=10, pady=10, ipady=10)
        self.display.focus_set()

        # Button layout inspired by Windows Calculator Standard mode
        buttons = [
            ('C', 1, 0, '#F1707A'), ('√', 1, 1, '#F1707A'), ('^', 1, 2, '#F1707A'), ('/', 1, 3, '#F1707A'),
            ('7', 2, 0, '#3C3C3C'), ('8', 2, 1, '#3C3C3C'), ('9', 2, 2, '#3C3C3C'), ('*', 2, 3, '#F1707A'),
            ('4', 3, 0, '#3C3C3C'), ('5', 3, 1, '#3C3C3C'), ('6', 3, 2, '#3C3C3C'), ('-', 3, 3, '#F1707A'),
            ('1', 4, 0, '#3C3C3C'), ('2', 4, 1, '#3C3C3C'), ('3', 4, 2, '#3C3C3C'), ('+', 4, 3, '#F1707A'),
            ('0', 5, 0, '#3C3C3C'), ('.', 5, 1, '#3C3C3C'), ('=', 5, 2, '#107C10'), ('sin', 5, 3, '#F1707A'),
            ('cos', 6, 3, '#F1707A'), ('tan', 7, 3, '#F1707A')
        ]

        for (text, row, col, color) in buttons:
            btn = tk.Button(root, text=text, bg=color, fg='white', font=self.btn_font, bd=0, relief=tk.FLAT,
                            command=lambda t=text: self.on_button_click(t))
            btn.grid(row=row, column=col, sticky='nsew', padx=1, pady=1, ipadx=10, ipady=15)

        # Configure grid weights for resizing (optional)
        for i in range(8):
            root.grid_rowconfigure(i, weight=1)
        for j in range(4):
            root.grid_columnconfigure(j, weight=1)

        # Keyboard bindings
        root.bind('<Return>', lambda e: self.on_button_click('='))
        root.bind('<KP_Enter>', lambda e: self.on_button_click('='))
        root.bind('<BackSpace>', self.backspace)
        root.bind('<Key>', self.key_input)

    def on_button_click(self, char):
        if char == 'C':
            self.display.delete(0, tk.END)
        elif char == '=':
            self.calculate()
        elif char in ['sin', 'cos', 'tan', '√']:
            # Insert function name with trailing space for parsing
            current = self.display.get()
            if current and not current.endswith(' '):
                self.display.insert(tk.END, ' ')
            self.display.insert(tk.END, char + ' ')
        else:
            self.display.insert(tk.END, char)

    def calculate(self):
        expr = self.display.get()
        result = self.helper.process_expression(expr)
        self.display.delete(0, tk.END)
        self.display.insert(0, str(result))

    def backspace(self, event):
        current = self.display.get()
        if current:
            self.display.delete(len(current)-1, tk.END)

    def key_input(self, event):
        # Allow digits, operators, dot, and letters for trig functions
        allowed_chars = '0123456789.+-*/^ '
        if event.char.lower() in allowed_chars or event.char.lower() in ['s', 'i', 'n', 'c', 'o', 't', 'a', 'r']:
            # Accept input
            return
        else:
            # Ignore other keys
            return "break"

if __name__ == "__main__":
    root = tk.Tk()
    icon = tk.PhotoImage(file="icon.png")
    root.iconphoto(True, icon)
    app = PocketCalculatorApp(root)
    root.mainloop()
