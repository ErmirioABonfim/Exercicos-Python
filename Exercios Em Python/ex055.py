
pesos = [float(input('Informe peso 01:  ')),
         float(input('Informe peso 02:  ')),
         float(input('Informe peso 03:  ')),
         float(input('Informe peso 04:  '))   
         ]
maior = pesos[0]
menor = pesos[0]
for i in range(len(pesos)):
    pesoA = pesos[i]#Posição atual      
    if i > 0:    
        if pesoA > maior:
            maior = pesoA
        if pesoA < menor:
            menor = pesoA
                   
print('-x-'*15) 
print('O maior peso é: ',maior)
print('-x-'*15) 
print('O menor peso é: ',menor)
print('-x-'*15) 
