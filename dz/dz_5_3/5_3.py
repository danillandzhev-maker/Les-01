import string

text = input("Введите текст: ")

for symbol in string.punctuation:
    text = text.replace(symbol, "")

words = text.split()
hashtag = "#" + "".join(word.capitalize() for word in words)

hashtag = hashtag[:140]

print("Хештег:", hashtag)