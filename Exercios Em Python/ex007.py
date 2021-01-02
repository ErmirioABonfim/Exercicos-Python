notas = []

n1 = float (input('Primeira nota'))
n2 = float (input('Segunda nota'))
notas.append(n1)
notas.append(n2)
print('A média do aluno é: {}'.format((n1+n2)/len(notas)))
