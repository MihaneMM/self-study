# 10 используя оператор switch написать программу которая выводит на экран
# о пренадлежости некоторого обозначения К к интервалам (-10k, 0],(0, 5], (5, 10], (10, 10k]

def enter_number():
    k = int(input('enter number '))
    return k

def affiliation(k):
    if -10000 < k <= 0:
        return -10000, 0
    elif 0 < k <= 5:
        return 0, 5 
    elif 5 < k <= 10:
        return 5, 10
    elif 10 < k <= 10000:
        return 10, 10000


k = enter_number()
af = affiliation(k)
print(f' number {k} concern {af} range')