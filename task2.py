# ввести n строк с консолиб упорядочить и вывести строки в порядке возрастания
n = int(input(' Enter n lines'))
lines = []

for i in range(n):
    lines.append(input('inp: '))


for buble in range(len(lines)):
    for i in range(len(lines)-1):
        if len(lines[i])>len(lines[i+1]):
            lines[i],lines[i+1]=lines[i+1],lines[i]

print(lines)