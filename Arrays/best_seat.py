def bestSeat(seats):
    # Write your code here.
    if sum(seats) == len(seats):
        return -1

    best_len = 0
    best_indexes = []
    best_count = 0

    for i in range(1, len(seats)-1):
        for j in range(len(seats)-1, -1, -1):
            current_seats = seats[i:j]
            current_sum = sum(current_seats)
            if current_sum == 0:
                current_len = len(current_seats)
                if current_len > best_len:
                    best_len = current_len
                    best_indexes.clear()
                    best_indexes = [i,j]
                    best_count = j - i

    if len(best_indexes) == 1:
        return best_indexes[0]

    if best_count % 2 == 0:
        return (best_indexes[0] + best_indexes[1]) // 2 - 1

    return (best_indexes[0] + best_indexes[1]) // 2
