import random


def get_user_numbers(ticket):
    user_numbers = []

    for row in ticket:
        while True:
            try:
                user_input = input(f"Выберите число из {row}: ")
                number = int(float(user_input))
                if number in row:
                    user_numbers.append(number)
                    break
                else:
                    print("Число должно быть в указанной строке.")
            except ValueError:
                print("Ошибка: введите корректное число.")

    return user_numbers


def get_random_numbers(ticket):
    program_numbers = [random.choice(row) for row in ticket]
    return program_numbers


ticket = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]

print("Выберите по одному числу из каждой строки лотерейного билета.")
user_numbers = get_user_numbers(ticket)
program_numbers = get_random_numbers(ticket)

print("\nВыбранные вами числа:", user_numbers)
print("Числа, выбранные программой:", program_numbers)

matches = set(user_numbers) & set(program_numbers)
result = ', '.join(str(item) for item in matches)
print(f"Количество совпадений: {len(matches)}")
print(f"Совпадения: {result}")
