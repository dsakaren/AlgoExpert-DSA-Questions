def runLengthEncoding(string):
    # Write your code here.
    letters = []

    string_to_return = ''
    char_count = 1


    for i in range(1, len(string)):
        previous_char = string[i-1]
        current_char = string[i]

        if previous_char == current_char:
            char_count += 1
            if char_count == 10:
                letters.append(str(9))
                letters.append(previous_char)
                char_count = 1
        else:
            letters.append(str(char_count))
            letters.append(previous_char)
            char_count = 1

    letters.append(str(char_count))
    letters.append(string[len(string) - 1])

    string_to_return = ''.join(el for el in letters)

    return string_to_return
