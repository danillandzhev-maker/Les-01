def common_elements():
    numbers_3 = [number for number in range(100) if number % 3 == 0]
    numbers_5 = [number for number in range(100) if number % 5 == 0]

    set_3 = set(numbers_3)
    set_5 = set(numbers_5)

    return set_3 & set_5


assert common_elements() == {0, 75, 45, 15, 90, 60, 30}

print("ОК")