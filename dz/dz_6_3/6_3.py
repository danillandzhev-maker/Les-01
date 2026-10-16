number = int(input("Введи целое число: "))

while number > 9:
    result = 1

    for digit in str(number):
        result *= int(digit)

    number = result

print(number)