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

class GUI_Calculator:
    def __init__(self):
        self.window = tk.Tk
        self.window.geometry("500x300")
        self.window.resizable(0, 0)
        self.window.title("simple calculator")

        # display frame and labels
        self.display_frame = self.create_display_frame()
        self.total_label, self.label = self.create_display_labels()
        


















from backend import Calculator

if __name__ == "__main__":
    calculator = Calculator()
    calculator.run_Calculator()

    