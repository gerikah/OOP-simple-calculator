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