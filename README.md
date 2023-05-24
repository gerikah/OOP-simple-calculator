## Calculator Program

This program is a simple calculator that performs basic mathematical operations such as addition, subtraction, multiplication, and division. It has a graphical user interface (GUI) built using the Tkinter library.

### Usage
1. Run the program by executing the script.
2. The calculator GUI will open.
3. Enter the first number in the first input field (`num1_entry`).
4. Enter the second number in the second input field (`num2_entry`).
5. Click on one of the mathematical operation buttons (`+`, `-`, `x`, or `÷`) to select the operation.
6. Click the "Calculate" button to perform the calculation.
7. The result will be displayed in the result label (`result_label`).
8. If you want to perform another calculation, click "Try Again" in the message box.
9. If you want to exit the program, click "No" in the message box or close the GUI window.

### Program Structure
The program consists of two files: `backend.py` and `simple_calc.py`.

#### backend.py
This file contains the `Calculator` class, which handles the backend calculations. It initializes the necessary variables and performs the selected mathematical operation. The `perform_calculation()` method performs the calculation based on the selected operation, and the `get_result()` method returns the result.

#### simple_calc.py
This file contains the `GUI_Calculator` class, which handles the GUI of the calculator using Tkinter. It initializes the GUI window and creates the necessary widgets, such as labels, buttons, and entry fields. The `run_calculator()` method starts the main loop to run the calculator GUI. Other methods, such as `set_operation()`, `calculate()`, `display_result()`, and `ask_try_again()`, handle different functionalities of the calculator.

### Dependencies
The program requires the following dependencies:
- Python 3.x
- Tkinter library

### Running the Program
To run the program, follow these steps:
1. Make sure you have Python 3.x installed on your system.
2. Install the Tkinter library if it is not already installed. You can use the command `pip install tk` to install it.
3. Save both `backend.py` and `frontend.py` files in the same directory.
4. Open a terminal or command prompt and navigate to the directory where the files are saved.
5. Run the program by executing the command `python frontend.py`.
6. The calculator GUI will open, and you can start using it as described in the "Usage" section.

Enjoy calculating with the Simple Calculator!
