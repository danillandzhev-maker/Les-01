numbers = [0, 1, 7, 2, 4, 8]

if numbers:
    total = sum(numbers[::2])
    result = total * numbers[-1]
else:
    result = 0

print(result)