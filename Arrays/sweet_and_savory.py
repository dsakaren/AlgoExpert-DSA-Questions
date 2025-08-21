def sweetAndSavory(dishes, target):
    # Write your code here.
    dishes.sort()

    left = 0
    right = len(dishes) - 1
    best_combination = [0, 0]
    best_score = float('inf')

    if not dishes or dishes[left] > 0 or dishes[right] < 0:
        return [0, 0]

    while left < right and dishes[left] < 0 and dishes[right] > 0:
        current_sum = dishes[left] + dishes[right]

        if current_sum == target:
            return [dishes[left], dishes[right]]
        elif current_sum < target:
            score = target - current_sum
            if score < best_score:
                best_combination = [dishes[left], dishes[right]]
                best_score = score
            left += 1
        else:
            right -= 1

    return best_combination
