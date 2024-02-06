"""def f():
    return [43, 65, 32]

def genf():
    g = 7
    for i in [43, 65, 32]:
        yield i
        print(g)
        g = g * 10 + 7

s = genf()
print(next(s))
print(next(s))
"""



# def fact(n):
#     pr = 1
#     for i in range(1, n+1):
#         pr=pr * i
#         yield pr

# for i in fact(10):
#     print(i, end=' ')

"""список = [1, 2, 3, 4, 5]

итератор = iter(список)

# Получение следующего элемента
первый_элемент = next(итератор)
print(первый_элемент)  # Вывод: 1

второй_элемент = next(итератор)
print(второй_элемент)  # Вывод: 2

третий_элемент = next(итератор)
print(третий_элемент)  # Вывод: 3"""

"""
В этом примере цикл продолжается до тех пор,
 пока не достигнут конец списка, и при возникновении 
исключения StopIteration цикл завершается.
список = [1, 2, 3, 4, 5]

итератор = iter(список)
 
while True:
    try:
        element = next(итератор)
        print(element)
    except StopIteration:
        break
"""


list_type = [1, 2, 3, 4]
iterator = iter(list_type)

for i in iterator:
    print(i)