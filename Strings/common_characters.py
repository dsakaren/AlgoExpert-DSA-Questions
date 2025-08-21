def commonCharacters(strings):
    # Write your code here.
    unique_letters = set()
    letters_count = {}
    return_array = []

    for letters in strings:
        for char in letters:
            unique_letters.add(char)
        for ch in unique_letters:
            if ch not in letters_count.keys():
                letters_count[ch] = 0
            letters_count[ch] += 1
        unique_letters.clear()

    for k, v in letters_count.items():
        if v == len(strings):
            return_array.append(k)

    return return_array
