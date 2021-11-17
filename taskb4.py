#  найти сумму элементов матрицы расположнных между первым и вторым 
#  положительными элементами каждой строки

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

def sum_of_segments(matrix):
    sum_of_segments = []
    for i in matrix:
        numbers =[]       
        tries = 0
        for j in i:
            if j > 0 and tries < 2:
                numbers.append(j)
                tries += 1
            elif tries ==1:
                numbers.append(j)
        sum_of_segments.append(sum(numbers))
    return sum_of_segments


rows, columns = matrix_size()
matrix= matrix(rows, columns)
sum_of_segments = sum_of_segments(matrix)
for fin in matrix:
    fin
    print(fin) 
print(f'sum of segments {sum_of_segments}')