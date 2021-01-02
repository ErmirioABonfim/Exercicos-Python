
dado = str(input('Informe o local onde nasceu: ')).strip()
dadoAux01 = dado.split()
print(dadoAux01)  

if 'Santo'.lower() in dadoAux01[0].lower() and len(dadoAux01[0]) == 5 :
    print('Sua cidade começa com a palavra santo ')
else:
    print('Sua cidade não começa com a palavra santo')


