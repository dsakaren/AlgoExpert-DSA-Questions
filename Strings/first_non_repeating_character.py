def firstNonRepeatingCharacter(string):
    # Write your code here.
    char_dict = {}

    for i in range(len(string)):
        if string[i] not in char_dict:
            char_dict[string[i]] = [i, 0]
        char_dict[string[i]][1] += 1

    for k, v in char_dict.items():
        if v[1] == 1:
            return v[0]

    return -1