def generateDocument(characters, document):
    # Write your code here.
    char_dict = {}
    doc_dict = {}

    if document.strip() == '' :
        return True

    # if characters.strip() == '':
    #     return False

    for char in characters:
        if char not in char_dict.keys():
            char_dict[char] = 0
        char_dict[char] += 1

    for char in document:
        if char not in doc_dict.keys():
            doc_dict[char] = 0
        doc_dict[char] += 1

    for k, val in doc_dict.items():
        char_count = char_dict.get(k,val-1)
        if val > char_count:
            return False

    return True
