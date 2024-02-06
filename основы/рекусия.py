# рекурсивная функция n!= 1 * 2 * 3 *...*m
#Факториал — это произведение всех натуральных чисел от 1 до данного числа. Например, факториал числа 5 будет равен 1 × 2 × 3 × 4 × 5 = 120.
# def recursive(value):
#     print(value)
#     if value < 4:
#         recursive(value+1)
#     print(value)


# recursive(1)

# def fact(n):
#     if n <= 0:
#         return 1
#     else:
#         return n * fact(n-1)
    

# p = fact(6)
# print(p) # факториал числа 6 

"""F = {
    'C:':{
        'python39':['python.exe', 'python.ini'],
        'Program Files': {
            'Java': ['README.txt', 'Welcome.html', 'java.exe'],
            'MATLAB': ['matlab.bat', 'matlab.exe', 'mcc.bat']
        },
        'Windows': {
            'Sistem32': ['acledit.dll', 'actui.dll', 'zipfldr.dll']
        }
    }
}

def get_files(path, depth=0):
    for f in path:
        print(" "*depth, f)
        if type(path[f]) == dict:
            get_files(path[f], depth+1)
        else:
            print(" "*depth, "".join(path[f]))


get_files(F)
"""


#Факториал:
# Напишите функцию для вычисления факториала числа с использованием рекурсии.

"""def Factorial(x):
    if x <= 0:
        return 1
    else:
        return x * Factorial(x-1)
    
p = Factorial(5)
print(p)
"""
#Сумма чисел:
# Создайте функцию, которая считает сумму чисел от 1 до n с использованием рекурсии.
"""def sum_of_numbers(n):
    # Базовый случай: сумма чисел от 1 до 1 равна 1
    if n == 1:
        return 1
    else:
        # Рекурсивный случай: суммируем текущее число с суммой чисел от 1 до (n-1)
        return n + sum_of_numbers(n-1)

# Пример использования
result = sum_of_numbers(3)
print(result)  # Ожидаемый результат: 6"""

# Возведение в степень:
# Реализуйте функцию для возведения числа в степень, используя рекурсию.

def power(x, n):
    # Базовый случай: любое число в степени 0 равно 1
    if n == 0:
        return 1
    else:
         # Рекурсивный случай: x^n = x * x^(n-1)
        return x * power(x, n-1)

# Пример использования
result = power(5, 3)
print(result)  # Ожидаемый результат: 8
    

# Палиндром:
# Напишите функцию, которая проверяет, является ли строка палиндромом с использованием рекурсии.

def is_palindrome(s):
    # Базовый случай: строка из одного символа всегда палиндром
    if len(s) <= 1:
        return True
    else:
        # Сравниваем первый и последний символы, затем рекурсивно проверяем подстроку между ними
        return s[0] == s[-1] and is_palindrome(s[1:-1])

# Пример использования
result = is_palindrome("radar")
print(result)  # Ожидаемый результат: True

# Числа Фибоначчи:
# Создайте функцию для генерации чисел Фибоначчи с использованием рекурсии.

def fibonacci(n):
        # Базовые случаи: F(0) = 0, F(1) = 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        # Рекурсивное соотношение: F(n) = F(n-1) + F(n-2)
        return fibonacci(n-1) + fibonacci(n-2)

# Пример использования
result = fibonacci(5)
print(result)  # Ожидаемый результат: 5

# Быстрое возведение в степень:
# Реализуйте алгоритм быстрого возведения числа в степень с использованием рекурсии.



# Обратная строка:
# Напишите функцию для обращения строки с использованием рекурсии.

# Бинарный поиск:
# Реализуйте алгоритм бинарного поиска с использованием рекурсии.

# Треугольное число:
# Создайте функцию для вычисления n-го треугольного числа с использованием рекурсии.




# Сортировка слиянием:
# Реализуйте сортировку слиянием с использованием рекурсии для списка чисел.





#.........................................

def rec(x):
    if x<4:
        print(x)# 1, 2, 3
        rec(x + 1)
        print(x)#3 ,2, 1
  

rec(1)


# функция нахождении факториала числа
def fact(x):
    if x==1:
        return 1
    return fact (x-1) * x

print(fact(4))
print(fact(10))

# функция нахождении фибонначи чисел 

"""def fib(n):
    if n==1:
        return 0
    if n==2:
        return 1
    return fib(n-1) +fib (n-2)

print(fib(5))"""

#палиндром
def palindrom(s):
    if len(s) <=1:
        return True
    if s[0] != s[-1]:
        return False
    return palindrom(s[1:-1])

print(palindrom('шалаш'))