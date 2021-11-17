# ввести н строк с консоли, вывести лишь те строки длина которых меньше \ больше средней длины

n = int(input(' Enter n lines'))
lines = []
sunn=[]
lines_big_average=[]
for i in range(n):
    lines.append(input('inp: '))

for j in lines:
    sunn.append(len(j)) 

sum_= sum(sunn) 
average_length = sum_/n

for j in lines:
    if len(j) > average_length:
        lines_big_average.append(j)
for g in lines_big_average:
    print(len(g))
print(lines_big_average)
