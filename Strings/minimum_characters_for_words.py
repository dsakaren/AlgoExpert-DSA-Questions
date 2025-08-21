def minimumCharactersForWords(words):
    # Write your code here.
    required_chars = {}
    current_chars = {}
    return_array = []

    for word in words:
        for char in word:
            if char not in current_chars:
                current_chars[char] = 0
            current_chars[char] += 1
            if char not in required_chars:
                required_chars[char] = 0
            required_chars[char] = max(required_chars[char],current_chars[char])
        current_chars.clear()

    for k, v in required_chars.items():
        for i in range(v):
            return_array.append(k)

    return return_array
