# frontend file

#import module
import tkinter as tk

large_font = ("Poppins", 20, "bold")
small_font = ("Poppins", 15)
digits_font = ("Poppins", 20, "bold")
default_font = ("Poppins", 15)




from back_end import Calculator

if __name__ == "__main__":
    calculator = Calculator()
    calculator.run_Calculator()

    