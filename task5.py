# 5 ввести н слов с консоли. Найти количесто свов содержащие только символы латинского алфавита. 
# А среди них -количествослов с разным количеством гласных и согласных букв.

n = int(input('enter n words'))
words=[]

for i in range(n):
    words.append(input('inp: '))

k=0
m=0
vowels = list("aeiouyAEIOUY")
consonants = list("bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ")

for i in range(len(words)):
    if words[i]>='a' and words[i] <='z': 
        k+=1

for i in words:
    number_of_vowels = sum(x in vowels for x in i)
    number_of_consonants = sum(x in consonants for x in i)
    if number_of_vowels == number_of_consonants:
        m+=1

print(f'words of the Latin alphabet {k}, vowels and consonants = {m}')