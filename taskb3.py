#  3 найти и вывести наибольшее число возрастающих (убывающих)
#    элементов матрицы идущих в подряд

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

def increasing_elements(matrix): # находим количество возврастающих эlементов в одной строке
    increasing = 0
  
    for i in matrix:
        number_of_times = 0
        for j in range(len(i)-1):               
            if i[j] < i[j+1]:
                number_of_times +=1
            if  i[j] > i[j+1]:
                number_of_times=0 
            if increasing < number_of_times:
                increasing = number_of_times
    return increasing

rows, columns = matrix_size()
matrix= matrix(rows, columns)
increasing = increasing_elements(matrix)
print(f'increasing {increasing}')

for fin in matrix:
    fin
    print(fin) 

