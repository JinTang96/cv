# import library
import numpy as np 

# define the coefficient of the equation
A = np.array([[2, 1, 1], [1, 1, 0], [0, 1, -3]])
B = np.array([2, 2, 1])

# Solve the variables
(X, Y, Z) = np.linalg.solve(A, B)

# Print the variables
print(f'x = {X}')
print(f'y = {Y}')
print(f'z = {Z}')