def sum_list(lst):
    if not lst:  # базовый случай - пустой список
        return 0
    else:
        return lst[0] + sum_list(lst[1:])

# Запрашиваем данные у пользователя
input_str = input("Введите числа через пробел: ")

try:
    # Преобразуем введенные данные в список чисел
    numbers = [float(num) for num in input_str.split()]
    result = sum_list(numbers)
    print(f"Сумма введенных чисел: {result}")
except ValueError:
    print("Ошибка: Вводите только целые числа, разделенные пробелами!")