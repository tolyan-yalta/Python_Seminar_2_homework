# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции вводятся с клавиатуры .

def is_int(value):  # Проверка введенного значения на целое число
    try:
        int(value)
        return True
    except ValueError:
        return False

def is_int_position(value): # Проверка что введенные позиции целые числа
    for i in value:
        if not is_int(i):
            return False
    return True

def is_position_in_range(value1, value2):   # Проверка что введенные позиции в диапазоне сгенерированоого списка
    for i in value1:
        if not (-1 < int(i) < len(value2)):
            return False
    return True

N = input('Введите число N: ')

while not is_int(N) or int(N) < 1:  # Проверка условий для введенного значения
    if not is_int(N):
        print('Введено не целое число')
        N = input('Введите целое число N: ')
        continue
    elif int(N) < 1:
        print('Число не может быть отрицательным или равным 0')
        N = input('Введите целое положительное число больше нуля: ')

N = int(N)

import random
list_random = []
for i in range(N):
    list_random.append(random.randint(-N, N))

print('Сгенерированный список: ', list_random)

print('Укажите позиции перемножаемых элементов:', end=' ')
list_position = list(input().split())

check = True 
while check: 
    if not is_int_position(list_position):
        print('Одна из указанных позиций не целое число')
        print('Укажите позиции перемножаемых элементов:', end=' ')
        list_position = list(input().split())
        continue
    if not is_position_in_range(list_position, list_random):
        print('Одна из указанных позиций вне диапазона списка')
        print('Укажите позиции перемножаемых элементов:', end=' ')
        list_position = list(input().split())
        continue
    check = False    
        
list_position = list(map(int, list_position))

result = 1
for i in range(len(list_position)):
    index = list_position[i]
    result *= list_random[index]

print('Произведение элементов на указанных позициях = ', round(result, 2))
