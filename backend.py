# backend file

class Calculator:
    def __init__(self):
        self.mathematical_operations = ["+", "-", "*", "/"]
        self.number_1 = None
        self.number_2 = None
        self.selected_operation = None
        self.result = None
    
    def perform_calculation(self):
        try:
            self.selected_operation = self.operation_Variable.get()
            self.number_1 = float(self.num1_entry.get())
            self.number_2 = float(self.num2_entry.get())
            
            if self.selected_operation == "+":
                self.result = self.number_1 + self.number_2
            elif self.selected_operation == "-":
                self.result = self.number_1 - self.number_2
            elif self.selected_operation == "*":
                self.result = self.number_1 * self.number_2
            else:
                self.result = self.number_1 / self.number_2            
        except ZeroDivisionError:
            print("Error. You cannot divide by zero.")
            self.result = None
        except ValueError:
            print("Inavalid input. Please enter valid number.")

    def get_result(self):
        return self.result
    
    