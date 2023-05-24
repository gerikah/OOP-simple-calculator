import tkinter as tk
from tkinter import messagebox

from backend import Calculator

class GUI_Calculator:
    def __init__(self, Calculator):
        self.calculator = Calculator()
        self.root = tk.Tk()
        self.root.geometry("500x300")
        self.root.resizable(0, 0)
        self.root.title("Simple Calculator")
        self.create_widgets()

    def create_widgets(self):
        # label for operation selection
        operation_label = tk.Label(self.root, text="Choose one mathematical operation")
        operation_label.grid(row=0, columnspan=4, padx=10, pady=10)

        # buttons for each operation
        add_button = tk.Button(self.root, text="+", command=lambda: self.set_operation("+"),
                               font=("Poppins", 15, "bold"), width=8)
        add_button.grid(row=1, column=0, padx=10, pady=10)
        subtract_button = tk.Button(self.root, text="-", command=lambda: self.set_operation("-"),
                                    font=("Poppins", 15, "bold"), width=8)
        subtract_button.grid(row=1, column=1, padx=10, pady=10)
        multiply_button = tk.Button(self.root, text="x", command=lambda: self.set_operation("*"),
                                    font=("Poppins", 15, "bold"), width=8)
        multiply_button.grid(row=1, column=2, padx=10, pady=10)
        divide_button = tk.Button(self.root, text="÷", command=lambda: self.set_operation("/"),
                                  font=("Poppins", 15, "bold"), width=8)
        divide_button.grid(row=1, column=3, padx=10, pady=10)

        # entry fields for number 1 and number 2
        self.num1_entry = tk.Entry(self.root)
        self.num1_entry.grid(row=2, column=0, columnspan=4, padx=10, pady=10)
        self.num2_entry = tk.Entry(self.root)
        self.num2_entry.grid(row=3, column=0, columnspan=4, padx=10, pady=10)

        # button to calculate
        calculate_button = tk.Button(self.root, text="Calculate", command=self.calculate,
                                     font=("Poppins", 15, "bold"), width=10)
        calculate_button.grid(row=4, columnspan=4, padx=10, pady=10)

        # displaying result label
        self.result_label = tk.Label(self.root)
        self.result_label.grid(row=5, columnspan=4, padx=10, pady=10)

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
        self.result_label.config(text="The result is {}".format(result))

if __name__ == "__main__":
    calculator_gui = GUI_Calculator(Calculator)
    calculator_gui.run_calculator()
