def semordnilap(words):
    # Write your code here.
    return_array = []

    for i in range(len(words)):
        other_words = words[:i] + words[i+1:]
        reversed_word = words[i][::-1]
        if reversed_word in other_words:
            if [words[i], reversed_word] not in return_array and [reversed_word, words[i]] not in return_array:
                return_array.append([words[i], reversed_word])

    return return_array
