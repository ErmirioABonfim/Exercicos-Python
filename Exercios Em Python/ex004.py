#Dissecando Uma Variável

a = input('Digite algo')
print('O tipo da variável é : ', type(a))
print('Tem somente espaçoso:', a.isspace())
print('É um número: ', a.isdigit())
print('É um número: ', a.isnumeric())
print('É alfabético: ', a.isalpha())
print('É alfanumérico:' , a.isalnum())
print('Está em Maiúsulas:' , a.isupper())
print('Está em Mnúsculas: ' , a.islower())
print('Está Capitalizada?:',a.istitle())

b = input('Digite algo')
c = type(a)

print('É um número? {}'.format(c))

