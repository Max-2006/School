a = int(input('введите число "a": '))
b = int(input('введите число "b": '))
c = int(input('введите число "c": '))

print("Равнобедренный треугольник", ( a == b and b != c and c != a ) or \
                   ( b == c and c != a and a != b ) or ( c == a and a != b and b != c ))