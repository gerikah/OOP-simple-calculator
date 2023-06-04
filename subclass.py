from backend import Calculator
 
class Advanced_Calculator(Calculator):
    def __init__(self):
        super().__init__()

    def exponent (self, base, exponent):
        self.number_1 = base
        self.number_2 = exponent
        self.selected_operation = "**"
        self.perform_calculation()
        return self.result
    
    def remainder(self, dividend, divisor):
        