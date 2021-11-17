# 12 написать программу которая выводит числа от 1 до 25 
# в виде матрицы  5х5 слева на право сверху вниз

def rows():
    rows=int(input('Enter number of rows'))
    return rows

def columns():
    columns=int(input('Enter number of columns'))
    return columns

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

rows=rows()
columns = columns()
matrix = matrix(rows, columns)

for fin in matrix:
    print(fin) 