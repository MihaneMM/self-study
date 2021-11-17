# ввести с консоли н - размерность матрицы a[n][n].
# задать значения элементов матрицы в интервале зачений от -н до н
# с помощью датчика случайных чисел 

# 1 упорядочить стоки (столбцы) матрицы в порядке возрастания значений
# элементов к-го столбца(стороки)

def matrix_size():
    rows=int(input('Enter number of rows'))
    columns=int(input('Enter number of columns'))
    return rows, columns

def matrix(rows, columns):
    import random
    matrix =[]

    for i in range(rows):
        one_str =[] # создаю список списков (матрицу)
        for j in range(columns):
            one_str.append(random.randint(-20, 50))
        matrix.append(one_str)

        for g in range(len(matrix)): # сортирую строки по их сумме 
            for j in range(len(matrix)-1):
                if sum(matrix[j]) > sum(matrix[j+1]):
                    matrix[j], matrix[j+1] = matrix[j+1], matrix[j]
    return matrix

rows, columns = matrix_size()
matrix= matrix(rows, columns)

for fin in matrix:
    fin.sort() # сортирую числа внутри каждой строки 
    print(fin) 