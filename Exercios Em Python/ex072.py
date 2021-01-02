tupla = ('zero','um', 'dois', 'três', 'quatro', 'cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')


while True:
    numDig = int(input('Digite um número de 0 a 20: '))
    if numDig > 20 or numDig  < 0:
        print('Tente de novo: ')
    else:
        numDig = numDig
        print(' O número que você digitou foi {}'.format(tupla[numDig]))
        break
        
print('^-x-Fim-x-^')
        
        
        