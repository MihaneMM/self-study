# 14 ввести число от 1 до 12. Вывести на консоль название месяца сообветствующее числу.
# осуществить проверку коректного ввода чисел.

def getNumber ():
    while True:
        getNumber = int(input('enter a number from 1 to 12: '))  
        if 0 < getNumber < 13: 
            return getNumber
            
def get_key(month, value):
    for k, v in month.items():
        if v == value:
            return k 

month = dict (
January=1,
February=2,
March=3, 
April=4,  
May=5,
June=6,
July=7,
August=8,
September=9,
October=10,
November=11,
December=12)

getNumber = getNumber()
value = getNumber
k=get_key(month, value)
print(k)

