# frontend file
import tkinter as tk
from tkinter import messagebox

from backend import Calculator

class GUI_Calculator:
    def __init__(self):
        self.calculator = Calculator()
        self.root = tk.Tk()
        self.root.title("Simple Calculator")
        self.create_widgets()

    def create_widgets(self):
        # label for operation selection
        operation_label = tk.Label(self.root, text= "Choose one mathematical operation")
        operation_label.pack

        # buttons for each operations
        add_button = tk.Button(self.root, text = "+", command = lambda: self.set_operation("+"))
        add_button.pack(side = tk.LEFT)
        subtract_button = tk.Button(self.root, text = "-", command = lambda: self.set_operation("-"))
        subtract_button.pack(side = tk.LEFT)
        multiply_button = tk.Button(self.root, text = "x", command = lambda: self.set_operation("*"))
        multiply_button.pack(side = tk.LEFT)
        divide_button = tk.Button(self.root, text = "÷", command = lambda: self.set_operation("/"))
        divide_button.pack(side = tk.LEFT)

        # entry fields for number 1 and number 2
        self.num1_entry = tk.Entry(self.root)
        self.num1_entry.pack()
        self.num2_entry = tk.Entry(self.root)
        self.num2_entry.pack()

        # button to calculate
        calculate_button = tk.Button(self.root, text = "Calculate", command = self.calculate)
        calculate_button.pack()

        # displaying result label
        self.result_label = tk.Label(self.root)
        self.result_label.pack()

    def run_calculator(self):
        self.root.mainloop()

    def set_operation(self, operation):
        self.calculator.selected_operation = operation

    def calculate(self):
        try:
            self.calculator.perform_calculation()
            result = self.calculator.get_result()
            self.display_result(result)
        except ValueError as error:
            messagebox.showerror("Error, Invalid expression", str(error))
        except ZeroDivisionError as error:
            messagebox.showerror("Error, You cannot divide by zero", str(error))

    def display_result(self, result):
        self.result_label.config(text = "The result is {}".format(result))

if __name__ == "__main__":
    calculator_gui = GUI_Calculator()
    calculator_gui.run_calculator()


    