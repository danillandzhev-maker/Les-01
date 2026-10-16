import string

letters = string.ascii_letters

user_input = input("Введи две буквы через дефис: ")

start_letter, end_letter = user_input.split("-")

start_index = letters.index(start_letter)
end_index = letters.index(end_letter)

result = letters[start_index:end_index + 1]

print(result)