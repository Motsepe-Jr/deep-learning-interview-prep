# Matrix times Vector
# Write a Python function that takes the dot product of a matrix and a vector. return -1 if the matrix could not be dotted with the vector

# Example:
# Input:
# a = [[1,2],[2,4]], b = [1,2]
# Output:
# [5, 10]
# Reasoning:
# 1*1 + 2*2 = 5; 1*2+ 2*4 = 10


def matrix_dot_vector(a:list[list[int|float]],b:list[int|float])-> list[int|float]:

	# he dot product between a matrix A (shape 𝑚×𝑛 ) and a vector b (shape 𝑛×1) requires the number of columns in the matrix to match the number of elements in the vector.

	# edge cases
	if len(a) != len(b):
		return -1

	c = [0] * len(a) # always going to return 1D (vector) and 2D (matrix)

	for index, row in enumerate(a):

		mat_row = multiplcation(row, b)

		c[index]  = sum(mat_row)

	return c


def multiplcation(a, b):

	assert len(a) == len(b), print("The matrix row doesnt match thew vector row")
	
	mat_row = [0] * len(a)

	for index in range(len(a)):
		mat_row[index] = a[index] * b[index]

	return mat_row

# Effient Solution: One line use List  Compregension

# return [sum(row[i] * b[i] for i in range(len(b))) for row in a]