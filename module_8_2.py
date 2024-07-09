def personal_sum(numbers):
    global result
    global k
    result = 0
    incorrect_data = 0
    k = 0
    for num in numbers:
        try:
            result += num
            k += 1
        except TypeError:
            print(f"Некорректный тип данных для подсчета суммы - {num}")
            incorrect_data += 1
    res = (result, incorrect_data)
    return res


def calculate_average(numbers):
    try:
        personal_sum(numbers)
        s = result
        k1 = k
        average = 0
        average = s / k1
    except ZeroDivisionError:
        0
    except TypeError:
        print("В numbers записан некорректный тип данных")
        average = None
    return average


print(f'Результат 1: {calculate_average("1, 2, 3")}')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Еще Строка"])}')
print(f'Результат 3: {calculate_average(567)}')
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')
