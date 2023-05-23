# frontend file

#import module
import tkinter as tk

# fonts
large_font = ("Poppins", 20, "bold")
small_font = ("Poppins", 15)
digits_font = ("Poppins", 20, "bold")
default_font = ("Poppins", 15)

# colors
off_white = "#09377B"
white = "#0B69B0"
light_blue = "#F7D507"
light_gray = "#FFFFFF"
label_color = "#000000"



from back_end import Calculator

if __name__ == "__main__":
    calculator = Calculator()
    calculator.run_Calculator()

    