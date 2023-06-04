# import Calculatro class from backend file
from backend import Calculator

# new class for new operations
class Advanced_Calculator(Calculator):
    def __init__(self):
        super().__init__()

    # exponent operation
    def exponent (self, base, exponent):
        self.number_1 = base
        self.number_2 = exponent
        self.selected_operation = "**"
        self.perform_calculation()
        return self.result
    
    # remainder operation
    def remainder(self, dividend, divisor):
        self.number_1 = dividend
        self.number_2 = divisor
        self.selected_operation = "%"
        self.perform_calculation()
        return self.result