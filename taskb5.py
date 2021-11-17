# 5 транспортировать квадратную матрицу 

def matrix_size():
    rows=int(input('Enter number of rows '))
    columns=int(input('Enter number of columns '))
    return rows, columns

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

def transport_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(i , len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    return matrix

rows, columns = matrix_size()
matrix= matrix(rows, columns)    
matrix = transport_matrix(matrix)
for fin in matrix:
    print(fin) 