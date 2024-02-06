#функция map
#class map(object)
    #map(func, iterables) --> map object

    #map() принимает функцию и итерацию (или несколько итераций) в качестве аргументов и возвращает итератор, который выдает преобразованные элементы по запросу.

# Определяем функцию, которую будем применять
"""def square(x):
    return x ** 2"""

# Исходная последовательность
"""numbers = [1, 2, 3, 4, 5]"""

# Используем map для применения функции к каждому элементу списка
"""squared_numbers = map(square, numbers)"""

# Преобразуем результат в список для просмотра
"""result = list(squared_numbers)

print(result)"""


a = [-1, 2, -3, 4, 5]
#abs приминился ко всем элементам "а"
b = list(map(abs, a))
#вызов
print(b)

#2 работа со стоками
def f(x):
    return x ** 2

a = ['hello', 'hi', 'good morning']
с = list(map(str.upper, a))
#вызов
print(с)

# добавление лямбда функции
def f(x):
    return x ** 2

a = ['hello', 'hi', 'good morning']
d = list(map(lambda x: x + "!" , a))
#вызов
print(d)

#sorted funtion
"""def f(x):
    return x ** 2

a = ['hello', 'hi', 'good morning']
b = list(map(list, a))
g = list(map(sorted, b))
#вызов
print(g)"""

#hz

"""def f(x):
    return x ** 2


s = list(map(int, input().split()))
print(s)
"""

list_type = ("I", "like", "Python")
print("**".join(list_type))

