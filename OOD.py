from guassSeidelSolver import GaussSeidelSolver
from art import logo
import time
# from replit import clear

NUM_OF_ITERATION = 10

print("---------------Object Oriented Design------------------")

while True:
    print(logo)  # prints an ASCII generated logo
    choice = input("Do you want to use the Guass-Siedel Program: type 'y' or 'n': ").lower()
    if choice == 'n':
        break
    print("-----------GUASS SIEDEL ITERATION------------")
    time.sleep(1)
    # Accept the coefficient matrix A from the user and turning it into a list
    coefficient_matrix = []
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
            # using the append function to append each row of the coefficient matrix to list A
            coefficient_matrix.append(row)
    # Sample Output: Coefficient matrix A = [[1, 9, -2], [2, -1, 8], [6, 1, 1]]
    if not coefficient_matrix:
        continue
    print(f"Coefficient matrix is {coefficient_matrix}")

    # Accept the right-hand side vector b from the user
    rhs_vector = input("Enter the right-hand side vector b: (use whitespace) \n").split()
    # converting each item in list rhs to a float type
    rhs_vector = list(map(float, rhs_vector))  # Output: [36, 121, 107]
    if not rhs_vector:
        continue

    # Accept the initial guess x0 from the user
    initial_guess = input("Enter the initial guess x0: (use whitespace) \n").split()
    if not initial_guess:
        initial_guess = [0, 0, 0]
    # converting each item of the initial guess to a float type
    initial_guess = list(map(float, initial_guess))  # Initial guess x0 = [0, 0, 0]

    # NUM_OF_ITERATION = int(input("Enter the number of iteration steps: "))

    # Create an instance of GaussSeidelSolver
    solver = GaussSeidelSolver(coefficient_matrix, rhs_vector, initial_guess, NUM_OF_ITERATION)
    # Solve the system of equations
    solution = solver.solve()

    # Print the solution rounded to 6 significant digits
    print("Solution:")
    for i, value in enumerate(solution):
        print(f"x{i + 1} = {value:.6g}")
