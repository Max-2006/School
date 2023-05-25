a = 1
b = 1

user_read_1 = int(input('Введите число "x":'))
user_read_2 = int(input('Введите число "y":'))
user_read_3 = int(input('Введите число "z":'))
if a * b > user_read_1 * user_read_2 or user_read_2 * user_read_3 or user_read_3 * user_read_1:
    print('Все подходит')
else:
    print('Не подходит')