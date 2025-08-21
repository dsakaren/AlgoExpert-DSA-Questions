def longestSubstringWithoutDuplication(string):
    # Write your code here.
    max_letters = []
    max_len = 0

    current_letters = []
    current_len = 0

    left = 0
    right = 0

    while left < len(string) and right < len(string):
        if string[right] not in current_letters:
            current_letters.append(string[right])
            current_len = len(current_letters)
            right += 1
        else:
            if current_len > max_len:
                max_len = current_len
                max_letters = current_letters.copy()
            current_letters.clear()
            left += 1
            right = left

    if current_len > max_len:
        max_letters = current_letters.copy()

    return ''.join(str(el) for el in max_letters)
