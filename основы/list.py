my_list = [1,2,3,4,5,6,]
my_list2 = ["hello", 'world']
my_list3 = ["H",4, "W", 7]
my_list4 = []
my_list5 = list()

# print(my_list[::-1])
# добавить 
my_list.append(5)

print(my_list)

#изменение списка
my_list[1] = 10
print(my_list)

# удаление удаление по позиции
my_list.pop(2) #указываем индекс (2) 
print(my_list)

# список начинается с конца
mind_list = [1,2,3,4,5,6]
print(mind_list[::-1])
# Cписки - изменяемый тип данных. Используются [] cкобки
# Кортеж - не изменяемый тип данных, по скорости чуть выше списков. Используются () cкобки
# Множества - изменяемый тип данных хранящий в себе уникальные обьекты в неотсортированном виде. Используются {} cкобки
# Замороженные множества- как и множества только не изменяемый тип данных

#сортировка списков
num =[4,3,2]#сортировка списка по возрастанию
num.sort()
print(num)

# найдите количество совпадений в списке используя переменную name
students = ['Baktiar', 'Sherdos','Sherdos', 'Alinur', 'Alinur']
name = input('Введите имя: ')
name_count = students.count(name)
print(name_count)

# Словари в Python предоставляют эффективный и 
# удобный способ работы с данными, особенно когда 
# требуется быстрый доступ к значениям по ключам.

# Создание словаря
мой_словарь = {"ключ1": "значение1", "ключ2": "значение2", "ключ3": "значение3"}

# Получение значения по ключу
значение = мой_словарь["ключ1"]
print(значение)  # Вывод: значение1

# Добавление нового элемента
мой_словарь["новый_ключ"] = "новое_значение"

# Изменение значения по ключу
мой_словарь["ключ2"] = "новое_значение2"

# Удаление элемента по ключу
del мой_словарь["ключ3"]

# Проверка наличия ключа в словаре
# если "ключ1" в мой_словарь:
print("Ключ1 есть в словаре")