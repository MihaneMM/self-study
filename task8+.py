# 8 ввести н слов с консоли. среди слов состоящих только из цифр
# найти слово палиндром.Если таких слов больше одного найти второе из них.

def enter_n_str():
    n = int(input('enter to numbers '))
    return n

def get_words(n):
    words=[]
    for i in range(n):
        words.append(input('inp: '))
    return words

n = enter_n_str()
words = get_words(n)
palindrome=[]

for word in words:
    if word == word[::-1]:
        palindrome.append(word)

if len(palindrome) > 1:
    print(palindrome[1])
else:
    print(palindrome)