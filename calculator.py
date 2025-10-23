print("=== Простой калькулятор ===")

a = input("Введите первое число: ")
b = input("Введите второе число: ")

operation = input("Выберите операцию (+, -, *, /): ")

try:
    a_val = float(a)
    b_val = float(b)
    is_number = True

except ValueError:
    is_number = False

# Работа с числами
if is_number:
    if operation == "+":
        result = a_val + b_val
    elif operation == "-":
        result = a_val - b_val
    elif operation == "*":
        result = a_val * b_val
    elif operation == "/":
        if b_val != 0:
            result = a_val / b_val
        else:
            print("Ошибка: деление на ноль!")
            exit()
    else:
        print("Ошибка: неизвестная операция.")
        exit()

# Работа со строками
else:
    if operation == "+":
        result = a + b
    elif operation == "*":
        try:
            b_int = int(b)
            result = a * b_int
        except ValueError:
            print("Ошибка: при работе со строками можно только складывать или умножать строку на целое число.")
            exit()
    else:
        print("Ошибка: при работе со строками доступны только '+' и '*' (на число).")
        exit()
    
print("Результат:", result)