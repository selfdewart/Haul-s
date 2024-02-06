# number = input()
# print(number, number, number, sep = '\n')


purchase = input()
price = int(input())
product = int(input())
money = int(input())
print("Чек")
print(purchase, ' - ', product, "кг", ' - ', price, 'руб/кг', sep = "")
print("Итого: ", price * product, 'руб', sep = "")
print('Внесено: ', money, "руб", sep = "")
print("Сдача: ", money - price * product, "руб", sep = "")