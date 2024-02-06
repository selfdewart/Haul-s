#Функция sorted() - это универсальный инструмент для #повторяющимися структурами данных, включая наборы, 
#списки, кортежи и многое другое.

original_set = {5, 3, 1, 4, 2}
sorted_set = sorted(original_set)
print(sorted_set)


# Сортировка в порядке убывания
# Если вам нужно выполнить сортировку в порядке убывания, установите для параметра reverse значение `True:

original_set = {5, 3, 1, 4, 2}
sorted_set = sorted(original_set, reverse=True)
print(sorted_set)


set_one = (63, 3, 35, 4, 56)
set_two = list(set_one)

set_two.sort(reverse=True)
print(set_two)

# Если вы хотите использовать оба параметра key и reverse при сортировке набора, вы можете следовать тому же подходу, что и раньше, сначала преобразовав набор в список, а затем отсортировав список по обоим параметрам. Вот пример того, как это сделать:
my_set = {5, 1, 3, 2, 4}
my_list = list(my_set)


def custom_key(x):
    return -x


my_list.sort(key=custom_key, reverse=True)
print(my_list)