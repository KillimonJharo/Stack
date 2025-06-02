# 1. Рекурсивная функция для вычисления факториала
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


# 2. Рекурсивная функция для вычисления суммы элементов списка
def sum_list(lst):
    if not lst:
        return 0
    else:
        return lst[0] + sum_list(lst[1:])


# 3. Рекурсивная функция бинарного поиска
def binary_search(lst, target, low=0, high=None):
    if high is None:
        high = len(lst) - 1

    if low > high:
        return -1

    mid = (low + high) // 2

    if lst[mid] == target:
        return mid
    elif lst[mid] > target:
        return binary_search(lst, target, low, mid - 1)
    else:
        return binary_search(lst, target, mid + 1, high)


# 4. Класс Stack
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        """Добавляет элемент на вершину стека"""
        self.items.append(item)

    def pop(self):
        """Удаляет и возвращает элемент с вершины стека"""
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Pop from empty stack")

    def is_empty(self):
        """Проверяет, пуст ли стек"""
        return len(self.items) == 0

    def peek(self):
        """Возвращает элемент с вершины стека без удаления"""
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Peek from empty stack")


def get_number_input(prompt):
    """Функция для безопасного ввода чисел"""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Ошибка! Пожалуйста, введите целое число.")


def get_list_input():
    """Функция для ввода списка чисел"""
    print("Введите числа через пробел (например: 1 2 3 4 5):")
    while True:
        try:
            return [int(x) for x in input().split()]
        except ValueError:
            print("Ошибка! Пожалуйста, вводите только числа, разделенные пробелами.")


def demo_factorial():
    """Демонстрация работы функции факториала"""
    print("\n--- Вычисление факториала ---")
    n = get_number_input("Введите число для вычисления факториала: ")
    print(f"Факториал числа {n} равен: {factorial(n)}")


def demo_sum_list():
    """Демонстрация работы функции суммы списка"""
    print("\n--- Сумма элементов списка ---")
    lst = get_list_input()
    print(f"Сумма элементов списка {lst} равна: {sum_list(lst)}")


def demo_binary_search():
    """Демонстрация работы бинарного поиска"""
    print("\n--- Бинарный поиск ---")
    lst = get_list_input()
    target = get_number_input("Введите число для поиска: ")

    # Проверяем, отсортирован ли список
    if lst != sorted(lst):
        print("Внимание: Список не был отсортирован. Сортирую...")
        lst.sort()
        print(f"Отсортированный список: {lst}")

    result = binary_search(lst, target)
    if result != -1:
        print(f"Число {target} найдено на позиции {result}")
    else:
        print(f"Число {target} не найдено в списке")


def demo_stack():
    """Демонстрация работы стека"""
    print("\n--- Работа со стеком ---")
    stack = Stack()

    while True:
        print("\nТекущее состояние стека:", stack.items)
        print("1. Добавить элемент (push)")
        print("2. Извлечь элемент (pop)")
        print("3. Посмотреть верхний элемент (peek)")
        print("4. Проверить, пуст ли стек")
        print("5. Вернуться в главное меню")

        choice = input("Выберите действие (1-5): ")

        if choice == '1':
            item = get_number_input("Введите элемент для добавления: ")
            stack.push(item)
            print(f"Элемент {item} добавлен в стек")
        elif choice == '2':
            try:
                item = stack.pop()
                print(f"Извлечен элемент: {item}")
            except IndexError:
                print("Ошибка: стек пуст!")
        elif choice == '3':
            try:
                item = stack.peek()
                print(f"Верхний элемент стека: {item}")
            except IndexError:
                print("Ошибка: стек пуст!")
        elif choice == '4':
            print("Стек пуст" if stack.is_empty() else "Стек не пуст")
        elif choice == '5':
            break
        else:
            print("Неверный ввод. Пожалуйста, выберите от 1 до 5.")


def main():
    """Главное меню программы"""
    while True:
        print("\n=== Главное меню ===")
        print("1. Вычислить факториал числа")
        print("2. Найти сумму элементов списка")
        print("3. Выполнить бинарный поиск")
        print("4. Работа со стеком")
        print("5. Выход")

        choice = input("Выберите операцию (1-5): ")

        if choice == '1':
            demo_factorial()
        elif choice == '2':
            demo_sum_list()
        elif choice == '3':
            demo_binary_search()
        elif choice == '4':
            demo_stack()
        elif choice == '5':
            print("Выход из программы...")
            break
        else:
            print("Неверный ввод. Пожалуйста, выберите от 1 до 5.")


if __name__ == "__main__":
    print("Программа для демонстрации рекурсивных функций и работы со стеком")
    main()