# frontend file
import tkinter as tk
from tkinter import messagebox

from backend import Calculator

class GUI_Calculator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Simple Calculator")
        self.create_widgets()

    def create_widgets(self):
        # label for operation selection
        operation_label = tk.Label(self.root, text= "Choose one mathematical operation")
        operation_label.pack

        # menu for operation selection
        self.operation_variable = tk.StringVar(self.root)
        self.operation_variable.set(self.calculator.mathematical_opeartions[0])
        
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

    def calculate(self):
        try:
            self.calculator.perform_calculation()
            result = self.calculator.get_result()
            self.display_result(result)
        except ValueError as error:
            messagebox.showerror("Error, Invalid expression", str(error))
        except ZeroDivisionError as error:
            messagebox.showerror("Error, You cannot divide by zero", str(error))





    





if __name__ == "__main__":
    calculator = Calculator()
    calculator.run_Calculator()

    