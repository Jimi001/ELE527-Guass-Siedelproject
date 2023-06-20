from gauss_seidel_solver import GaussSeidelSolver
from get_input import GetInput
from art import logo
import time

# from replit import clear

NUM_OF_ITERATION = 10

print("---------------Object Oriented Design------------------")

user_inputs = GetInput()


def program():
    while True:
        print(logo)  # prints an ASCII generated logo
        choice = input("Do you want to use the Gauss-Seidel Program: type 'y' or 'n': ").lower()
        if choice == 'n':
            break
        print("-----------GAUSS SEIDEL ITERATION------------")
        time.sleep(1)
        coefficient_matrix = user_inputs.get_matrix()
        # Sample Output: Coefficient matrix A = [[1, 9, -2], [2, -1, 8], [6, 1, 1]]
        print(f"Coefficient matrix is {coefficient_matrix}")
        if not coefficient_matrix:
            time.sleep(2)
            clear()
            coefficient_matrix = []
      break
        try:
            rhs_vector = user_inputs.get_rhs_vector()
            if len(coefficient_matrix) != len(rhs_vector):
                print(f"length of the coefficient matrix is not equal to the length of the right-hand side vector")
                time.sleep(2)
                continue
            initial_guess = user_inputs.get_initial_guess()
            # NUM_OF_ITERATION = int(input("Enter the number of iteration steps: "))
        except ValueError as err_message:
            # clear()
            print("HI! you didn't enter an integer or float number")
            print(f"Computer says it {err_message}")
            continue

        # Create an instance of GaussSeidelSolver
        solver = GaussSeidelSolver(coefficient_matrix, rhs_vector, initial_guess, NUM_OF_ITERATION)
        # Solve the system of equations
        solution = solver.solve()

        # Print the solution rounded to 6 significant digits
        print("Solution:")
        for i, value in enumerate(solution):
            print(f"x{i + 1} = {value:.6g}")


program()
