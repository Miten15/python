#wap to perform ad , sub , mul and div on 2 matrix
import numpy as np

# Define the matrices
matrix1 = np.array([
    [1, 2],
    [3, 4]
])
matrix2 = np.array([
    [12, 22],
    [32, 42]
])

# Perform operations
add = matrix1 + matrix2  # Addition
sub = matrix1 - matrix2  # Subtraction
mul = matrix1 * matrix2 
mul2 = matrix1 @ matrix2 
#np.matmul(matrix1, matrix2)
div = matrix1 / matrix2  # Element-wise division

# Print the results
print(f"Addition of 2 matrices:\n{add}\n")
print(f"Subtraction of 2 matrices:\n{sub}\n")
print(f"Element-wise multiplication of 2 matrices:\n{mul}\n")
print(f"(2nd way )Element-wise multiplication of 2 matrices:\n{mul2}\n")
print(f"Element-wise division of 2 matrices:\n{div}\n")
