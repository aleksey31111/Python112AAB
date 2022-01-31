num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
print("Введите операцию:\n1.\"r\" - Унарный минус. "
      "\n2. \"+\" - Сложение.\n3. \"-\" - Вычитание.\n4. \"/\" - Деление."
      "\n5. \"*\" - Умножение.\n6. \"%\" - Нахождение остатка.\n7. \"<\" - Наименьшее из двух чисел."
      "\n8. \">\" - Наибольшее из двух чисел")
operation = input()
if operation == "r":
    print(not num1, not num2)
elif operation == "+":
    print(num1 + num2)
elif operation == "-":
    print(num1 - num2)
elif operation == "/":
    if num2 != 0:
        print(num1 / num2)
elif operation == "*":
    print(num1 * num2)
elif operation == "%":
    print(num1 % num2)
elif operation == "<":
    if num1 < num2:
        print(num1)
    elif num1 > num2:
        print(num2)
elif operation == ">":
    if num1 < num2:
        print(num2)
    if num1 > num2:
        print(num1)
