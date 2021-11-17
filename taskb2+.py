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
    matrix =[]
    x=1
    for i in range(rows):
        one_str =[]
        for j in range(columns):
            one_str.append(x)
            x+=1
        matrix.append(one_str)
    return matrix

def shift(matrix, steps): # сдвиг столбцов
    if steps < 0:
        steps = abs(steps)
        for i in range(steps):
            for fun in matrix:
                fun.append(fun.pop(0))
    else:
        for i in range(steps):
            for fun in matrix:
                fun.insert(0, fun.pop())
    return matrix

rows, columns, steps = matrix_size()
matrix= matrix(rows, columns)
matrix = shift (matrix, steps)

for fin in matrix:
    fin
    print(fin) 