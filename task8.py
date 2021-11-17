# 8 ввести н слов с консоли. среди слов состоящих только из цифр
# найти слово палиндром.Если таких слов больше одного найти второе из них.

# найти слово палиндром
# если их больше 1 вывести второе

def enter_n_str():
    n = int(input('enter to numbers '))
    return n

def get_words(n):
    words=[]
    for i in range(n):
        words.append(int(input('inp: ')))
    return words

def is_Palindrome(number): # сработать через символы  слово  
    reversed_number = 0
    tmp_original = number
    
    while tmp_original > 0:
        reversed_number = (reversed_number * 10) + tmp_original % 10
        tmp_original = tmp_original // 10
    
    if number == reversed_number:
        return True

n = enter_n_str()
words = get_words(n)
palindrome=[]
for number in words:
    if is_Palindrome(number):
        palindrome.append(number)

if len(palindrome) > 1:
    print(palindrome[1])
else:
    print(palindrome)
