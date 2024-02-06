#Написать функцию is_year_leap, принимающую 1 аргумент — год, и возвращающую True, если год високосный, и False иначе.
"""i = int(input())
if (i % 4 == 0 and i % 100 != 0)or(i % 400 == 0):
    print('True')
else:
    print('False')"""

#Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12), и возвращающую время года, которому этот месяц принадлежит (зима, весна, лето или осень).



"""
    Программа Python для фильтрации нечетных чисел
    в списке, используя функцию filter()
"""

# список чисел
numbers = [1, 2, 4, 5, 7, 8, 10, 11]

# функция, которая проверяет числа
"""def filter_odd_num(in_num):
    if(in_num % 2) == 0:
        return True
    else:
        return False"""

# Применение filter() для удаления нечетных чисел
"""out_filter = filter(filter_odd_num, numbers)

print("Тип объекта out_filter: ", type(out_filter))
print("Отфильтрованный список: ", list(out_filter))"""

#Написать программу, в которой есть главный класс Games со динамическим полем game, year,// опишите конструктор присваивающий значение полю game, year, также опишите метод getName, который возвращает имя игры
"""class Game:
    def __init__(self, name, year):
        self.game = name
        self.year = year

    def getName(self):
        return self.game

# Пример использования
if __name__ == "__main__":
    # Создаем объект класса Game
    my_game = Game("SoloKnight", 2024)

    # Выводим имя игры с использованием метода getName
    print("game title", my_game.getName())
"""
#if __name__ == "__main__": - Эта конструкция проверяет, является ли текущий файл основным программным модулем (то есть файл, который был запущен, а не импортирован как модуль в другом файле). Если файл запущен напрямую, а не импортирован, то код внутри этого блока будет выполняться.

# my_game = Game("Моя игра", 2022) - Здесь создается объект класса Game. Мы используем конструктор класса Game, передавая два аргумента: строку "Моя игра" в качестве названия игры и число 2022 в качестве года. Этот объект сохраняется в переменной my_game.

# Таким образом, блок кода после if __name__ == "__main__": представляет собой пример использования созданного класса Game. В нем создается объект my_game с определенным названием игры и годом, и далее вы можете использовать этот объект для доступа к методам и полям класса, например, вызвать my_game.getName() для получения названия игры.

"""# class Gun:
#     name = "" 
#     damage = 0       
# class FreGun(Gun):
#     pass

# class Figun(Gun):
#     pass

# The_rifle = Gun()
# The_rifle.name = "Ar_15"
# The_rifle.damage = 46
# print(f"gun name: {The_rifle.name}, damage gun: {The_rifle.damage},")"""



# Создать класс Автомобиль от которого будут наследоватся три под класса Пикап, Седан, Минивен/. У класса будут параметры скорость, вес, цвет. У его подклассов будут один свой уникальный параметр которого нету у других. И затем создайте для каждого лодкласса по одному эгзампляру


#Создаем класс Автомобиль
class The_car:
    speed = 0
    color = ""
    weight = 0
#Создаем класс Пикап
class pickup(The_car):
    passability = 0 
    # проходимость 
#Создаем класс Минивен
class minivan(The_car):
    Capacity = 0
    #вместимость
#Создаем класс Седан
class sedan(The_car):
    cost = 0
    # стоимость


#создаем экзампляр для каждого класса 
Car = The_car()
Car.color = "Blue"
Car.weight = 1500
Car.speed = 75

truck = pickup()
truck.passability = 45

tuc_tuc = minivan()
tuc_tuc.Capacity = 500


hardtop = sedan()
hardtop.cost = 2700000

#вызываем класс Автомобиль
print(f"цвет автомобиля {Car.color}, вес {Car.weight}/кг, скорость км/час  {Car.speed}")
#вызываем класс Пикап
print(f"проходимость {truck.passability}/km")
#вызываем класс Минивен
print(f"вместимость {tuc_tuc.Capacity}/kg")
#вызываем класс Седан
print(f"цена:{hardtop.cost}$")


#Создать класс Animal от которого будут наследоватся два под класса Хищник, Траваядный.// От класса Хищник наследуется класс Лев, Волк и Тигр.//  От класса Траваядный наследуется класс Корова, Коза и Олень. И у каждого будут свои уникалные параметры. Общие параметры вынести в родителский класс

class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
    
    def make_sound(self):
        print(f"{self.name} говорить {self.sound}")

class Predator(Animal):
    def __init__(self, name, sound, hunting_skill):
        super().__init__(name, sound)
        self.hunting_skill = hunting_skill
    def show_skill(self):
        print(f"{self.name} имеет {self.hunting_skill} охотничий навык ")

class Herbivore(Animal):
    def __init__(self, name, sound, grazing_location):
        super().__init__(name, sound)
        self.grazing_location = grazing_location

    def show_location(self):
        print(f"{self.name} обитает чаще всего в {self.grazing_location}")


class Lion(Predator):
    def __init__(self, name, hunting_skill):
        super().__init__(name, "Ррррав", hunting_skill)


class Wolf(Predator):
    def __init__(self, name, hunting_skill):
        super().__init__(name, "ауу", hunting_skill)


class Tiger(Predator):
    def __init__(self, name, hunting_skill):
        super().__init__(name, "Арррр", hunting_skill)


class Cow(Herbivore):
    def __init__(self, name, grazing_location):
        super().__init__(name, "муу", grazing_location)


class Goat(Herbivore):
    def __init__(self, name, grazing_location):
        super().__init__(name, "бее", grazing_location)


class Deer(Herbivore):
    def __init__(self, name, hunting_skill):
        super().__init__(name, "мугх", hunting_skill)


#лев
lion = Lion("Симба", "отличный")
lion.make_sound()
lion.show_skill()

#корова

cow = Cow("Метти", "луггу")
cow.make_sound()
cow.show_location()





    