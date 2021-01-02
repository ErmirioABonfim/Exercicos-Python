num = str (input('Informe um número')) 
print('Analisando o número {} '.format(num))

for i in range(len(num)):
    if i == 0:
        print('Unidade {}'.format(num[3]))
    elif i == 1:    
        print('Dezena {}'.format(num[2]))
    elif i == 2:
        print('Centena {}'.format(num[1]))
    elif i == 3:
        print('Milhar {}'.format(num[0]))   
    
print('Fim de Análise')