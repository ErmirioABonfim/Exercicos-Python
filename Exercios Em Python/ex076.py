listaPrecos = ('lapis', 1.75,
               'borracha',2,
               'caderno',15.91,
               'estojo',25,
               'transferidor',4.20,
               'compasso',9.99,
               'mochila',120.32,
               'caneta',22.30,
               'livro',34.90)

print('-'* 40)
print(f'{"Listagem de preços":^40}'.upper())
print('-'*40)


for pos in range(len(listaPrecos)):
    if pos % 2 == 0:
        print(listaPrecos[pos])
    else:
        print(f'{}'