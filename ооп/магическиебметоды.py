# class Test:
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end
#         self.counter = start

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.counter >= self.end:
#             raise StopIteration
#         else:
#             current_value = self.counter
#             self.counter -= 1
#             return current_value

# test = Test(10, 0)
# for i in test:
#     print(i)


class Test:
    def __init__(self, arg):
        self.arg = arg
        self.counter = len(arg) - 1  # Устанавливаем счетчик в конец списка

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter >= 0:
            index = self.counter
            self.counter -= 1
            return self.arg[index]
        else:
            raise StopIteration

# test = Test([1, 2, 3, 4, 5])
# for i in test:
#     print(i)


# магические методы __str__ и __repr__
# В этом примере __init__, __str__ и __add__ - это 
# магические методы, определяющие инициализацию, строковое представление и сложение объектов типа Комплексное_Число.
class Комплексное_Число:
    def __init__(self, вещественная_часть, мнимая_часть):
        self.вещественная_часть = вещественная_часть
        self.мнимая_часть = мнимая_часть

    def __str__(self):
        return f"{self.вещественная_часть} + {self.мнимая_часть}i"

    def __add__(self, другое_число):
        новая_вещественная = self.вещественная_часть + другое_число.вещественная_часть
        новая_мнимая = self.мнимая_часть + другое_число.мнимая_часть
        return Комплексное_Число(новая_вещественная, новая_мнимая)

# Использование магических методов
"""число1 = Комплексное_Число(1, 2)
число2 = Комплексное_Число(2, 3)

сумма_чисел = число1 + число2
print(сумма_чисел)  # Вывод: 3 + 5i
"""
# Создайте класс Matrix для представления матриц. Реализуйте магические методы __init__, __add__, __sub__, __mul__, __str__ и __eq__. Проверьте операции сложения, вычитания, умножения и сравнения для объектов этого класса.

class Matrix:
    def __init__(self, rows, columns, elements):
        self.rows = rows
        self.columns = columns
        self.elements = elements

    def __add__(self, другая_матрица):
        if self.rows != другая_матрица.rows or self.columns != другая_матрица.columns:
            raise ValueError("Нельзя сложить матрицы разных размеров.")
        
        новые_элементы = [
            [self.elements[i][j] + другая_матрица.elements[i][j] for j in range(self.columns)]
            for i in range(self.rows)
        ]
        
        return Matrix(self.rows, self.columns, новые_элементы)

    def __sub__(self, другая_матрица):
        if self.rows != другая_матрица.rows or self.columns != другая_матрица.columns:
            raise ValueError("Нельзя вычесть матрицы разных размеров.")
        
        новые_элементы = [
            [self.elements[i][j] - другая_матрица.elements[i][j] for j in range(self.columns)]
            for i in range(self.rows)
        ]
        
        return Matrix(self.rows, self.columns, новые_элементы)

    def __mul__(self, другая_матрица):
        if self.columns != другая_матрица.rows:
            raise ValueError("Число столбцов первой матрицы должно быть равно числу строк второй матрицы.")
        
        новые_элементы = [
            [sum(self.elements[i][k] * другая_матрица.elements[k][j] for k in range(self.columns))
             for j in range(другая_матрица.columns)]
            for i in range(self.rows)
        ]
        
        return Matrix(self.rows, другая_матрица.columns, новые_элементы)

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.elements])

    def __eq__(self, другая_матрица):
        return self.elements == другая_матрица.elements

# Пример использования
# matrix1 = Matrix(2, 3, [[1, 2, 3], [4, 5, 6]])
# matrix2 = Matrix(2, 3, [[7, 8, 9], [10, 11, 12]])

# # Сложение матриц
# сумма_матриц = matrix1 + matrix2
# print("Сумма матриц:")
# print(сумма_матриц)
# print()

# # Вычитание матриц
# разность_матриц = matrix1 - matrix2
# print("Разность матриц:")
# print(разность_матриц)
# print()

# # Умножение матриц
# произведение_матриц = matrix1 * matrix2
# print("Произведение матриц:")
# print(произведение_матриц)
# print()

# # Сравнение матриц
# print("Сравнение матриц:")
# print(matrix1 == matrix2)  # False
# print(matrix1 == Matrix(2, 3, [[1, 2, 3], [4, 5, 6]]))  # True


# Метод __len__ позволяет нам определить длину объекта. Это часто используется для собственных коллекций, чтобы поддерживать процедуру len().

# Пример кода:
    
class Mylist:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)
    
lst = Mylist([1, 2, 3, 4, 5])
print(len(lst))


# Метод __getitem__ позволяет объекту быть поддерживаемым индексированием, что позволяет нам обращаться к элементам объекта по индексу, подобно списку или словарю.

#Пример кода:
class MyList:
    def __init__(self, items):
        self.items = items

    def __getitem__(self, index):
        return self.items[index]

# lst = MyList([1, 2, 3, 4, 5])
# print(lst[2])  # Выведет: 3

# Метод __setitem__ позволяет объекту поддерживать присваивание значений по индексу.

# Пример кода:

class MyList:
    def __init__(self, items):
        self.items = items

    def __setitem__(self, index, value):
        self.items[index] = value

# lst = MyList([1, 2, 3, 4, 5])
# lst[2] = 10
# print(lst.items)  # Выведет: [1, 2, 10, 4, 5]
        


#  __delitem__ - Удаление по индексу

# Метод __delitem__ позволяет объекту поддерживать удаление элемента по индексу.

# Пример кода:
class MyList:
    def __init__(self, items):
        self.items = items

    def __delitem__(self, index):
        del self.items[index]

# lst = MyList([1, 2, 3, 4, 5])
# del lst[2]
# print(lst.items)  # Выведет: [1, 2, 4, 5]
        
# __iter__ и __next__ - Итерация по объекту

# Метод __iter__ позволяет объекту быть итерируемым, что делает его поддерживаемым в циклах for и других конструкциях, требующих итерации.

# Каждый итератор должен иметь метод __next__, который возвращает следующий элемент последовательности. Если элементы закончились, метод должен возбуждать исключение StopIteration.

# Пример кода:
        
class MyRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start >= self.end:
            raise StopIteration # Вызываем исключение StopIteration
        current = self.start
        self.start += 1
        return current

# numbers = MyRange(1, 5)
# iterator = iter(numbers)  # Получаем итератор
# print(next(iterator))  # Выведет: 1
# print(next(iterator))  # Выведет: 2
# print(next(iterator))  # Выведет: 3
# print(next(iterator))  # Выведет: 4
# print(next(iterator))  # Выведет: StopIteration исключение


# __contains__ - Проверка наличия элемента

# Метод __contains__ позволяет нам определить поведение оператора in, который используется для проверки наличия элемента в объекте.

# Пример кода:

class Team:
    def __init__(self, members):
        self.members = members

    def __contains__(self, member):
        return member in self.members

# team_A = Team(['Alice', 'Bob', 'Charlie'])
# print('Alice' in team_A)  # Выведет: True
# print('Dave' in team_A)   # Выведет: False


# __call__ - Вызов объекта как функции

# Метод __call__ позволяет нам вызывать экземпляр класса, как если бы он был функцией.

# Пример кода:

class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, x):
        return self.factor * x

# double = Multiplier(2)
# print(double(5))  # Выведет: 10

# Создайте класс Matrix для представления матриц. Реализуйте магические методы __init__, __add__, __sub__, __mul__, __str__ и __eq__. Проверьте операции сложения, вычитания, умножения и сравнения для объектов этого класса.

class Macro:
    def __init__(self, rows, colums, element):
        self.rows = rows
        self.colums = colums
        self.element = element

    def __add__(self, other):
        if self.rows != other.rows or self.colums != other.colums:#Эта строка проверяет, имеют ли матрицы одинаковые размеры. Если хотя бы количество строк или количество столбцов не совпадает, вызывается исключение 
            raise ValueError("Нельзя сложить матрицы разных размеров.")
        new_elements = [
            [self.elements[i][j] + other.elements[i][j] for j in range(self.columns)]
        for i in range(self.rows)
        ]

        return Matrix(self.rows, self.columns, new_elements)
    

# Пример использования
matrix1 = Matrix(2, 3, [[1, 2, 3], [4, 5, 6]])
matrix2 = Matrix(2, 3, [[7, 8, 9], [10, 11, 12]])

# Сложение матриц
sum_matrix = matrix1 + matrix2
print("Сумма матриц:")
print(sum_matrix)
print()




# 
# class Matrix:
#     def __init__(self, a11, a12, a21, a22):
#         self.rows = 2
#         self.columns = 2
#         self.elements = [[a11, a12], [a21, a22]]

#     def __add__(self, other):
#         if isinstance(other, Matrix) and self.rows == other.rows and self.columns == other.columns:
#             new_elements = [
#                 [self.elements[i][j] + other.elements[i][j] for j in range(self.columns)]
#                 for i in range(self.rows)
#             ]
#             return Matrix(*new_elements)
#         else:
#             raise ValueError("Нельзя сложить матрицы разных размеров.")

#     def __sub__(self, other):
#         if isinstance(other, Matrix) and self.rows == other.rows and self.columns == other.columns:
#             new_elements = [
#                 [self.elements[i][j] - other.elements[i][j] for j in range(self.columns)]
#                 for i in range(self.rows)
#             ]
#             return Matrix(*new_elements)
#         else:
#             raise ValueError("Нельзя вычесть матрицы разных размеров.")

#     def __mul__(self, other):
#         if isinstance(other, Matrix) and self.columns == other.rows:
#             new_elements = [
#                 [sum(self.elements[i][k] * other.elements[k][j] for k in range(self.columns))
#                  for j in range(other.columns)]
#                 for i in range(self.rows)
#             ]
#             return Matrix(*new_elements)
#         else:
#             raise ValueError("Неподходящий размер для умножения матриц.")

#     def __str__(self):
#         return '\n'.join([' '.join(map(str, row)) for row in self.elements])

#     def __eq__(self, other):
#         return isinstance(other, Matrix) and self.elements == other.elements


# # Пример использования
# matrix1 = Matrix(1, 2, 3, 4)
# matrix2 = Matrix(5, 6, 7, 8)

# # Сложение матриц
# sum_matrix = matrix1 + matrix2
# print("Сумма матриц:")
# print(sum_matrix)
# print()

# # Вычитание матриц
# diff_matrix = matrix1 - matrix2
# print("Разность матриц:")
# print(diff_matrix)
# print()

# # Умножение матриц
# prod_matrix = matrix1 * matrix2
# print("Произведение матриц:")
# print(prod_matrix)
# print()

# # Сравнение матриц
# print("Сравнение матриц:")
# print(matrix1 == matrix2)  # False
# print(matrix1 == Matrix(1, 2, 3, 4))  # True


# dz
# Матрицы:
# Реализуйте класс Matrix для представления матриц. Реализуйте магические методы __init__, __add__, __sub__, __mul__, __str__, и __eq__. Протестируйте операции сложения, вычитания, умножения и сравнения для объектов этого класса.

