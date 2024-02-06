class Test():
    name = "itrun"   # публичный
    _lastname = "itrun"  # _защищенный
    __adress = "itrun"   # __приватный

    def getInfo():
        print("Информация")


# cоздайте класс студент, с переменными имя возраст и адресс. возраст и адресс приватные
# cоздайте приватный метод внутри класс с названием getInfo(). Напиши описание про студента
class User():
    def __init__(self, name, age, address):
        self.name = name
        self.__age = age
        self.__address = address
    def getInfo(self):
        print("информация")
        print(self.name, self.__age, self.__address)

user1 = User("Имя", 20, "Osh") # экзепляр
user2 = User("Имя", 30, "Bishkek")
user2.name = "namw"
user2.getInfo()
user2.getInfo()

