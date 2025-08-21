def transposeMatrix(matrix):
    # Write your code here.
    new_matrix = []
    new_len = len(matrix[0])

    for i in range(new_len):
        new_matrix.append([None] * len(matrix))

    for row_idx in range(len(new_matrix)):
        for col_idx in range(len(new_matrix[row_idx])):
            new_matrix[row_idx][col_idx] = matrix[col_idx][row_idx]


    return new_matrix
