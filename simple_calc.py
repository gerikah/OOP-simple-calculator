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
        operation_label = tk.Label(self.root, text= "Choose one mathematical operation")
        operation_label.pack





if __name__ == "__main__":
    calculator = Calculator()
    calculator.run_Calculator()

    