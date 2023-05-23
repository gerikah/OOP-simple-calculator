# back end file

class Calculator:
    def __init__(self):
        self.mathematical_operations = ["+", "-", "*", "/"]
        self.number_1 = None
        self.number_2 = None
        self.selected_operation = None
        self.result = None

    def run_Calculator(self):
        while True:
            self.get_operation()
            self.get_numbers()
            self.perform_calculation()
            self.display_result()
            if not self.try_again()
                print("Thank you for using this calculator")
                break

    def get_operation(self):
        while True:
            try:
                print("Choose one mathematical operation: ")
                self.selected_operation = input()
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

    def perform_calculation(self):
        try:
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

    def display_result(self):
        if self.result is not None:
            print("The result of {} {} {} is {}".format(self.number_1, self.selected_operation, self.number_2))

    def try_again(self):
        while True:
            try:
                print("Do you want to try again? (yes/no): ")
                answer = input().lower()
                if answer not in ["yes", "no"]:
                    raise ValueError
                break
            except ValueError:
                print("Inavalid input. Please enter 'yes' or 'no'.")
        return answer == "yes"
    