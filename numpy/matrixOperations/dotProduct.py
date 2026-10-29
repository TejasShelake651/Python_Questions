import numpy as np

# Matrix Dot Product and Linear Algebra

m1 = np.array([[1, 2], [3, 4]])
m2 = np.array([[5, 6], [7, 8]])

print("Matrix 1:\n", m1)
print("Matrix 2:\n", m2)

# Element-wise multiplication
print("\nElement-wise Multiplication (m1 * m2):\n", m1 * m2)

# Matrix Dot Product (m1 @ m2 or np.dot)
dot_result = np.dot(m1, m2)
print("\nMatrix Dot Product (np.dot(m1, m2)):\n", dot_result)

# Matrix Multiplication using '@' operator
matmul_result = m1 @ m2
print("\nMatrix Multiplication using '@':\n", matmul_result)
