# функция возвращающая площадь треугольника по 2 длинам его сторон
# def reactangl_area(a, b):
#     return a * b

# print(reactangl_area(17, 14))


# функция возвращяющяя большее из чисел

"""def maximum(a, b):
#     if a > b:
#         return a 
#     else:
#         return b
    
# print(maximum(25, 17))"""

# та же  функция с помощью лямбда в одной строке
print((lambda a, b: a if a > b else b)(25, 14))    
