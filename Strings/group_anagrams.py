def groupAnagrams(words):
    # Write your code here.
    return_array = []
    temp_array = []
    first_word_letters = {}
    other_word_letters = {}

    for i in range(len(words)):
        if word_in_return_array(words[i], return_array):
            continue
        temp_array.clear()
        first_word_letters.clear()
        other_word_letters.clear()
        for letter in words[i]:
            if letter not in first_word_letters:
                first_word_letters[letter] = 0
            first_word_letters[letter] += 1
        for j in range(i+1, len(words)):

            if len(words[i]) == len(words[j]):
                for letter in words[j]:
                    if letter not in first_word_letters:
                        other_word_letters.clear()
                        break
                    if letter not in other_word_letters:
                        other_word_letters[letter] = 0
                    other_word_letters[letter] += 1
                for k, val in first_word_letters.items():
                    if val != other_word_letters.get(k,0):
                        other_word_letters.clear()
                        break
                else:
                    temp_array.append(words[j])
                    other_word_letters.clear()
        temp_array.append(words[i])
        if temp_array not in return_array:
            return_array.append(temp_array.copy())


    return return_array

def word_in_return_array(word, arr):
    for i in range(len(arr)):
        if word in arr[i]:
            return True
    return False
