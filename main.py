from roundToSignificantFigures import round_to_significant_figures
from art import logo
import time

# from replit import clear

NUM_OF_ITERATION = 10

print("----------Procedure Programming Design--------")


def gauss_seidel(matrix, rhs, guess, num_of_iteration):
    """
    :param matrix: Coefficient matrix
    :param rhs: Right-hand side vector
    :param guess: Initial guess
    :param num_of_iteration: Number of iteration
    :return: the final solution vector
    """

    no_of_rows = len(matrix)  # number of rows in coefficient matrix
    x = guess.copy()  # a copy of the initial guess

    for step in range(NUM_OF_ITERATION):
        for i in range(no_of_rows):
            # calculates the sum of the products of the coefficients (A[i][j])
            # and the corresponding variables (x[j])
            # for all terms except the diagonal term (A[i][i]).
            # This is represented by the variable s.
            s = sum(matrix[i][j] * x[j] for j in range(no_of_rows) if j != i)
            # The method then updates the i-th element of the x vector by dividing
            # the difference between the right-hand side value (b[i]) and
            # the sum s by the diagonal coefficient (A[i][i]).
            # The result is assigned to x[i].
            x[i] = round_to_significant_figures((rhs[i] - s) / matrix[i][i], 6)

    return x  # returns the final solution vector x.


while True:
    # clear()
    print(logo)  # prints an ASCII generated logo
    choice = input("Do you want to use the Guass-Siedel Program: type 'y' or 'n': ").lower()
    if choice == 'n':
        break

    print("-----------GUASS SIEDEL ITERATION------------")
    time.sleep(1)
    # Accept the coefficient matrix A from the user and turning it into a list
    coefficient_matrix = []
    for num in range(3):
        try:
            # Using the split function on each row to convert to a list
            row = input(f"Enter row {num + 1} of coefficient matrix A: (use whitespace) \n").split()
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

    # Solve the system of equations
    solution = gauss_seidel(coefficient_matrix, rhs_vector, initial_guess, NUM_OF_ITERATION)

    # Print the solution rounded to 6 significant digits
    print("Solution:")
    for num, value in enumerate(solution):
        print(f"x{num + 1} = {value:.6g}")
