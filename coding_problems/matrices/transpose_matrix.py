def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:

	b = []
	col_len = len(a[0])
	row_len = len(a)

	for col in range(col_len):
		row_elements = []
		for row in range(row_len):
			row_elements.append(a[row][col])

		b.append(row_elements)

	return b

	# on line solution:
	#  [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
