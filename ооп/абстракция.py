# class Car:
#     def __init__(self, make, model):
#         self.make = make
#         self.model = model

#     def start_engine(self):
#         print(f"{self.make} {self.model} engine started.")

# my_car = Car("Toyota", "Camry")
# my_car.start_engine()


from turtle import *

# Абстракция
from abc import ABC, abstractmethod
# class Figure(ABC):
#     @abstractmethod
#     def square(self):
#         pass

#     @abstractmethod
#     def draw(self):
#         pass


# class Quadrate(Figure):
#     def __init__(self, a):
#         self.a = a
#     def square(self):
#         print(self.a * self.a)
#     def draw(self):
#         for i in range(4):
#             forward(self.a)
#             left(90)
#         input()





"""class Book(ABC):
    def __init__(self, title, author):
        self.title = title
        self.author = author

    @abstractmethod
    def get_summary(self):
        pass

class Fiction(Book):
    def get_summary(self):
        print(f'"{self.title}" - роман в стиле исторический фикшн, автор - {self.author}')

class NonFiction(Book):
    def get_summary(self):
        print(f'"{self.title}" - книга в стиле нон фикшн, автор - {self.author}')

class Poetry(Book):
    pass

fiction_book = Fiction("Террор", "Дэн Симмонс")
nonfiction_book = NonFiction("Как писать книги", "Стивен Кинг")
fiction_book.get_summary()
nonfiction_book.get_summary()"""



# from abc import ABC, abstractmethod

# class Animal(ABC):
#     @abstractmethod
#     def speak(self):
#         pass

# class Dog(Animal):
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         print(f"{self.name} говорит Гав-гав")

# class Cat(Animal):
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         print(f"{self.name} говорит Мяу-мяу")

# class Cow(Animal):
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         print(f"{self.name} говорит Муу")

# # Создайте экземпляры каждого класса
# dog = Dog("Барсик")
# cat = Cat("Мурзик")
# cow = Cow("Буренка")

# # Вызовите метод speak для каждого экземпляра
# dog.speak()
# cat.speak()
# cow.speak()
"""
# from turtle import *


# class Figure(ABC):
#     @abstractmethod
#     def square(self):
#         pass

#     @abstractmethod
#     def draw(self):
#         pass


# class Quadrate(Figure):
#     def __init__(self, a):
#         self.a = a
#     def square(self):
#         print(self.a * self.a)
#     def draw(self):
#         for i in range(4):
#             forward(self.a)
#             left(90)
#         input()

# class Circle(Figure):
#     def __init__(self, name):
#         self.name = name
#     def square(self):
#         print((self.name * 2) * 3.14)
#     def draw(self):
#         for i in range(250):
             forward(self.name)
             left(90)
        input()

    

 Создание экземпляра класса Quadrate
 quadrate = Quadrate(5)  # Здесь 5 - длина стороны квадрата

 Вызов метода square для вычисления площади квадрата
 quadrate.square()  # Выведет площадь квадрата

 Вызов метода draw для отрисовки квадрата (при условии, что у вас есть библиотека, поддерживающая forward и left)
 quadrate.draw()  # Нарисует квадрат и остановит выполнение программы
"""


# 
# В программировании, абстракция — это процесс скрытия 
# деталей реализации и предоставления пользователю 
# упрощенного интерфейса для взаимодействия. В Python 
# абстракция может проявляться на разных уровнях, начиная 
# от использования функций и классов до создания 
# пользовательских интерфейсов.

# Функции: Использование функций позволяет скрыть детали реализации кода. Пользователь вызывает функцию, не беспокоясь о том, как она работает внутри.

def add_numbers(a, b):
    return a + b

result = add_numbers(3, 5)

# Классы и объекты: ООП (объектно-ориентированное программирование) предоставляет механизм абстракции через классы. Пользователь работает с объектами, не зная детали их реализации.
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start_engine(self):
        print(f"{self.brand} {self.model} engine started.")

# my_car = Car("Toyota", "Camry")
# my_car.start_engine()


from abc import ABC, abstractmethod


class Weapon:

    def __init__(self, name, damage, price):
        self.name = name
        self.damage = damage
        self.price = price


class MagicalWeapon(Weapon):
    pass


class ColdWeapon(Weapon):
    pass


class SWeapon(Weapon):
    pass


class AbstractPerson(ABC):

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def info(self):
        pass


class Person(AbstractPerson):

    def __init__(self, name, type_attack, hp, damage):
        self.name = name
        self.type_attack = type_attack
        self.hp = hp
        self.damage = damage
        self.weapons = []
        self.balans = 0

    def attack(self, enemy):
        print(f'Атакует - {self.name} {self.type_attack}')
        damage = 0
        for i in self.weapons:
            damage += i.damage
        enemy.hp -= damage + self.damage
        if enemy.hp <= 0:
            print(f'{enemy.name} Умер')

    def info(self):
        print(f'У {self.name} {self.hp} жизней. Баланс {self.balans}')

    def buy_weapon(self, weapon):
        if self.balans < weapon.price:
            print('Недостаточно монет')
        else:
            print(f'{self.name} купил {weapon.name} за {weapon.price}')
            self.balans -= weapon.price
            self.weapons.append(weapon)


class Warrior(Person):
    pass


class Archer(Person):
    pass


class Wizard(Person):
    pass

# robo = Person('Робот', 'удар мечом', 250, 35)

# warrior1 = Warrior('Артур', 'удар мечом', 250, 35)
# warrior2 = Warrior('Ланселот', 'колить шпагой', 245, 50)
# archer1 = Archer('Робин Гуд', 'выстрел из лука', 120, 20)
# archer2 = Archer('Ария', 'выстрел из арбалета', 110, 55)
# wizard1 = Wizard('Силвия', 'удар грома', 100, 90)
# wizard2 = Wizard('Мерлин', 'огненный шар', 130, 70)
# list_per = [warrior1, archer2, wizard1, warrior2, archer1, wizard2]
# sword = ColdWeapon('Меч', 50, 100)

# warrior1.buy_weapon(sword)
# warrior1.info()
# warrior1.attack(robo)
# robo.info()




# Создайте класс Student с атрибутами name, age и методом study(). Затем создайте класс University с атрибутами name и students, и методами admit_student(student) и list_students(). Создайте несколько объектов студентов и добавьте их в университет

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def study(self):
        print(f"{self.name} учится")

class University:
    def __init__(self, name):
        self.name = name
        self.students = []

    def admit_student(self, student):
        self.students.append(student) #добовляем студента в список students
        print(f"{student.name} был(а) принят в {self.name}.")

    def list_students(self):
        print(f"студенты {self.name}")
        for student in self.students:
            print(f"- {student.name}")

# # Создаем объекты студентов
# student1 = Student("Alice", 20)
# student2 = Student("Bob", 22)
# student3 = Student("Charlie", 21)

# # Создаем объект университета
# university = University("Примерного университет")

# # Добавляем студентов в университет
# university.admit_student(student1)
# university.admit_student(student2)
# university.admit_student(student3)

# # Выводим список студентов в университете
# university.list_students()
            

# Создайте класс Book с атрибутами title, author и методами get_info(). Затем создайте класс Library с атрибутами name и books, и методами add_book(book) и list_books(). Создайте несколько объектов книг и добавьте их в библиотеку.
            
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_info(self):
        return f"{self.title} by {self.author}"

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"{book.title} has been added to {self.name}.")

    def list_books(self):
        print(f"Books in {self.name}:")
        for book in self.books:
            print(f"- {book.get_info()}")

# Создаем объекты книг
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
book3 = Book("1984", "George Orwell")

# Создаем объект библиотеки
library = Library("City Library")

# Добавляем книги в библиотеку
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Выводим список книг в библиотеке
library.list_books()

# Создайте класс BankAccount с атрибутами balance и методами deposit(amount) и withdraw(amount). Создайте объект банковского счета, внесите и снимите с него средства.

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Внесено {amount} руб. Новый баланс: {self.balance} руб.")
        else:
            print("Ошибка: Сумма для внесения должна быть положительной.")

    def withdraw(self, amount):
        if amount > 0 and amount < self.balance:
            self.balance -= amount
            print(f"Снято {amount} руб. Новый баланс: {self.balance} руб.")
        elif amount <= 0:
            print("Ошибка: Сумма для снятия должна быть положительной.")
        else:
            print("Ошибка: Недостаточно средств на счете.")

# Создаем объект банковского счет
my_account = BankAccount(balance=1000)

#вносим средства
my_account.deposit(500)

#снимаем средства 
my_account.withdraw(200)

# Попытка снять больше средств, чем есть на счете
my_account.withdraw(1500)