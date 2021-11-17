# 13 написать прогграмму позволяющию коректно ноходить корни квадратного уравнения.
# параметры уравнения дожны задаваться с командной строки

print('Solving the equation a•x²+b•x+c=0')
a = input(' Enter to number a: ')
b = input(' Enter to number b: ')
c = input(' Enter to number c: ')
a = float(a)
b = float(b)
c = float(c)
discriminant = b**2 - 4*a*c
print('discriminant = ' + str(discriminant))
if discriminant < 0:
    print('There are no roots')
elif discriminant == 0:
    x = -b / (2 * a)
    print('x = ' + str(x))
else:
    x1 = (-b + discriminant ** 0.5) / (2 * a)
    x2 = (-b - discriminant ** 0.5) / (2 * a)
    print('x1 = ' + str(x1))
    print('x2 = ' + str(x2))
   