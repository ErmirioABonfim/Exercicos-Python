import random
import emoji
from time import sleep
NumPC = random.randrange(0,5,1)
print('\033[1;31;47m -=-'*10)
NumUsuario= int(input('\033[1;33;42m Pense em um número e quando estiver pronto digite '))
print('-=-'*10)
print('\033[1;31;47m Processando...'.upper())
sleep(3)
if NumPC == NumUsuario:
    print(emoji.emojize('Parabéns você acertou :thumbsup:', use_aliases=True))
else:
    print(emoji.emojize('Você errou :hankey:', use_aliases=True))
    

print('Eu pensei no {}, Obrigado por jogar'.format(NumPC))