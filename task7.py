# 7 ввести н слов с консоли. найти слово состоящее только из разных символов.
# если таких слов несколько вывести первое из них

# + ввести количество вводимых слов
# + ввести эти слова, добавить в список
# + сравнить одинаковы ли символы в слове
# + вывести слово с одинаковыми символами

def enter_n_str():
    n = int(input('enter to words'))
    return n

def spisok_words(n):
    words=[]
    for i in range(n):
        words.append(input('inp: '))
    return words

def is_unique(word): # ['dvuhd']
    for i in range(len(word)-1):
        for j in range(i + 1, len(word)):
            if word[j] == word[i]:
                return False
    return True

n = enter_n_str()
words = spisok_words(n)

for word in words:
    if is_unique(word):
        print(word)
