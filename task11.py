# 10 используя оператор switch написать программу которая выводит на экран
# о пренадлежости некоторого обозначения К к интервалам (-10k, 5],(0, 10], (5, 15], (10, 10k]

def enter_number():
    k = int(input('enter number '))
    return k

def affiliation(k):
    if -10000 < k <= 5:
        if 0 < k <= 10:
            return (-10000, 5), (0, 10)
        return -10000, 5
    if 0 < k <= 10:
        if 5 < k <= 15:
            return (0, 10), (5, 15)
        return 0, 10 
    if 5 < k <= 15:
        if 10 < k <= 10000:
            return (5, 15), (10, 10000)
        return 5, 15
    if 10 < k <= 10000:
        return 10, 10000

k = enter_number()
af = affiliation(k)
print(f' number {k} concern {af} range')
