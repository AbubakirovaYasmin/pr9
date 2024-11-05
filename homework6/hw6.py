# def input_numbers():
#     numbers = []
#     while True:
#         user_input = input("Введите число (или 'стоп' для завершения ввода): ")
#         if user_input.lower() == 'стоп':
#             break
#         try:
#
#             num = int(float(user_input))
#             numbers.append(num)
#         except ValueError:
#             print("Ошибка: введите корректное число.")
#     return numbers
import random
numbers = [random.randint(0, 100) for _ in range(10)]
print("Сгенерированный список:", numbers)

def swap_min_max(numbers):
    if not numbers:
        print("Список пуст.")
        return

    min_index = numbers.index(min(numbers))
    max_index = numbers.index(max(numbers))

    numbers[min_index], numbers[max_index] = numbers[max_index], numbers[min_index]
    return numbers


# numbers = input_numbers()
swapped_numbers = swap_min_max(numbers)
print("Список после замены:", swapped_numbers)


