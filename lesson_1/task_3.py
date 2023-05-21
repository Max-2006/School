a = int(input('введите число "a": '))
b = int(input('введите число "b": '))
c = int(input('введите число "c": '))

if a == b and a != c or b != c:
    print(True)
elif b == c and b != a or a != c:
    print(True)
elif c == a and c != b or a != b:
    print(True)
else:
    print(False)
