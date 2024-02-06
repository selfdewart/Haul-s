# 1
#n = input() 
# print([i for i in range(1, int(n)) if i % 2 == 0])
#Возьмём строку Hi, loop! и будем выводить каждый её символ. Если встретим запятую, досрочно завершим цикл.
# string = 'Hi, loop!'
# for i in string:
#     if i == ',':
#         break
#     print(i)

# num = int(input())
# if num == 1:
#     d = 1
# for i in range(1, int((num /2)+1)):
#     if num%i == 0:
#         i += 1
#     print(i)


# num = int(input())
# for i in range(1, int(num)):
#     if i%2 != 0:
#         print(i)

# word = input("Введите слово: ")
# reversed_word = word[::-1]

# reversed_word =[1]
# if word == reversed_word:
#     print("Это палиндром!")
# else:
#     print("Это не палиндром.")

# word = input("Введите слово: ")
# is_palindrome = all(word[i] == word[~i] for i in range(len(word) // 2))
# if is_palindrome:
#     print("Это палиндром!")
# else:
#     print("Это не палиндром.")

# Метод 2: использовать цикл для сравнения символов

# word = input("Введите слово: ")
# is_palindrome = True
# for i in range(len(word) // 2):
#     if word[i] != word[len(word) - i - 1]:
#         is_palindrome = False
#         break
# if is_palindrome:
#     print("Это палиндром!")
# else:
#     print("Это не палиндром.")

# text = input("Введите текст: ")
# гласные = "АЕЁИОУЫЭЮЯаеёиоуыэюя"
# найденные_гласные = [буква for буква in text if буква in гласные]
# print("Гласные буквы в тексте:", найденные_гласные)
# #Этот код создаёт словарь, в котором ключи будут индексами элементов списка users, а значения будут самими элементами таблицы.
# users = ['Alinur', 'Sherdos']
# user_dict = {index: user for index, user in enumerate(users)}
# print(user_dict)

# Пример 1: Перебор элементов списка


# # Пример 3: Поиск элемента в двумерном списке
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# target = 5
# for row in range(len(matrix)):
#     for col in range(len(matrix[row])):
#         if matrix[row][col] == target:
#             print(f"Элемент {target} найден в позиции ({row}, {col}).")

#Вычисление високосного года 
# year = int(input())

# if (year % 4) == 0:
#    if (year % 100) == 0:
#        if (year % 400) == 0:
#            print(year, "год високосный")
#        else:
#            print(year,'Не високосный')
#    else:
#        print(year,'год високосный')
# else:
#    print(year,' Не високосный')



# num1 = float(input("Введи первое число: "))
# num2 = float(input("Введи второе число: "))
# num3 = float(input("Введи третье число: "))

# if (num1 >= num2) and (num1 >= num3):
#    largest = num1
# elif (num2 >= num1) and (num2 >= num3):
#    largest = num2
# else:
#    largest = num3

# print("Наибольшее число из трех чисел", largest)

#Простые числа вычисление
# lower = 900
# upper = 1000

# print("Диапазон чисел между", lower, "и", upper)

# for num in range(lower, upper + 1):
#    if num > 1:
#        for i in range(2, num):
#            if (num % i) == 0:
#                break
#        else:
#            print(num)



# years = int(input())
# def season(years):
#  if years <= 12:
#     if (1 <= years <= 4):
#          return"весна"
#     elif (5 <= years <= 8):
#              print("лето")
#     elif 9 <= years <= 11:
#         return "осень" 
#     else:
#         return"зима"
#  else:
#      return"неверный номер месяц"
    
# print(f"Месяц {years} принадлежит к времени года: {season(years)}")

# Написать функцию is_prime, принимающую 1 аргумент
# — число от 0 до 1000, и возвращающую True, если оно простое, и False - иначе.
"""is_prime = int(input())
if is_prime % 2 != 0:
    print("True")
else:
    print('False')"""

# def is_prime(number):
#     if number < 2:
#         return False  # 0 и 1 не являются простыми числами
#     if number == 2:
#         return True  # 2 - простое число

#     # Проверяем, делится ли число нацело на все числа от 2 до квадратного корня из числа + 1
#     for i in range(2, int(number**0.5) + 1):
#         if number % i == 0:
#             return False  # Число не является простым, так как делится без остатка

#     return True  # Если ни одно число не подошло, то число простое

# # Пример использования функции
# number = 17
# if is_prime(number):
#     print(f"{number} - простое число")
# else:
#     print(f"{number} - не простое число")


# def bank(a, years):
#     # Преобразуем процентную ставку в десятичное значение
#     annual_interest_rate = 10 / 100

#     # Вычисляем конечную сумму с использованием формулы сложных процентов
#     final_amount = a * (1 + annual_interest_rate) ** years

#     return final_amount

# # Пример использования функции
# initial_deposit = 1000  # Начальный вклад
# investment_period = 5  # Срок вклада в годах
# result = bank(initial_deposit, investment_period)
# print(f"Через {investment_period} лет на счету будет {result:.2f} рублей")


def is_valid_date(day, month, year):
    # Проверяем, что год, месяц и день находятся в допустимых диапазонах
    if year < 1 or month < 1 or month > 12:
        return False
    
    # Определяем максимальное количество дней в каждом месяце
    max_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Проверяем високосный год
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        max_days[1] = 29

    # Проверяем, что день находится в допустимом диапазоне
    if day < 1 or day > max_days[month - 1]:
        return False

    return True

# Пример использования функции
day = 31
month = 12
year = 2023

if is_valid_date(day, month, year):
    print(f"{day:02d}.{month:02d}.{year} - такая дата существует в календаре.")
else:
    print(f"{day:02d}.{month:02d}.{year} - такой даты в календаре нет.")
