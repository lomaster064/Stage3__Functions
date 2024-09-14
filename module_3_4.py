def single_root_words(root_word = 'word', *other_words):
    same_words = []
    word = root_word.upper()
    for i in range(len(other_words)):
        value = other_words[i].upper()
        if word == value or word.count(value) or value.count(word):
            same_words.append(other_words[i])

    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)