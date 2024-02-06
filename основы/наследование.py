# функция super

class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def display_info(self):
        print(f"Brand: {self.brand}")

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)  # вызываем конструктор родительского класса
        self.model = model

    def display_info(self):
        super().display_info()  # вызываем метод родительского класса
        print(f"Model: {self.model}")

# Создаем объект класса Car
my_car = Car("Toyota", "Camry")

# Вызываем метод display_info() класса Car
my_car.display_info()



# Функция super() в Python используется для вызова методов или атрибутов из родительского класса в подклассе. Это позволяет избежать явного указания имени родительского класса и делает код более гибким при изменении иерархии классов. super() обычно используется внутри методов подкласса, например, в конструкторе __init__, чтобы вызвать конструктор родительского класса и инициализировать общие атрибуты.

# Пример использования super():

 
class Parent:
    def __init__(self, name):
        self.name = name

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)  # Вызов конструктора родительского класса
        self.age = age

child = Child("Alice", 10)
print(child.name)  # Общий атрибут из родительского класса
print(child.age)   # Уникальный атрибут из подкласса