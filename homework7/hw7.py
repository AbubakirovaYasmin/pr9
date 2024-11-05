import random
numbers = [random.randint(0, 100) for _ in range(10)]
print("Сгенерированный список:", numbers)

def cyclic_shift_right(arr):
    if not arr:
        return arr
    return [arr[-1]] + arr[:-1]


# def get_integer_input():
#     while True:
#         user_input = input("Введите число: ")
#         try:
#             number = int(float(user_input))
#             return number
#         except ValueError:
#             print("Ошибка: введите корректное число.")


# print("Введите числа (для завершения введите 'exit'): ")

# while True:
#     user_input = input()
#     if user_input.lower() == 'exit':
#         break
#     try:
#         number = int(float(user_input))
#         numbers.append(number)
#     except ValueError:
#         print("Ошибка: введите корректное число.")

if numbers:
    # print("Исходный список:", numbers)
    shifted_numbers = cyclic_shift_right(numbers)
    print("Список после циклического сдвига вправо:", shifted_numbers)
else:
    print("Список пуст.")


