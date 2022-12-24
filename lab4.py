# Задание 1
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = []
def odd_index(list):
    for i in range(len(list)):
        if i % 2 == 0:
            result.append(list[i])
    print(result)
odd_index(list)

# Задание 2
any_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = []
def more(list):
    for i in range(len(list)):
        if list[i] > list[i - 1]:
            result.append(list[i])
    print(result)
more(any_list)

# Задание 3
list_a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def replace(list):
    max_ = list.index(max(list))
    min_ = list.index(min(list))
    list[max_], list[min_] = list[min_], list[max_]
    print(list)
replace(list_a)

# Задание 4
n = int(input('Введите количество значений:'))
a = {}
b = [0] * 2 * n
for i in range(0,2 * n, 2):
    b[i] = input('Введите ключ:')
for i in range(1, 2 * n, 2):
    b[i] = input('Введите значение:')
for i in range(0, 2 * n, 2):
    a[b[i]] = b[i+1]
print(a)
h = input('Введите ключ, значение которого хотите получить:')
print(a[h])

# Задание 5
from figures import triangle_area
triangle_area()