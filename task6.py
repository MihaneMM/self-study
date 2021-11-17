# 6 ввести н слов с консоли. 
# найти слово символы в котором идут в строгом порядке возрастания их кодов.
# если их несколько вывести первое из них.

def enter_n_str():
    n = int(input('enter to words'))
    return n

def spisok_words(n):
    words=[]
    for i in range(n):
        words.append(input('inp: '))
    return words


def converts_letters_to_number (word): # работает только при ['nvsdjn']
    numbers=[]
    for i in word:
        numbers.append(ord(i))
    return numbers

def is_ascending_order(numbers): # [1, 2, 3]
    for i in range(len(numbers)-1):
        if numbers[i] > numbers[i+1]:
            return False    
    return True

n = enter_n_str()
words = spisok_words(n)

for word in words:
    numbers = converts_letters_to_number(word)
    if is_ascending_order(numbers):
        print(word)
