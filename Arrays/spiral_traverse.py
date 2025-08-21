def spiralTraverse(array):
    # Write your code here.
    spiral_array = []
    visited = []

    start_point = [0, 0]
    matrix_width = len(array[0])
    matrix_height = len(array)

    directions = {
        'right' : (0, 1),
        'down' : (1, 0),
        'left': (0, -1),
        'up': (-1, 0)
    }

    row_idx, col_idx = start_point[0], start_point[1]

    for idx in range(matrix_width):
        row_idx, col_idx = [idx, idx]

        spiral_array = traverse(spiral_array,array, visited, directions, row_idx, col_idx, 'right', matrix_width-idx)
        row_idx, col_idx = [idx+1, matrix_width-idx-1]
        spiral_array = traverse(spiral_array,array, visited, directions, row_idx, col_idx, 'down', matrix_height-idx-1)
        row_idx, col_idx = [matrix_height-idx-1,matrix_width-idx-2]
        spiral_array = traverse(spiral_array,array, visited, directions, row_idx, col_idx, 'left', matrix_width-idx-1)
        row_idx, col_idx = [matrix_height-idx-1-1, idx]
        spiral_array = traverse(spiral_array,array, visited, directions, row_idx, col_idx, 'up', matrix_height-idx-1)


    return spiral_array

def traverse(spiral_array, array, visited, directions, row_idx, col_idx, current_direction, n):

    for i in range(n):
        if [row_idx, col_idx] not in visited:
            spiral_array.append(array[row_idx][col_idx])
            visited.append(([row_idx, col_idx]))
            row_idx += directions[current_direction][0]
            col_idx += directions[current_direction][1]

    return spiral_array

