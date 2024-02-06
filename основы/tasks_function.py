#Создайте базовый класс Shape, который имеет метод area(). Затем создайте подклассы Circle и Rectangle, переопределив метод area() для каждой фигуры. Создайте несколько объектов каждого класса и вызовите их методы area().

import math

class Shape:
    def Shape(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return self.width * self.height
    

# Создаем объекты
circle1 = Circle(5)
circle2 = Circle(7)

rectangle1 = Rectangle(4, 6)
rectangle2 = Rectangle(3, 9)

# Вызываем методы area()
print(f"Площадь круга 1: {circle1.area()}")
print(f"Площадь круга 2: {circle2.area()}")

print(f"Площадь прямоугольника 1: {rectangle1.area()}")
print(f"Площадь прямоугольника 2: {rectangle2.area()}")

#Создайте базовый класс Animal с методом speak(). Создайте подклассы Dog, Cat и Cow, переопределив метод speak() для каждого класса. Создайте несколько объектов каждого класса и вызовите их методы speak().


class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"
    
class Cow(Animal):
    def speak(self):
        return "Moo!"
    
# Создаем обьекты 
    
cat1 = Cat()
dog1 = Dog()
cow = Cow()

# Вызов методов speak
print(cat1.speak())
print(dog1.speak())
print(cow.speak())

# Создайте базовый класс Car с методами start_engine() и stop_engine(). Затем создайте подклассы ElectricCar и GasolineCar, переопределив методы start_engine() и stop_engine() для каждого типа автомобиля. Создайте объекты каждого класса и вызовите их методы.

class Car:
    def start_engine(self):
        pass

    def stop_engine(self): 
        pass

class ElectricCar(Car):
    def start_engine(self):
        return "бесшумно"
    
    def stop_engine(self):
        return "плавно"
    
class GasolineCar(Car):
    def start_engine(self):
        return "почти громко"
    
    def stop_engine(self):
        return "резко"
    

car2 = ElectricCar()
car3 = GasolineCar()

print("Электрокар стартует ", car2.start_engine())
print("Электрокар останавливается ", car2.stop_engine())

print("Бензиновый автомобиль стартует ", car3.start_engine())
print("Бензиновый автомобиль останавливается ",car3.stop_engine())

        