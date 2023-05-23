# back end file

class Calculator:
    def __init__(self):
        self.mathematical_operations = ["+", "-", "*", "/"]
        self.number_1 = None
        self.number_2 = None
        self.selected_operation = None
        self.result = None

    def run_Calculator(self):
    
        self.get_operation()
        self.get_numbers()
        self.perform_calculation()
        self.display_result()
    
    def get_operation(self):
        while True:
            try:
                print("Choose one mathematical operation: ")
                self.selected_operation = input ().strip
                if self.selected_operation not in self.mathematical_operations:
                    raise ValueError
                break
            except ValueError:
                print("Inavalid operation. Please try again.")

    def get_numbers(self):
        try:
            print("Enter the first number: ")
            self.number_1 = float(input())
            print("Enter the second number: ")
            self.number_2 = float(input())
        except ValueError:
            print("Invalid input. Please try again")

calculator = Calculator()
calculator.run_Calculator()