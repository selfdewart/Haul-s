# class Games:
#     def init(self, game, year):
#         self.name = game
#         self.year = year
#     def getName2(self):
#          print(self.name, self.year)

# class PCGames(Games):
#     def getName2(self):
#         print(f"Videocard {self.name} год выпуска {self.year}")

# class PS4Games(Games):
#     def getName2(self):
#         print(f"120fps {self.name} год выпуска {self.year}")

# class XboxGames(Games):
#     def getName2(self):
#         print(f"cheapness {self.name} год выпуска {self.year}")

# class MobileGames(Games):
#     def getName2(self):
#         print(f"мобилььность {self.name} год выпуска {self.year}")


# getGame = PCGames("Call off duty", 2017)
# getGame.getName2()

class Steamship:
    def __init__(self, make, model, year, max_speed):
        self.make = make
        self.model = model
        self.year = year
        self.max_speed = max_speed
        self.odometer = 0
        self.is_swimming = False

    def get_swimming(self, distance):
        if not self.is_swimming:
            self.is_swimming = True
            self.odometer += distance
            print(f"{self.make} {self.model} начал плавание. Проплыто {distance} километров.")
        else:
            print(f"{self.make} {self.model} уже плывет.")

    def stop_swimming(self):
        if self.is_swimming:
            self.is_swimming = False
            print(f"{self.make} {self.model} остановился.")
        else:
            print(f"{self.make} {self.model} не плавает в данный момент.")

    def info_about_swim(self):
        if self.is_swimming:
            print(f"{self.make} {self.model} плавает на скорости {self.max_speed} км/ч.")
        else:
            print(f"{self.make} {self.model} не плавает в данный момент.")

    def info_about_steamship(self):
        print(f"Информация о пароходе {self.make} {self.model}:")
        print(f"Год выпуска: {self.year}")
        print(f"Максимальная скорость: {self.max_speed} км/ч")
        print(f"Пройденное расстояние: {self.odometer} километров")
        self.info_about_swim()

# Создаем объект класса Steamship
steamship = Steamship("Steamy", "Model-X", 2020, 30)

# Вывод информации о пароходе
steamship.info_about_steamship()

# Начинаем плавание
steamship.get_swimming(10)

# Вывод информации о текущем состоянии
steamship.info_about_steamship()

# Останавливаем плавание
steamship.stop_swimming()

# Вывод информации после остановки
steamship.info_about_steamship()
