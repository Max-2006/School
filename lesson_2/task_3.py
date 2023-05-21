a = 1
b = 2
c = 3
d = 4
e = 5

user_input = int(input('Введите число: '))

if a == user_input:
    print('Плохо')
elif b == user_input:
    print('Неудовлетворительно')
elif c == user_input:
    print('Удовлетворительно')
elif d == user_input:
    print('Хорошо')
elif e == user_input:
    print('Отлично')
else:
    print('Повторите еще раз')