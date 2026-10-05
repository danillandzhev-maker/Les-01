A = int(input("Введи первое число:"))
B = int(input("Введи второе число:"))
C = input("Введи действие:")

if C =="+":
    print(A + B)
elif C == "-":
    print(A - B)
elif C == "*":
    print(A * B)
elif C == "/":
    if B == 0:
        print("На ноль на делиться")
    else:
         print(A / B)


