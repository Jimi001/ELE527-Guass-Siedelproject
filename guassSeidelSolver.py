class GaussSeidelSolver:
    def __init__(self, matrix, rhs, guess, num_of_iteration):
        self.matrix = matrix
        self.rhs = rhs
        self.guess = guess
        self.num_of_iteration = num_of_iteration
        self.no_of_rows = len(matrix)

    def solve(self):
        x = self.guess.copy()

        for step in range(self.num_of_iteration):
            for i in range(self.no_of_rows):
                s = sum(self.matrix[i][j] * x[j] for j in range(self.no_of_rows) if j != i)
                x[i] = round_to_significant_figures((self.rhs[i] - s) / self.matrix[i][i], 6)

        return x