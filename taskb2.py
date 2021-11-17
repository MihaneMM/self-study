# ввести с консоли н - размерность матрицы a[n][n].
# задать значения элементов матрицы в интервале зачений от -н до н
# с помощью датчика случайных чисел 
# 2 выполнить циклический сдвиг матрицы на к позиций в право (влево, вверх, низ)

def matrix_size():
    rows=int(input('Enter number of rows '))
    columns=int(input('Enter number of columns '))
    steps=int(input('Enter number lifting up '))
    return rows, columns, steps

def matrix(rows, columns):
    import random
    matrix =[]

    for i in range(rows):
        one_str =[] # создаю список списков (матрицу)
        for j in range(columns):
            one_str.append(random.randint(-20, 50))
        matrix.append(one_str)
    return matrix

def shift(matrix, steps): # опускание
    if steps < 0:
        steps = abs(steps)
        for i in range(steps):
            matrix.append(matrix.pop(0))
    else:
        for i in range(steps):
            matrix.insert(0, matrix.pop())
    return matrix

rows, columns, steps = matrix_size()
matrix = matrix(rows, columns)
matrix = shift(matrix, steps)

for fin in matrix:
    print(fin) 