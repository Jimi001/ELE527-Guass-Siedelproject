import time


class GetInput:
    def __init__(self):
        self.initial_guess = None
        self.rhs_vector = []
        self.coefficient_matrix = []

    def get_matrix(self):
        # Accept the coefficient matrix A from the user and turning it into a list
        self.coefficient_matrix = []
        for i in range(3):
            try:
                # Using the split function on each row to convert to a list
                row = input(f"Enter row {i + 1} of coefficient matrix A: (use whitespace) \n").split()
                # converting each item in coefficient matrix A to a float type
                row = list(map(float, row))
            except ValueError as err_message:
                # clear()
                print("HI! you didn't enter an integer or float number")
                print(f"Computer says it {err_message}")
                break
            else:
                if len(row) != 3:
                    time.sleep(1)
                    continue
                # using the append function to append each row of the coefficient matrix to list A
                self.coefficient_matrix.append(row)
        return self.coefficient_matrix

    def get_rhs_vector(self):
        # Accept the right-hand side vector b from the user
        self.rhs_vector = input("Enter the right-hand side vector b: (use whitespace) \n").split()
        # converting each item in list rhs to a float type
        self.rhs_vector = list(map(float, self.rhs_vector))  # Output: [36, 121, 107]
        return self.rhs_vector

    def get_initial_guess(self):
        # Accept the initial guess x0 from the user
        self.initial_guess = input("Enter the initial guess x0: (use whitespace) \n").split()
        if len(self.initial_guess) != 3:
            self.initial_guess = [0, 0, 0]
        # converting each item of the initial guess to a float type
        self.initial_guess = list(map(float, self.initial_guess))  # Initial guess x0 = [0, 0, 0]
        return self.initial_guess
