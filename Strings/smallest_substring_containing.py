def smallestSubstringContaining(bigString, smallString):
    # Write your code here.
    smallest_substring = ''
    smallest_substring_len = len(bigString)
    current_substring_letters = {}
    solutions = []


    small_string_letters = get_letters_count(smallString)
    small_string_len = len(smallString)

    left = 0
    right = small_string_len


    while left < len(bigString) and right <= len(bigString):
        current_substring = bigString[left:right]
        current_substring_letters = get_letters_count(current_substring)
        if is_solution(small_string_letters,current_substring_letters):
            solutions.append(current_substring)
        current_substring_letters.clear()
        if right != len(bigString):
            right += 1
        else:
            left += 1
            right = small_string_len + left
            if left > len(bigString) - small_string_len:
                break

    if smallString in bigString:
        solutions.append(bigString)

    if not solutions:
        return ''
    solutions.sort(key=lambda x:len(x))


    return solutions[0]

def get_letters_count(word):
    letters_count = {}
    for i in range(len(word)):
        if word[i] not in letters_count:
            letters_count[word[i]] = 0
        letters_count[word[i]] += 1

    return letters_count

def is_solution(small_letters, current_letters):
    for k, v in small_letters.items():
        current_key = current_letters.get(k, 0)
        if v > current_key:
            return False
    return True
