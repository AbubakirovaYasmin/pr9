numbers = []

while True:
    user_input = input("Введите число (или 'end' для завершения): ")

    if user_input.lower() == 'end':
        break

    try:

        number = int(float(user_input))
        numbers.append(number)
    except ValueError:
        print("Ошибка: введите корректное число.")

print("Нечетные элементы списка:")
for num in numbers:
    if num % 2 != 0:
        print(num)