import tkinter as tk
from tkinter import messagebox
from backend import Calculator


class CalculatorGUI:
    def __init__(self):
        self.calculator = Calculator()

        self.root = tk.Tk()
        self.root.title("Calculator")

        self.create_widgets()

    def create_widgets(self):
        # Label for operation selection
        operation_label = tk.Label(self.root, text="Choose one mathematical operation:")
        operation_label.pack()

        # Dropdown menu for operation selection
        self.operation_var = tk.StringVar(self.root)
        self.operation_var.set(self.calculator.mathematical_operations[0])
        operation_dropdown = tk.OptionMenu(self.root, self.operation_var, *self.calculator.mathematical_operations)
        operation_dropdown.pack()

        # Entry fields for numbers
        self.num1_entry = tk.Entry(self.root)
        self.num1_entry.pack()
        self.num2_entry = tk.Entry(self.root)
        self.num2_entry.pack()

        # Button for calculation
        calculate_button = tk.Button(self.root, text="Calculate", command=self.calculate)
        calculate_button.pack()

        # Label for displaying result
        self.result_label = tk.Label(self.root)
        self.result_label.pack()

    def run(self):
        self.root.mainloop()

    def calculate(self):
        try:
            self.calculator.perform_calculation()
            result = self.calculator.get_result()
            self.display_result(result)

        except ValueError as e:
            messagebox.showerror("Error", str(e))
        except ZeroDivisionError as e:
            messagebox.showerror("Error", str(e))

    def display_result(self, result):
        self.result_label.config(text="The result is {}".format(result))


if __name__ == "__main__":
    calculator_gui = CalculatorGUI()
    calculator_gui.run()

    