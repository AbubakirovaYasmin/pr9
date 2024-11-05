def get_list(a, b):
    start = int(min(a, b))
    end = int(max(a, b))

    integers = []
    for i in range(start, end + 1):
        if (i > a and i < b) or (i < a and i > b):
            integers.append(i)

    squares = []
    for i in integers:
        squares.append(i ** 2)

    return integers, squares


while True:
    try:
        a = float(input("Введите число a: "))
        b = float(input("Введите число b: "))
        break
    except ValueError:
        print("Ошибка: пожалуйста, введите корректные числа.")

integers, squares = get_list(a, b)

print(f"Целые числа между {a} и {b}: {integers}")
print(f"Квадраты целых чисел: {squares}")