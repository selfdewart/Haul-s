# # Создайте функцию с тремя аргументами, функция должна находить какой обьект больше других. Верните ту которая больше остальных
# def find_largest_object(a, b, c):
#     # Используем функцию max() для нахождения максимального значения
#     largest = max(a, b, c)
#     return largest

# # Пример использования функции
# object1 = 10
# object2 = 5
# object3 = 15

# largest_object = find_largest_object(object1, object2, object3)
# print("Наибольший объект:", largest_object)

# # Функция с одним аргументом, принимает только строки
# # Верните первую цифру которая встретится в тексте

# def find_first_digit(text):
#     for char in text:
#         if char.isdigit():
#             return char
#     return None  # Возвращаем None, если в строке не найдено ни одной цифры

# # Пример использования функции
# text = "Пример строки с цифрой 42 и текстом"
# first_digit = find_first_digit(text)
# if first_digit is not None:
#     print("Первая цифра в строке:", first_digit)
# else:
#     print("В строке нет цифр.")


# # Улучшение пред задания. Найдите цифру которая больше остальных в тексте и верните ее
# def find_largest_digit(text):
#     # Инициализируем переменные для отслеживания цифр и их количества
#     digit_count = {}
    
#     # Перебираем символы в тексте
#     for char in text:
#         if char.isdigit():
#             digit = int(char)
#             if digit in digit_count:
#                 digit_count[digit] += 1
#             else:
#                 digit_count[digit] = 1
    
#     # Находим цифру с максимальным количеством встреч
#     if digit_count:
#         largest_digit = max(digit_count, key=digit_count.get)
#         return str(largest_digit)
#     else:
#         return None  # Возвращаем None, если в строке нет цифр

# # Пример использования функции
# text = "Пример строки с цифрами 12345 и текстом"
# largest_digit = find_largest_digit(text)
# if largest_digit is not None:
#     print("Цифра, которая больше остальных в строке:", largest_digit)
# else:
#     print("В строке нет цифр.")

# #Выведите 100 раз надпись 'hello world'
# # решите двумя циклами
# # Используем два цикла: внешний для повторения вывода и внутренний для вывода 'hello world'.
# for _ in range(100):
#     for _ in range(1):
#         print('hello world')

#Написать функцию arithmetic, принимающую 3 аргумента: первые 2 - числа, третий - операция, которая должна быть произведена над ними. Если третий аргумент +, сложить их; если —, то вычесть; * — умножить; / — разделить (первое на второе). В остальных случаях вернуть строку "Неизвестная операция".
# def arithmetic(num1, num2, operation):
#     if operation == '+':
#         return num1 + num2
#     elif operation == '-':
#         return num1 - num2
#     elif operation == '*':
#         return num1 * num2
#     elif operation == '/':
#         if num2 != 0:
#             return num1 / num2
#         else:
#             return "Деление на ноль невозможно"
#     else:
#         return "Неизвестная операция"

# # Примеры использования функции
# result1 = arithmetic(5, 3, '+')  # Сложение
# result2 = arithmetic(5, 3, '-')  # Вычитание
# result3 = arithmetic(5, 3, '*')  # Умножение
# result4 = arithmetic(6, 2, '/')  # Деление
# result5 = arithmetic(5, 3, '%')  # Неизвестная операция

# print(result1)  # Вывод: 8
# print(result2)  # Вывод: 2
# print(result3)  # Вывод: 15
# print(result4)  # Вывод: 3.0
# print(result5)  # Вывод: Неизвестная операция


# def num(a, s, oper):
#    if oper == '+':
#        return a + s
#    elif oper =='-':
#        return a - s
#    elif oper =='*':
#        return a * s
#    elif oper =='/':
#        if s != 0:
#             return a / s
#        else:
#             return "Деление на ноль невозможно"
#    else:
#      return "Неизвестная операция"
# num(2, 3, '-')

#определение функции
def sayhello():
    print('hello')
    print('world')
    print('and evrybody')
#главная программа (в ней будем вызывать функции)
sayhello()
print("pause")
sayhello()

#определение функции
def square(x):
    print('квадрат числа ', x, "=", x**2)

def multiply(a, b):
    print(a*b)

def even(a):
    if a%2 == 0:
        print(a,'chetnoe')
    else:
        print(a,'nechetnoe')

def factorial(n):
    pr=1
    for i in range(2, n+1):
        pr=pr*i
    print(pr)


def primer():
    print("hello")

def primer():
    print("HELLO")
#главная программа (в ней будем вызывать функции)
primer()
import turtle

def move():
    turtle.forward(100)
    turtle.left(90)

def drawscuare():
    for i in range(4):
        move()

