
# В программировании, абстракция — это процесс скрытия 
# деталей реализации и предоставления пользователю 
# упрощенного интерфейса для взаимодействия. В Python 
# абстракция может проявляться на разных уровнях, начиная 
# от использования функций и классов до создания 
# пользовательских интерфейсов.



# Создайте абстрактный класс Subject с абстрактным методом study(). Затем создайте подклассы Math, Science, и History, реализовав метод study() для каждого предмета. Создайте объекты каждого класса и вызовите их методы study().

from abc import ABC, abstractmethod

class Subject(ABC):
    @abstractmethod
    def study(self):
        pass

class Math(Subject):
    def study(self):
        print("Студент в кабинете Математики")

class Science(Subject):
    def study(self):
        print("Студент в кабинете Науки")

class History(Subject):
    def study(self):
        print("Студент в кабинете Истории")

# Создаем объекты каждого класса и вызываем их методы study()
# math_subject = Math()
# science_subject = Science()
# history_subject = History()

# math_subject.study()
# science_subject.study()
# history_subject.study()


# Транспортные средства:
# Создайте абстрактный класс Vehicle с абстрактными методами start() и stop(). Затем создайте подклассы Car, Motorcycle и Bicycle, реализовав методы start() и stop() для каждого транспортного средства. Создайте объекты каждого класса и вызовите их методы.

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass 

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def start(self):
        print("машина завелась")
    def stop(self):
        print("машина остановилась")


class Motorcycle(Vehicle):
    def start(self):
        print("мотоцикл завелся")
    def stop(self):
        print("мотоцикл остановился")


class Bicycle(Vehicle):
    def start(self):
        print("велосипед тронулся")
    def stop(self):
        print("велосипед остановился")

# создаем обьекты классов
car1 = Car()
Motorcycle1 = Motorcycle()
bicycle1 = Bicycle()

# вызываем методы study
# car1.start()
# car1.stop()
# Motorcycle1.start()
# Motorcycle1.stop()
# bicycle1.start()
# bicycle1.stop()


# Банковские счета:
# Создайте абстрактный класс BankAccount с абстрактными методами deposit() и withdraw(). Затем создайте подклассы SavingsAccount и CheckingAccount, реализовав методы для каждого типа счета. Создайте объекты каждого класса и вызовите их методы.

class BankAccount(ABC):
    @abstractmethod
    def deposit(self):
        pass

    @abstractmethod
    def withdraw(self):
        pass

# Сберегательный счет
class SavingsAccount(BankAccount):
    def deposit(self, amount):
        self.sum = amount
        print(f"ваш депозит; {self.sum}")

    def withdraw(self, derive):
        self.derive = derive
        if self.derive < self.sum:
            self.count = self.sum - self.derive
            print(f"вы вывели: {self.derive} ваш текущий счет {self.count}")
        else:
            print(f"На вашем счету недостаточно средств")


# Текущий счет
class CheckingAccount(BankAccount):
    def deposit(self, amount):
        self.balance = amount
        print(f"ваш депозит; {self.balance}")

    def withdraw(self, derive):
        self.derive = derive
        if self.derive < self.balance:
            self.count = self.balance - self.derive
            print(f"вы вывели: {self.derive} ваш текущий счет {self.count}")
        else:
            print(f"На вашем счету недостаточно средств")



#создаем экземпляр класса 
Account = CheckingAccount()
money = SavingsAccount()

Account.deposit(600)
Account.withdraw(1000)
money.deposit(5000)
money.withdraw(3000)
