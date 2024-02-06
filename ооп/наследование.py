# Напишите класс Steamship(пароход). Создайте следующие характеристики (полей) объекта: make (марка), model, year, max_speed, odometer, is_swimmng и методы имитирующих поведение парохода 
# get_swimning (плавает), stop_swimming
# (остановка), info_about_swim(информация об плавание), info_about_steamship(информация об пароходе). Метод get_swimming должен изменить  is_swimmng на True, а stop_swimming на False. По
# умолчанию поле is_swimmng= False. Метод get_swimmng должен принимать расстояние плаванья и
# изменять показания одометра (километраж). Создайте 1 объект класса и используйте
# все методы класса.

class Steamship():
    def __init__(self, model, year, max_speed, odometer, is_swimmng):
       self.model = model # model
       self.year = year  # год выпуска
       self.year = max_speed   #максимальная скорость
       self.year = odometer #Пройденное расстояние
       self.year = is_swimmng #плавает
    def get_swimning(Steamship):
        print("плавает")

    def stop_swimming(Steamship):
        print("стоит")

    def info_about_swim(Steamship):
        print("information")

    def info_about_steamship(Steamship):
        print("информация об пароходе")


class SwimmingOdometer:
    def __init__(self):
        self.is_swimming = False
        self.odometer = 0

    def start_swimming(self):
        if not self.is_swimming:
            self.is_swimming = True
            print("Начало плавания")

    def stop_swimming(self):
        if self.is_swimming:
            self.is_swimming = False
            print("Завершение плавания")

    def get_swimming(self, distance):
        if self.is_swimming:
            self.odometer += distance
            print(f"Проплыто {distance} километров. Всего: {self.odometer} километров")
        else:
            print("Вы должны начать плавание, прежде чем фиксировать расстояние.")

# Создаем объект класса
swimming_tracker = SwimmingOdometer()

# Начинаем плавание
swimming_tracker.start_swimming()

# Записываем плавание на расстояние 2 километра
swimming_tracker.get_swimming(2)

# Завершаем плавание
swimming_tracker.stop_swimming()

# Попробуем записать плавание после завершения
swimming_tracker.get_swimming(3)
