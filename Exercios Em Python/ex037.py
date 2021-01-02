#Conversor de base
num = int(input(' informe o número que deseja converter'))
print(""" Informe a base para converter
      [0] Binário 
      [1] Decimal
      [2] Octal
      [3] Hexadecimal
      """)
baseSel = int(input())

if baseSel == int (0):
    print('O número {} decimal em binário é: {}'.format(num,bin(num) ))
elif baseSel == int(1):
    print('O número {} decimal em decimal é: {}'.format(num,(num) ))
elif baseSel == int(2):
    print('O número {} decimal em Octal é: {}'.format(num,oct(num) ))
elif baseSel == int(3):
    print('O número {} decimal em hexadecimal o é: {}'.format(num,hex(num) ))

