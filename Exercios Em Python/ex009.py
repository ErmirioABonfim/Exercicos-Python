num = int(input('Digite um número para er sua tabuada'))
d = 0
print('-'*12)
for i in range (10):
    result = num * d
    print('{} Vezes {} é: {}'.format((num),(d),(result)))
    d = d+1
print('-'*12)