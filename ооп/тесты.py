# class SpeakAnymal():
#     def animal(any1):
#         any1 == "Dog"
    
#     def make_sound(any1):
#         pass




# class Rabbit:
#     def __init__(self, name):
#         self.name = name

#     @staticmethod
#     def make_sound(name):
#         return f"{name} Meow!"

# # Пример использования:
# rabbit_name = "Кошка"
# rabbit_sound = Rabbit.make_sound(rabbit_name)
# print(rabbit_sound)  # Выведет "Барашек шшш-шшш!"


# """.[Создайте класс Person.] В конструкторе он принимает name, surname. Создайте метод info_about_human, который возращает name, surname. Создайте 3 экземпляра класса и вызовите методы."""
# class Person(): #Создайте класс Person.
#     def __init__(self, name, surname): #В конструкторе он принимает name, surname.
#         self.name = name
#         self.surname =surname
#     def info_about(self):  #метод info_about_human, который возращает name, surname
#         print(f"{self.name} {self.surname}")
# #ввод данных
# person1 = Person("Саша", "Панфилов")
# person2 = Person("Иван", "Викторович")
# person3 = Person("Ирина", "Виноградовна")

# #вывод данных
# person1.info_about()
# person2.info_about()
# person3.info_about()

"""20. Напишите класс Сonstructor, которое имитирует строительство жилого дома. В конструкторе мы передаем сколько этажей мы хотим построить. Затем пишем метод build, который строит наш дом пока мы не дойдем до этажа которую мы хотим построить которую мы передавали в  конструкторе. И также создайте магический метод __str__, для вывода данных нашего класса."""
class Constructor:
    def __init__(self, floors_to_build):
        self.total_floors = floors_to_build
        self.current_floor = 0

    def build(self):
        if self.current_floor < self.total_floors:
            self.current_floor += 1
            print(f"Building floor {self.current_floor}")
        else:
            print("The house is already built!")

    def __str__(self):
        return f"House construction progress: {self.current_floor}/{self.total_floors} floors built"

# Пример использования класса
if __name__ == "__main__":
    house = Constructor(3)  # Создаем объект класса с указанием количества этажей
    print(house)  # Выводим информацию о текущем состоянии строительства
    house.build()  # Строим первый этаж
    house.build()  # Строим второй этаж
    house.build()  # Строим третий этаж
    house.build()  # Попытка строить ещё один этаж (превышение указанного количества)
    print(house)  # Выводим информацию о текущем состоянии строительства
