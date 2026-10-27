def popular_words(text, words):
    text = text.lower()
    text = text.split()

    result = {}

    for word in words:
        result[word] = text.count(word)

    return result