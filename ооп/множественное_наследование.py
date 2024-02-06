# class Telephone():
#     def call():
#         pass

# class Telephone2(Telephone):
#     def send_message():
#         pass

# class Telephone3():
#     def get_instagram():
#         pass

# class Phone():
#         pass

# class PhoneMixin(Telephone, Telephone2):pass

# class SmartPhone(Telephone3):
#     pass

# class Grandpa_phone(Telephone):
#     pass


# множественное наследование 
class Doctor:

    def can_cure(self):
        print("I am doctor")


    def can_build(self):
        print("я доктор я тоже могу строить но не очень")

class Builder:
    def can_build(self):
        print("I am builder I can building")

class Person(Builder, Doctor):
    def can_build(self):
        print("I am human and i m aslo to builder")

# print(Person.__mro__ )
# c = Person()
# c.can_build()

# # 

class Doctor:
    def __init__(self, degree):
        self.degree = degree

    def graduate(self):
        print("Ура я отучился на врача")


    def can_build(self):
        print("я доктор я тоже могу строить но не очень")

class Builder:
    def __init__(self, rank):
        self.rank = rank

    def graduate(self):
        print("Ура я отучился на строителя")

    def can_build(self):
        print("I am builder I can building")

class Person(Builder, Doctor):
    def __init__(self, rank, degree):
        super().__init__(rank)
        Doctor.__init__(self, degree)
    def __str__(self):
        return f" Person {self.rank} {self.degree}"

# вызов функции
# s = Person(5, 'spec')
# print(s)
    

class Goods:
    def __init__(self, name, weight, price):
        super().__init__()
        print("init Mixinlog")
        self.name = name
        self.weight = weight
        self.price = price

    def print_info(self):
        print(f"{self.name}, {self.weight}, {self.price}")

class MixinLog:
    ID = 0

    def __init__(self):
        print("init MixinLing")
        MixinLog.ID += 1
        self.id = MixinLog.ID
    
    def save_sell_log(self):
        print(f"{self.id}: товар был продан в 00:00 часов")

class NoteBook(Goods, MixinLog):
    pass

p = NoteBook("aser", 1.5, 30000)
p.print_info()
p.save_sell_log()
print(NoteBook.__mro__)

# В Python существует три типа наследования: одиночное, множественное и многоуровневое. Одиночное наследование - это когда дочерний класс наследует от одного родительского класса. Множественное наследование - это когда дочерний класс наследует от нескольких родительских классов. Многоуровневое наследование - это когда дочерний класс наследует от родительского класса, который, в свою очередь, наследует от другого родительского класса.