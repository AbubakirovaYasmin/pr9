import random


def get_number():
    while True:
        user_input = input("Введите число: ")
        try:

            return int(float(user_input))
        except ValueError:
            print("Ошибка: введите число.")


numbers = [random.randint(0, 100) for _ in range(10)]
print("Сгенерированный список:", numbers)

result = []
for i in range(1, len(numbers)):
    if numbers[i] > numbers[i - 1]:
        result.append(numbers[i])

print("Элементы, которые больше предыдущего:", result)
