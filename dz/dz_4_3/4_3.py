import random

numbers = [random.randint(1, 10) for _ in range(random.randint(3, 10))]

result = [numbers[0], numbers[2], numbers[-2]]

print(numbers)
print(result)