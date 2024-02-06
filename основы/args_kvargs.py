def summa(*args):
    print(type(args))

summa(7, 8, 9, 1, 10) 

def brand(**brands):
    print(brands)

brand(a = 'Apple', s = 'Samsung') 

# **kwargs (звездочка перед "kwargs") используется для передачи произвольного числа именованных аргументов (ключевых слов) в функцию. Когда вы видите **kwargs в определении функции, это означает, что функция может принимать любое количество аргументов в форме "ключ=значение".
# Пример:

def пример(**kwargs):
    for ключ, значение in kwargs.items():
        print(f'{ключ}: {значение}')

пример(имя='Иван', возраст=25)
# Вывод:
# имя: Иван
# возраст: 25