def factorial(n):
    if n == 0 or n == 1:  # базовый случай
        return 1
    else:
        return n * factorial(n - 1)

# Запрашиваем число у пользователя
try:
    num = int(input("Введите целое неотрицательное число для вычисления: "))
    if num < 0:
        print("Факториал отрицательного числа не определен!")
    else:
        print(f"Факториал числа {num} равен: {factorial(num)}")
except ValueError:
    print("Ошибка: Введите целое число!")