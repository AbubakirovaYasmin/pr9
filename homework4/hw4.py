
numbers = []

while True:
    user_input = input("Введите число (или 'end' для завершения): ")

    if user_input.lower() == 'стоп':
        break

    try:

        number = int(float(user_input))
        numbers.append(number)
    except ValueError:
        print("Ошибка: введите число.")

even_count = sum(1 for num in numbers if num % 2 == 0)
odd_count = len(numbers) - even_count

print(f"Введенные числа: {numbers}")
print(f"Количество четных чисел: {even_count}")
print(f"Количество нечетных чисел: {odd_count}")