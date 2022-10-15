# Реализуйте алгоритм перемешивания списка.

N = 10

import random

list_first = []
for i in range(N):
    list_first.append(random.randint(-N, N))
print('Случайно сгенерированный список:')
print(list_first)


list_new_index = []
list_new_index.append(random.randint(0, N - 1))
for i in range(1, N):
    list_new_index.append(random.randint(0, N - 1))
    while list_new_index.count(list_new_index[i]) > 1:
        list_new_index.remove(list_new_index[i])
        list_new_index.append(random.randint(0, N - 1))
print('Новые индексы для списка')
print(list_new_index)
        
list_second = []
for i in list_new_index:
    list_second.append(list_first[i])
print('Перемешанный список')
print(list_second)   

