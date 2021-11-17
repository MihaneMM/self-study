# 14 ввести число от 1 до 12. Вывести на консоль название месяца сообветствующее числу.
# осуществить проверку коректного ввода чисел.

def getNumber ():
    while True:
        k = int(input('enter a number from 1 to 12: '))  
        if 0 < k < 13: 
            return k
            
month = {
1 : 'January',
2: 'February',
3: 'March', 
4: 'April',  
5: 'May',
6: 'June',
7: 'July',
8: 'August',
9: 'September',
10: 'October',
11: 'November',
12: 'December'}

k=getNumber() 
print(month[k])
