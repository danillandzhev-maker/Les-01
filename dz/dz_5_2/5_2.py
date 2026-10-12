while True:
    first_number = float(input("Введите первое число: "))
    operation = input("Введите операцию (+, -, *, /): ")
    second_number = float(input("Введите второе число: "))

    if operation == "+":
        result = first_number + second_number
    elif operation == "-":
        result = first_number - second_number
    elif operation == "*":
        result = first_number * second_number
    elif operation == "/":
        if second_number != 0:
            result = first_number / second_number
        else:
            print("На ноль делить нельзя!")
            result = None
    else:
        print("Неверная операция!")
        result = None

    if result is not None:
        print("Результат:", result)

    continue_calculation = input(
        "Продолжить работу? (yes/y): "
    ).lower()

    if continue_calculation != "yes" and continue_calculation != "y":
        print("Калькулятор завершил работу.")
        break