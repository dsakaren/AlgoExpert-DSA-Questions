def reverseWordsInString(string):
    # Write your code here.
    output_string = ''
    reversed_words = []

    left = right = len(string) - 1

    while right >= 0 and left >= 0:
        if string[left] != ' ':
            left -= 1
        else:
            reversed_words.append(string[left+1:right+1])
            left = right = left-1
    reversed_words.append(string[left+1:right+1])

    output_string = " ".join(reversed_words)

    return output_string
