def longestPalindromicSubstring(string):
    # Write your code here.
    max_len = 0
    max_substr = ''

    for i in range(len(string)):
        for j in range(len(string)-1, i-1, -1):
            current_substring = string[i:j+1]
            if current_substring == current_substring[::-1]:
                if len(current_substring) > max_len:
                    max_len = len(current_substring)
                    max_substr = current_substring

    return max_substr
