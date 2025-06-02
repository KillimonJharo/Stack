def binary_search(arr, target, low=0, high=None):
    if high is None:
        high = len(arr) - 1

    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, high)
    else:
        return binary_search(arr, target, low, mid - 1)


def get_sorted_list():
    while True:
        try:
            input_str = input("Введите отсортированные числа через пробел: ")
            numbers = [float(x) for x in input_str.split()]

            # Проверяем, что список отсортирован
            if numbers != sorted(numbers):
                print("Ошибка: Числа должны быть введены в отсортированном порядке!")
                continue

            return numbers
        except ValueError:
            print("Ошибка: Вводите только числа, разделенные пробелами!")


def get_target_number():
    while True:
        try:
            return float(input("Введите число для поиска: "))
        except ValueError:
            print("Ошибка: Введите корректное число!")


# Основная программа
print("Программа бинарного поиска в отсортированном массиве")
numbers = get_sorted_list()
target = get_target_number()

result = binary_search(numbers, target)

if result != -1:
    print(f"Число {target} найдено на позиции {result}")
else:
    print(-1)