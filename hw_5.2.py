while True:
    a = float(input("Введіть перше число: "))
    op = input("Оберіть операцію (+, -, *, /): ")
    b = float(input("Введіть друге число: "))

    if op == "+":
        result = a + b
    elif op == "-":
        result = a - b
    elif op == "*":
        result = a * b
    elif op == "/":
        if b == 0:
            print("На нуль ділити не можна!")
            continue
        result = a / b
    else:
        print("Невідома операція!")
        continue

    print("Результат:", result)

    cont = input("Бажаєте продовжити? (y / n): ").lower()
    if cont != "y" and cont != "yes":
        print("Роботу завершено.")
        break
