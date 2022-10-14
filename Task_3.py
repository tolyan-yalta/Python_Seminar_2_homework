# Задайте список из n чисел последовательности (1 + 1/n)^n 
# и выведите на экран их сумму.

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

print('{', end="")
sum = 0
for i in range(1, int(N) + 1):
    temp = round((1 + 1 / i) ** i, 2)
    print(f'{i}: {temp}', end="")
    sum += temp
    if i == int(N):
        print('}')
        break
    print(',', end=' ')

print('Сумма чисел последовательности = ', round(sum, 2))
