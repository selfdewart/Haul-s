#встроенные функции

# def square(x):
#     print(x**2)
#     return None 

def square(x):
    return x ** 2
a = square(square(3))
print(a)

# a = abs(-7)
# print(a)

# # max number
# b = max(4,abs(-90),6,min(80,200))
# print(b)

# def example():
#     print(1)
#     print(2)
#     return 'hello' # чтобы вывести hello обернем вызов принтом
#     print(3)
#     print(4)
# example()
# # print(example())

# def even(x):
#     if x%2 == 0:
#         return True
#     return False
# for i in range(1,11):
#     print(i,even(i))

# def factorial(x):
#     pr=1
#     for i in range(2, x+1):
#       pr=pr*i
#     return pr

# def sochet(n, k):
#     return factorial(n)/(factorial(k)*factorial(n-k))
# print(sochet(5,3))
square = lambda x: x**2

result = square(5)
print(result)

def printNumbers(*nums):
    for arg in nums:
        print(arg)

printNumbers(1,2)
printNumbers(1,2,3,4,5,6,7)
