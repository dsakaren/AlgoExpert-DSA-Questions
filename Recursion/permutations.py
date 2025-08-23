def getPermutations(array):
    # Write your code here.
    if not array:
        return []

    n = len(array)
    result, solutions = [], []

    def backtrack():
        if len(solutions) == n:
            # result.append(solutions.copy())
            result.append(solutions[:])
            return

        for num in array:
            if num not in solutions:
                solutions.append(num)
                backtrack()
                solutions.pop()

    backtrack()

    return result
