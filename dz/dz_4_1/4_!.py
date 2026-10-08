numbers = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]

numbers = [number for number in numbers if number != 0] + [0] * numbers.count(0)

print(numbers)