def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "На ноль делить нельзя"
    return x / y

def root(x):
    if x < 0:
        return "Из отрицательного числа нельзя извлечь корень"
    return x**0.5

def pow(x, y):
    return x**y

def value(x, y):
    return y / 100 * x

print("Выберите операцию:")
print("1. Сложение")
print("2. Вычитание")
print("3. Умножение")
print("4. Деление")
print("5. Извлечение корня из числа")
print("6. Возведение числа в степень")
print("7. Нахождение процента от числа")
choice = input("Введите номер операции (1/2/3/4/5/6/7): ")


if choice == '1':
    num1 = float(input("Введите первое слагаемое: "))
    num2 = float(input("Введите второе слагаемое: "))
    print(num1, "+", num2, "=", add(num1, num2))

elif choice == '2':
    num1 = float(input("Введите уменьшаемое: "))
    num2 = float(input("Введите вычитаемое: "))
    print(num1, "-", num2, "=", subtract(num1, num2))

elif choice == '3':
    num1 = float(input("Введите первый множитель: "))
    num2 = float(input("Введите второй множитель: "))
    print(num1, "*", num2, "=", multiply(num1, num2))

elif choice == '4':
    num1 = float(input("Введите делимое: "))
    num2 = float(input("Введите делитель: "))
    print(num1, "/", num2, "=", divide(num1, num2))

elif choice == '5':
    num1 = float(input("Введите число: "))
    print(f"root({num1}) = {root(num1)}")

elif choice == '6':
    num1 = float(input("Введите основание степени: "))
    num2 = float(input("Введите показатель степени: "))
    print(num1, "**", num2, "=", pow(num1, num2))

elif choice == '7':
    num1 = float(input("Введите число: "))
    num2 = float(input("Введите процент: "))
    print(f"value({num1}, {num2}) = {value(num1, num2)}")
    
else:
    print("Некорректный ввод")
