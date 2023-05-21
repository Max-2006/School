a = int(input("Введите число 1 :"))
b = int(input("Введите число 2 :"))
c = int(input("Введите число 3 :"))

if a < b < c :
    print(a + c)
elif b < c < a :
    print(b + a)
elif c < a < b :
    print(c + b)
elif c < b < a :
    print(c + a)
elif a < c < b :
    print(a + b)
else:
    print('Повторите еще раз')