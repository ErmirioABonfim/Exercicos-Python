DiasAlugados = int (input('Informe os dias Alugados'))
kmRodados = float(input('Informe os Km rodados'))
valDiaria = float(input('Informe valor da diária '))
valKm = float(input("Informe o valor do Km Rodado"))
ValorPagar = (DiasAlugados * valDiaria) + (kmRodados*valKm)
print('Com {} dias alugados e  {} Km rodados considerando os valores de diária e de KM rodado o valor a pagar é de : R${}'.format((DiasAlugados),(kmRodados),(ValorPagar)))
