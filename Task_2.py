# Напишите программу, которая принимает на вход число N 
# и выдает набор произведений чисел от 1 до N.

def is_int(value):  # Проверка введенного значения на целое число
    try:
        int(value)
        return True
    except ValueError:
        return False


N = input('Введите число N: ')

while not is_int(N) or int(N) < 1:  # Проверка условий для введенного значения
    if not is_int(N):
        print('Введено не целое число')
        N = input('Введите целое число N: ')
        continue
    elif int(N) < 1:
        print('Число не может быть отрицательным или равным 0')
        N = input('Введите целое положительное число больше нуля: ')

temp = 1
for i in range(1, int(N) + 1):
    temp *= i
    print(temp, end=' ')

