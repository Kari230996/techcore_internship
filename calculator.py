print("=== Простой калькулятор ===")

a = input("Введите первое число: ")
b = input("Введите второе число: ")

operation = input("Выберите операцию (+, -, *, /): ")

try:
    a = float(a)
    b = float(b)

except ValueError:
    print("Ошибка: введите число!")
    exit()

if operation == "+":
    result = a + b
elif operation == "-":
    result = a - b
elif operation == "*":
    result = a * b
elif operation == "/":
    if b != 0:
        result = a / b
    else:
        print("Ошибка: деление на ноль!")
        exit()
    
print("Результат:", result)