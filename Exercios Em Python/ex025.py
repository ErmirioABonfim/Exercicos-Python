nome = str(input(' Informe seu nome completo: ').lower())
nomeAux = nome.split()
print(nome, len(nomeAux))
test = 0

for i in range(len(nomeAux)):
    if 'silva' == nomeAux[i]:
        print('Seu Nome contem Silva')
        test = 1
    else:
        test = 0
if test == 0:
    print('Seu nome não contem Silva')   

