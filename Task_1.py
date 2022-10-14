# Напишите программу, которая принимает на вход вещественное число 
# и показывает сумму его цифр.

def is_float(value):    # Проверка введенного значения на вещественное число
    try:
        float(value)
        return True
    except ValueError:
        return False

number = input('Введите вещественное число: ')

while not is_float(number):  # Проверка условий для введенного значения
    print('Введено не вещественное число')
    number = input('Введите вещественное число: ')

sum = 0
for i in number:
    if not i.isdigit():
        continue
    sum += int(i)

print('Сумма цифр введенного числа', sum)
