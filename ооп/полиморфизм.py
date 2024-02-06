# class University:
#     def __init__(self, university_name):
#         self.university_name = university_name
#         self.departments = {}

#     def add_department(self, department_name):
#         self.departments[department_name] = []

# class Student:
#     def __init__(self, firstname, lastname):
#         self.firstname = firstname
#         self.lastname = lastname

#     # This method should be used to add a student to a department in the University class
#     def add_student(self, university, department_name, student):
#         university.departments[department_name].append(student)

# # Create a University instance
# university1 = University("My University")

# # Create some student instances
# student1 = Student("Иван", "Иванов")

# # Add a department to the University
# university1.add_department("Факультет математики")

# # Add a student to a department in the University
# student1.add_student(university1, "Факультет математики", student1)


# class Zoo():
    
#     def init(self,name):
#         self.animals = []
#         self.staff = []
#         self.name = name
    
#     def add_animal(self, animal):
#         self.animals.append(animal)
    
#     def add_staf(self, staf):
#         self.staff.append(staf)
    
#     def get_info(self):
#         print(f'Zoo name - {self.name} Staff - {self.staff}, animals - {self.animals}')
    
# class Animal():
#     def init(self, age, high, area) -> None:
#         self.age = age
#         self.high = high
#         self.area = area
        

# class Lion(Animal):
#     status = 'predator'
#     food = 'meat'
#     animal = 'lion'
    
#     def init(self, charater,age, high, area):
#         self.charater = charater
#         super().init(age, high, area)
        
#     def str(self) -> str:
#         return f'[animal - {self.animal}, meail - {self.food}, status - {self.status}, age - {self.age}, high - {self.high}, age - {self.area}, charater - {self.charater} ], ' 
        
# class Staff():
#     def init(self, hmyw, name) -> None:
#         self.how_mach_years_work = hmyw
#         self.name = name


from abc import ABC, abstractmethod


class Weapon():
    
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
    

class Person(AbstractPerson):
    
    def __init__(self, name,type_attack, hp, damage) -> None:
        self.name  = name
        self.type_attack = type_attack
        self.hp = hp
        self.damage = damage
        self.weapons = []
        self.balans = 1000
        
    def attack(self, enemy):
        print(f'Атакует - {self.name} {self.type_attack}')
        damage = 0
        for i in self.weapons:
            damage += i.damage
        enemy.hp -= damage + self.damage
        if enemy.hp <= 0:
            print(f'{enemy.name} Умер')
        
    def __str__(self):
        return f'У {self.name} {self.hp} жизней. баланс {self.balans}'
        
    def buy_weapon(self,weapon):
        if self.balans < weapon.price:
            print('недостаточно монет')
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


robo = Person('Робот','удар мечом',250, 35)

warrior1 = Warrior('Артур','удар мечом',250, 135)
warrior2 = Warrior('Ланселот', 'колить шпагой',245,50)
archer1 = Archer('Робин Гуд', 'выстрил из лука', 120, 20)
archer2 = Archer('Ария', 'выстрел из арбалета', 110, 55)
wizard1 = Wizard('Силвия' , 'удар грома', 100, 90)
wizard2 = Wizard('Мерлин', 'огненный шар', 130, 70)
list_per = [warrior1, archer2, wizard1, warrior2, archer1, wizard2]
sword = ColdWeapon('Меч', 50, 100)


warrior1.attack(robo)
print(robo)
warrior1.attack(robo)
print(robo)
warrior1.buy_weapon(sword)
print(warrior1)