# ALDAY, Gerikah L.
# BSCPE 1-5

# frontend file of the program

# import necessary modules and classes
import tkinter as tk
from tkinter import messagebox
from backend import Calculator

# creating class GUI_Calculator
class GUI_Calculator:
    def __init__(self, Calculator):
        self.calculator = Calculator()
        self.root = tk.Tk()
        self.root.geometry("500x300")
        self.root.resizable(0, 0)
        self.root.title("Simple Calculator")
        self.create_widgets()

    # creating widgets for the GUI
    def create_widgets(self):
        # label for operation selection
        operation_label = tk.Label(self.root, text="Choose one mathematical operation", font=("Poppins", 12))
        operation_label.grid(row=3, columnspan=4, padx=10, pady=10)

    # buttons for each operation
        # addition 
        add_button = tk.Button(self.root, text="+", command=lambda: self.set_operation("+"), font=("Poppins", 15, "bold"), width=8)
        add_button.grid(row=4, column=0, padx=10, pady=10)
        # subtraction
        subtract_button = tk.Button(self.root, text="-", command=lambda: self.set_operation("-"), font=("Poppins", 15, "bold"), width=8)
        subtract_button.grid(row=4, column=1, padx=10, pady=10)
        # multiplication
        multiply_button = tk.Button(self.root, text="x", command=lambda: self.set_operation("*"), font=("Poppins", 15, "bold"), width=8)
        multiply_button.grid(row=4, column=2, padx=10, pady=10)
        # division
        divide_button = tk.Button(self.root, text="÷", command=lambda: self.set_operation("/"), font=("Poppins", 15, "bold"), width=8)
        divide_button.grid(row=4, column=3, padx=10, pady=10)

        # entry fields for number 1 and number 2
        self.num1_entry = tk.Entry(self.root)
        self.num1_entry.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

        self.num2_entry = tk.Entry(self.root)
        self.num2_entry.grid(row=2, column=0, columnspan=4, padx=10, pady=10)

        # button to calculate
        calculate_button = tk.Button(self.root, text="Calculate", command=self.calculate, font=("Poppins", 15, "bold"), width=10)
        calculate_button.grid(row=6, columnspan=4, padx=10, pady=10)

        # displaying result label
        self.result_label = tk.Label(self.root)
        self.result_label.grid(row=5, columnspan=4, padx=10, pady=10)

    
    def run_calculator(self):
        # main loop to run teh calculator GUI
        self.root.mainloop()

    def set_operation(self, operation):
        # set the selected operation 
        self.calculator.selected_operation = operation

    def calculate(self):
        try:
            # attempt to perform the calculation
            self.calculator.number_1 = float(self.num1_entry.get())
            self.calculator.number_2 = float(self.num2_entry.get())
            self.calculator.perform_calculation()
            result = self.calculator.get_result()
            self.display_result(result)
            self.ask_try_again()
        except ValueError as error:
            # display an error message if the input is invalid
            messagebox.showerror("Error, Invalid expression", str(error))
        except ZeroDivisionError as error:
            # display error message if division by zero occurs
            messagebox.showerror("Error, You cannot divide by zero", str(error))

    
    def display_result(self, result):
        # display the result on the GUI
        self.result_label.config(text="The result is {}".format(result), font = ("Poppins", 12, "bold"), foreground="violet")

    def ask_try_again(self):
        # ask the user if they want to perform another calculation
        answer = messagebox.askyesno("Try Again", "Do you want to perform another calculation?")
        if answer:
            # clear the input fields and result label if the user wants to try again
            self.num1_entry.delete(0, tk.END)
            self.num2_entry.delete(0, tk.END)
            self.result_label.config(text="")
        else:
            # display a final message and disable the input fields before quitting the GUI
            self.result_label.config(text="Thank you for using this calculator")
            self.num1_entry.config(state="disabled")
            self.num2_entry.config(state="disabled")
            self.root.after(2000, self.root.quit)

if __name__ == "__main__":
    # instance of the GUI calculator and run it
    calculator_gui = GUI_Calculator(Calculator)
    calculator_gui.run_calculator()
