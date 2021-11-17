#4. Ввести n слов с консоли. Найти слово, в котором число различныхсимволов минимально.
#  Если таких слов несколько, найти первое изних.
n = int(input(' Enter n words'))
lines = []
word_min=100
names_k_v= {}
for i in range(n):
    lines.append(input('inp: '))


names_k_v= {}
for s in lines:
    number=len(s)
    for i in range(len(s) - 1):
        for j in range(i + 1, len(s)):
            if s[j] == s[i]:
                number-=1            
    
    names_k_v[s] = number
    
    if number < word_min:
        word_min=number 
print(word_min)

for k in names_k_v:
    if names_k_v[k] == word_min:
        print(k, names_k_v[k])


  