# Функция, которая возвращает True для четных чисел
def is_even(num):
    return num % 2 == 0

# Список чисел
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Используем filter() для фильтрации четных чисел
even_numbers = filter(is_even, numbers)

# Преобразуем результат в список
result = list(even_numbers)

print(result)


numbers = [3, 7, 11, 26, 5, 18, 31]

filtered_numbers = list(filter(lambda x: x > 10, numbers))
print(filtered_numbers)