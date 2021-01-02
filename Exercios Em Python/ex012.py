precoProd = float(input('Qual o preço do produto? '))
desc = float(input('Informe o desconto'))
print('O produto de {} reais na promoção de {}% custará R$:{}'.format((precoProd),(desc),((precoProd - (precoProd*desc)/100.0))))
