# 10. Найти максимальный элемент(ы) в матрице и удалить из матрицы все
# строки и столбцы, его содержащие.

def matrix_size():
    rows=int(input('Enter number of rows '))
    columns=int(input('Enter number of columns '))
    return rows, columns

def matrix(rows, columns):
    import random
    matrix =[]

    for i in range(rows):
        one_str =[] # создаю список списков (матрицу)
        for j in range(columns):
            one_str.append(random.randint(-20, 50))
        matrix.append(one_str)
    return matrix

def max_number(matrix): # нахожу максимальный номер
    max_number=0
    for i in range(len(matrix)-1):
        for j in range(len(matrix[i])):
            if matrix[i][j] > max_number:
                max_number = matrix[i][j]  
    return max_number

def index_max_number(matrix, max_number):

    rows=[] # в каких строках и столбцах макс номер
    columns=[]
    for g in range(len(matrix)):
        for t in range(len(matrix[g])):
            if matrix[g][t] == max_number:
                rows.append(g)
                columns.append(t)

    return rows, columns

rows, columns = matrix_size()
matrix= matrix(rows, columns)
max_number= max_number(matrix)
print(f'max_number {max_number}')

rows, columns = index_max_number(matrix, max_number)
print(f'rows {rows}')
print(f'columns {columns}')

import numpy as np
for index in sorted(rows, reverse=True):
    del matrix[index]
for t in matrix:
    t=np.delete(t, columns)
    print(t)    
    