# ELE527-Guass-Siedelproject
ELE527 Guass-Siedel project
# Gauss-Seidel Solver

The Gauss-Seidel Solver is a Python program that solves a system of linear equations using the Gauss-Seidel iteration method. This program allows users to input the coefficient matrix, the right-hand side vector, the initial guess, and the number of iteration steps to obtain the solution.

## Table of Contents
- [Introduction](#introduction)
- [Requirements](#requirements)
- [Usage](#usage)
- [Example](#example)
- [License](#license)

## Introduction

The Gauss-Seidel iteration is an iterative method used to solve a system of linear equations. It is particularly useful when the coefficient matrix is diagonally dominant or positive definite. The method starts with an initial guess for the solution and iteratively refines the solution until a specified number of steps or a convergence criterion is met.

This program provides a convenient way to apply the Gauss-Seidel iteration method to solve systems of linear equations. It prompts the user to enter the necessary inputs and displays the solution along with the residuals/errors.

## Requirements

- Python 3.x

## Usage

1. Clone the repository or download as zip

2. Open a terminal or command prompt and navigate to the directory containing the `main.py` file.

3. Run the program using the following command: python gauss_seidel.py or use any IDE of your choice
4. Follow the prompts to enter the coefficient matrix, the right-hand side vector, the initial guess, and the number of iteration steps.

5. The program will solve the system of equations using the Gauss-Seidel method and display the solution.

## Example

Suppose we have the following system of linear equations:
x1 + 9x2 - 2x3 = 36
2x1 - x2 + 8x3 = 121
6x1 + x2 + x3 = 107


We can use the Gauss-Seidel Solver program to find the solution. Here is an example of how to use the program:

Enter the coefficient matrix A:
1 9 -2
2 -1 8
6 1 1
Enter the right-hand side vector b:
36 121 107
Enter the initial guess x0:
0 0 0
Enter the number of iteration steps: 10 (I've hard-coded 10 iterations already, you can un-comment the code in the file)

Solution:
x1 = 1.800000
x2 = 15.466667
x3 = -8.933333

then it converts the solutions to 6 significant figures

In this example, the user enters the coefficient matrix `A`, the right-hand side vector `b`, the initial guess `x0`, and the number of iteration steps as prompted. The program then solves the system of equations using the Gauss-Seidel method and displays the solution. 







