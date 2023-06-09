# backend file of the program

class Calculator:
    def __init__(self):
        # list of valid mathematical operations
        self.mathematical_operations = ["+", "-", "*", "/"]
        # setting variables to None
        self.number_1 = None
        self.number_2 = None
        self.selected_operation = None
        self.result = None
    
    def perform_calculation(self):
        try:
            if self.selected_operation == "+": 
                # addition operation
                self.result = self.number_1 + self.number_2
            elif self.selected_operation == "-": 
                # subtraction operation
                self.result = self.number_1 - self.number_2
            elif self.selected_operation == "*": 
                # multiplication operation
                self.result = self.number_1 * self.number_2
            elif self.selected_operation == "/": 
                # division operation
                self.result = self.number_1 / self.number_2  
                if self.number_2 == 0:
                    raise ZeroDivisionError
            elif self.selected_operation == "**":
                # exponent operation
                self.result = self.number_1 ** self.number_2
            else: 
                # remainder operation
                self.selected_operation == "%"
                self.result = self.number_1 % self.number_2
                if self.number_2 == 0:
                    raise ZeroDivisionError
                
        except ZeroDivisionError:
            self.result = None
            raise ZeroDivisionError("Error. You cannot divide by zero.")
            
        except ValueError:
            raise ValueError("Inavalid input. Please enter valid number.")

    def get_result(self):
        return self.result