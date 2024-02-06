# условие
# if - else -elif
a = 10
b = 5 
if a > b:
   print("A больше чем В")
else:
   print("B больше чем A")

"""
# if (условие)
#     операторы если условие правильно
#     операторы если условие правильно
# else:
#     операторы если условие не правильно
#     операторы если условие не правильно
# """

# if True:
#    print("Условие которые всегда работает")

# if False:
#    print("Условие которые никогда не работает")

#    if "Baktiar" == "Baktiar":
#       print("они равны")
# else:
#    print("они не равны")

#задание

# age = int(input())
# age2 = int(input())
# if age > age2:
#    print("age")
# elif age < age2:
#    print("age2")
# else:
#    print("age2")

# number = int(input())
# if ((number % 2) == 0):
#    print("четное число")
# else:
#    print("нечетное число")

# login = input()
# password = input()
# if login == "root" and password == "123":
#    print("успешно")
# else:
#    print("Логин или пароль не правильный")

# a = int(input())
# if a < 5:
#    print("от 1 до 5")
# elif a < 10:
#    print("число от 5 до 10")
# elif a < 15:
#    print("число от 15 до 15")
# elif a < 20:
#    print("число от 15 до 20")
# else:
#    print("введенное число меньше 1 или больше 19")

# a = int(input())
# b = int(input())
# c = int(input())
# if b < a > c:
#    print(a)
# elif a < b > c:
#    print(b)
# else:
#    print(c)
   
#Пример 1: Итерация строки с помощью цикла for

str = "Python"  
for i in str:  
    print(i) 

#Пример 2: Программа для печати таблицы заданного числа.

list = [1,2,3,4,5,6,7,8,9,10]  
n = 5  
for i in list:  
    c = n*i  
    print(c)  

#Пример 1: Программа для печати чисел по порядку.

for i in range(10):  
    print(i,end = ' ') 

#Пример 2: Программа для печати таблицы заданного числа.

# n = int(input("Enter the number "))  
# for i in range(1,11):  
#     c = n*i  
#     print(n,"*",i,"=",c) 

#Мы также можем использовать функцию range() с последовательностью чисел. Функция len() сочетается с функцией range(), которая выполняет итерацию по последовательности с использованием индексации. Рассмотрим следующий пример.

list = ['Peter','Joseph','Ricky','Devansh']  
for i in range(len(list)):  
    print("Hello",list[i])  

#Пример

# n=2  
# while 1:  
#     i=1;  
#     while i<=10:  
#         print("%d X %d = %d\n"%(n,i,n*i));  
#         i = i+1;  
#     choice = int(input("Do you want to continue printing the table, press 0 for no?"))  
#     if choice == 0:  
#         break;      
#     n=n+1  


# str = "JavaTpoint"  
# for i in str:  
#     if(i == 'T'):  
#         continue  
#     print(i)  

# if and else
#Пример 1: Программа для проверки того, имеет ли человек право голосовать или нет.

age = int (input("Enter your age? "))  
if age>=18:  
    print("You are eligible to vote !!");  
else:  
    print("Sorry! you have to wait !!");  